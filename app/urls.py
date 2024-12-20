from django.urls import path

from app.views.agent import (
    CreateAgentView,
    ListAgentView,
    RetrieveDestroyUpdateAgentView,
)
from app.views.task import CreateTaskView, ListTaskView, RetrieveDestroyUpdateTaskView
from app.views.ticket import (
    CreateTicketView,
    ListTicketView,
    RetrieveDestroyUpdateTicketView,
)

urlpatterns = [
    # Agent urls
    path("agents/", ListAgentView.as_view(), name="agents-list"),
    path("create-agent/", CreateAgentView.as_view(), name="create-agent"),
    path(
        "agents/<uuid:id>/",
        RetrieveDestroyUpdateAgentView.as_view(),
        name="agents-get-delete-update",
    ),
    # Task urls
    path("tasks/", ListTaskView.as_view(), name="tasks-list"),
    path("create-task/", CreateTaskView.as_view(), name="create-task"),
    path(
        "tasks/<uuid:id>/",
        RetrieveDestroyUpdateTaskView.as_view(),
        name="tasks-get-delete-update",
    ),
    # Ticket urls
    path("tickets/", ListTicketView.as_view(), name="tickets-list"),
    path("create-ticket/", CreateTicketView.as_view(), name="create-ticket"),
    path(
        "tickets/<uuid:id>/",
        RetrieveDestroyUpdateTicketView.as_view(),
        name="tickets-get-delete-update",
    ),
]
