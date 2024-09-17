FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /chat

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /chat/

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "chat.wsgi:application"]