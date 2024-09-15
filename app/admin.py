from django.contrib import admin
from .models import Agent, Task, Ticket

# Register your models here.
admin.site.register(Agent)
admin.site.register(Task)
admin.site.register(Ticket)

