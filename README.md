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

- Clone the repository:
`git clone https://github.com/Marlinekhavele/Contact-Centre-API `

- cd `chat`

Set up PostgreSQL database:
```shell
  # Ubuntu
   - sudo apt-get update
   - sudo apt-get install postgresql postgresql-contrib
   # macOS
   - brew install postgresql

  # Switch to the PostgreSQL user
  - sudo -i -u postgres
  # linux
  - psql

  # Open PostgreSQL shell Mac
  -  brew services start postgres
  -  psql postgres

  # Create a new user 
  - CREATE USER postgres WITH PASSWORD 'password';

  # Create the database
  - CREATE DATABASE ticket_assignment;

  # Grant privileges to the user
  - GRANT ALL PRIVILEGES ON DATABASE ticket_assignment TO postgres;

  # Exit the PostgreSQL shell
   - \q
```
Create and activate a virtual environment: [install pyenv](https://ericsysmin.com/2024/02/05/how-to-install-pyenv-on-macos/)
```shell
pyenv virtualenv venv
pyenv activate venv
```

Install dependencies:
```shell
pip install -r requirements.txt
```

Set up the database:
```shell
python manage.py makemigrations
python manage.py migrate
```

Create a superuser:
```shell
python manage.py createsuperuser
```
Set up environment variables in a `.env` file:
```shell
SECRET_KEY=secretkey
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_USER=postgres
DB_HOST=localhost
DB_NAME=ticket_assignment
DB_PASSWORD=password
REDIS_LOCATION=redis://127.0.0.1:6379/1
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

Source the env file: `source .env`
```
Access the admin interface with the above command:
```shell
http://127.0.0.1:3000/admin/
```
Start the development server:
```shell
python manage.py runserver 
```

In a separate terminal, start Celery:
```shell
celery -A chat worker -l info
```
In a separate termial ensure redis is running 
```shell
redis-cli ping
```

#### Usage
The application provides the following API endpoints:
```shell
/api/token/: gives the token that will be used on the Agent API
/api/v1/tasks/: CRUD operations for tasks
/api/v1/agents/: CRUD operations for agents and they have to be authenticated
/api/v1/tickets/: CRUD operations for tickets
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
Example: Create a ticket
```bash
POST /api/v1/create-ticket/
{
    "id": "51b6f80a-a172-4c1f-9a21-346ed97d492c",
    "restriction": {},
    "platform": "facebook_chat",
    "priority": 2147483647
}
```
Example: List ticket
```bash
GET /api/v1/tickets/
[
    {
        "id": "e4df3854-8f66-44d0-8e26-2693c65ae105",
        "restriction": [
            "test",
            "tick"
        ],
        "platform": "facebook_chat",
        "priority": 0
    }
]
```
Example: Create a token
```bash
POST /api/token/
{
  "username": "flix",
  "password": "12345"
}

```
The system will automatically attempt to assign the task to an available agent based on the defined rules and priorities.

- `MAX_CALL_TASKS`: Maximum number of simultaneous voice calls for an agent (default: 3)
- `MAX_OTHER_TASKS`: Maximum number of simultaneous text-based tasks for an agent (default: 4)
- `TASK_PRIORITY`: Priority levels for different task types

#### Testing
Run the test suite with:
```bash
python manage.py test
```

#### Lint
Run Lint:
```bash
make lint
```

### Deployment
For production deployment:
Set `DEBUG = False` in settings.py

### DockerFile
A Dockerfile is provided for containerized deployment of the application. The service can be easily started and stopped using make commands.
Running the Service Locally:
```bash
make serve
```
Stopping the Service:
```bash
make stop
```
Restarting the Service:
```bash
make start
```

N/B
- when you think of seasonality the whole design changes 