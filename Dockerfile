# Dockerfile

FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

# Install pipenv and dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pip install importlib-metadata
RUN pipenv install --system --dev

# Copy wait-for-it.sh and give it execute permissions
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Copy the rest of the application code
COPY . /code/

# Set the working directory to the app folder
WORKDIR /code

# Command to run the application using uvicorn
CMD ["/wait-for-it.sh", "db:5432", "--", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
