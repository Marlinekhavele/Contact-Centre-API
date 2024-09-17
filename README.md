## Contact Center Task 
This Django-based application manages task assignments for a multilingual contact center, supporting multiple communication channels and automated agents.

### Features

- Multilingual support (EN, DE, FR, IT, and others)
- Multi-channel support (voice calls, emails, Facebook Messenger, website chat)
- Automated task assignment algorithm
- Priority-based queueing system
- Celery for asynchronous task processing

### Requirements

- Python 3.11
- Django 3.2+
- Django REST Framework
- Celery
- Redis
- PostgreSQL

### Installation

1. Clone the repository:
`git clone https://github.com/Marlinekhavele/Contact-Centre-API `
cd chat

2. Create and activate a virtual environment:
`python -m venv env`
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required packages:
`pip install -r requirements.txt`

4. Set up the database:
` python manage.py migrate`

5. Create a superuser:
` python manage.py createsuperuser`

6. Start the development server:
` python manage.py runserver `

7. In a separate terminal, start Celery:
` celery -A chat worker -l info`

#### Usage
The application provides the following API endpoints:
```bash
- /api/tasks/: CRUD operations for tasks
- /api/agents/: CRUD operations for agents
- /api/tickets/: CRUD operations for tickets
```
You can interact with these endpoints using tools like cURL, Postman, or the built-in Django REST Framework browsable API.
Example:List a task 
```bash
GET /api/v1/tasks/
Content-Type: application/json
    {
        "id": "742b5a39-5622-4aa2-923e-99d8d4d1d4dd",
        "ticket": "09aa214f-3ca0-4152-8788-4330af53211a",
        "created_at": "2024-09-17T05:06:13.804241Z",
        "updated_at": "2024-09-17T05:06:13.804330Z",
        "agent": "c4c26be4-a2aa-43f0-a365-3039d5391f65",
        "status": "in_progress"
    }
```
Example: Create a task 
```bash
POST /api/v1/create-task/
{
    "id": "b1373489-e638-4192-beb1-6bd33196d09d",
    "ticket": "f6fff39b-1036-4d82-8d88-c7f3ef420f25",
    "created_at": "2024-09-17T10:47:15.508472Z",
    "updated_at": "2024-09-17T10:47:15.508665Z",
    "agent": "abd72992-5d57-4be2-9251-bf94847ae599",
    "status": "open"
}
```
The system will automatically attempt to assign the task to an available agent based on the defined rules and priorities.

- `MAX_CALL_TASKS`: Maximum number of simultaneous voice calls for an agent (default: 3)
- `MAX_OTHER_TASKS`: Maximum number of simultaneous text-based tasks for an agent (default: 4)
- `TASK_PRIORITY`: Priority levels for different task types

#### Testing
Run the test suite with:
`python manage.py test`

### Deployment
For production deployment:
Set `DEBUG = False` in settings.py

- A Dockerfile is provided for containerized deployment.

N/B

- `.env` file is exposed on Github just to ease on environment variables sharing ideally this is not recommended and can cause a huge security risk lets just ignore it for now on this project.