# Amnesty Collab

A Django REST Framework backend with a Vue.js frontend.

## Requirements

- Python 3.13 or later
- Node.js 20 or later and npm for the Vue frontend
- Docker and Docker Compose (optional)

## Environment setup

Copy the example environment file and update values for your machine:

```bash
cp .env.example .env
```

For local SQLite development, use these values in `.env`:

```env
DJANGO_SECRET_KEY=replace-with-a-development-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_ENGINE=django.db.backends.sqlite3
DATABASE_NAME=db.sqlite3
VITE_API_URL=http://localhost:8000/api
```

Do not commit `.env` or production secrets.

## Start the Django backend locally

Create and activate a virtual environment, then install the dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Apply migrations and start the development server:

```bash
python manage.py migrate
python manage.py runserver
```

The backend is available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Start with Docker

The Compose service runs Django on port `8000`:

```bash
docker compose up --build
```

Apply migrations from another terminal when the container is running:

```bash
docker compose exec web python manage.py migrate
```

Stop the service with:

```bash
docker compose down
```

## Start the Vue frontend

The frontend uses Vite and should live in a frontend directory with its own `package.json`. Once the Vue frontend is present:

```bash
cd frontend
npm install
```

Create `frontend/.env` with the backend URL:

```env
VITE_API_URL=http://localhost:8000/api
```

Start the frontend development server:

```bash
npm run dev
```

Vite normally serves the frontend at [http://localhost:5173/](http://localhost:5173/).

## Useful commands

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py test
python manage.py createsuperuser
```

The Django admin is available at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) after creating a superuser.
