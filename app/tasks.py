import redis
from celery import shared_task
from django.db import transaction
from django.utils import timezone

from .models import Agent, Task

redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)

MAX_CALL_TASKS = 3
MAX_OTHER_TASKS = 4
HIGH_PRIORITY = 1
NORMAL_PRIORITY = 0


@shared_task
def assign_task(task_id):
    with transaction.atomic():
        task = Task.objects.select_for_update().get(id=task_id)
        ticket = task.ticket

        priority = HIGH_PRIORITY if ticket.platform == "call" else NORMAL_PRIORITY
        ticket.priority = priority
        ticket.save()

        available_agents = Agent.objects.filter(
            language_skills__contains=ticket.restriction
        )

        for agent in available_agents:
            assigned_tasks = agent.assigned_tasks
            if ticket.platform == "call":
                if (
                    "call" not in assigned_tasks
                    and len(assigned_tasks) < MAX_CALL_TASKS
                ):
                    assign_to_agent(task, agent)
                    return
            else:
                if len(assigned_tasks) < MAX_OTHER_TASKS:
                    assign_to_agent(task, agent)
                    return

        redis_client.zadd("task_queue", {str(task.id): priority})


def assign_to_agent(task, agent):
    task.agent = agent
    task.status = "in_progress"
    task.save()
    agent.assigned_tasks.append(task.ticket.platform)
    agent.save()


@shared_task
def process_task_queue():
    while True:
        task_id = redis_client.zpopmax("task_queue")
        if not task_id:
            break

        task = Task.objects.get(id=task_id[0].decode())
        assign_task(task.id)


@shared_task
def check_completed_tasks():
    ten_minutes_ago = timezone.now() - timezone.timedelta(minutes=10)
    in_progress_tasks = Task.objects.filter(
        status="in_progress", updated_at__lte=ten_minutes_ago
    )

    for task in in_progress_tasks:
        task.status = "done"
        task.save()

        agent = task.agent
        agent.assigned_tasks.remove(task.ticket.platform)
        agent.save()
