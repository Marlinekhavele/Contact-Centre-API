from celery import shared_task
from django.utils import timezone
from .models import Task, Agent
from django.db import transaction
import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@shared_task
def assign_task(task_id):
    with transaction.atomic():
        task = Task.objects.select_for_update().get(id=task_id)
        ticket = task.ticket
        
        # Set priority based on platform (call has higher priority)
        priority = 1 if ticket.platform == 'call' else 0
        
        available_agents = Agent.objects.filter(language_skills__contains=ticket.restriction)

        for agent in available_agents:
            assigned_tasks = agent.assigned_tasks
            if ticket.platform == 'call':
                if 'call' not in assigned_tasks and len(assigned_tasks) < 3:
                    assign_to_agent(task, agent)
                    return
            else:
                if len(assigned_tasks) < 4:
                    assign_to_agent(task, agent)
                    return

        # If no agent is available, queue the task
        redis_client.zadd('task_queue', {str(task.id): priority})

def assign_to_agent(task, agent):
    task.agent = agent
    task.status = 'in_progress'
    task.save()
    agent.assigned_tasks.append(task.ticket.platform)
    agent.save()

@shared_task
def process_task_queue():
    while True:
        # Get the highest priority task from the queue
        task_id = redis_client.zpopmax('task_queue')
        if not task_id:
            break

        task = Task.objects.get(id=task_id[0].decode())
        assign_task(task.id)

@shared_task
def check_completed_tasks():
    ten_minutes_ago = timezone.now() - timezone.timedelta(minutes=10)
    in_progress_tasks = Task.objects.filter(status='in_progress', updated_at__lte=ten_minutes_ago)
    
    for task in in_progress_tasks:
        task.status = 'done'
        task.save()
        
        agent = task.agent
        agent.assigned_tasks.remove(task.ticket.platform)
        agent.save()