# ⚙️ TaskTrackr Backend

Backend for **TaskTrackr**, a full-stack productivity and task management app.  
Built with **Django REST Framework**, **JWT Authentication**, and **PostgreSQL (via Docker Compose)**.

---

## 🚀 Tech Stack

- **Python 3.11+**
- **Django 4.2**
- **Django REST Framework**
- **Simple JWT (Authentication)**
- **PostgreSQL**
- **Docker & Docker Compose**
- **Gunicorn** (for production)

---

## 🧩 Features

✅ User registration & authentication (JWT)  
✅ Project and Task CRUD with relations  
✅ Token-based authorization (access & refresh)  
✅ RESTful API design with automatic schema generation  
✅ Dockerized PostgreSQL + backend for easy setup

---

## ⚙️ Local Development Setup

### 1️⃣ Clone repository
```
git clone <repo-url>
cd tasktrackr-pro/backend
```
# 2️⃣ Environment variables
Create a .env file in the backend folder:
```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_NAME=tasktrackr_db
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=db
DATABASE_PORT=5432
```
# 3️⃣ Run via Docker
```
docker compose up --build
```
✅ Backend → http://localhost:8000/api/
✅ PostgreSQL → localhost:5432

## 🧠 API Endpoints
```
| Method     | Endpoint                    | Description          |
| ---------- | --------------------------- | -------------------- |
| **POST**   | `/api/users/register/`      | Register new user    |
| **POST**   | `/api/users/token/`         | Obtain JWT tokens    |
| **POST**   | `/api/users/token/refresh/` | Refresh access token |
| **GET**    | `/api/projects/`            | List all projects    |
| **POST**   | `/api/projects/`            | Create new project   |
| **GET**    | `/api/tasks/`               | List all tasks       |
| **POST**   | `/api/tasks/`               | Create new task      |
| **PATCH**  | `/api/tasks/<id>/`          | Update task status   |
| **DELETE** | `/api/tasks/<id>/`          | Delete task          |

```

## 🧱 Models Overview
# 👤 User
- username
- email
- password (hashed)

# 📁 Project
- name
- description
- created_at
- related tasks (OneToMany)

# ✅ Task
- title
- description
- status (pending, in_progress, done)
- due_date
- project (ForeignKey → Project)

## 🧪 Testing
# Run backend tests:
```
docker compose exec backend python manage.py test
```
Example output:
```
Ran 10 tests in 1.35s
OK
```
# 🐳 Docker Compose Overview
```
version: "3.9"

services:
  backend:
    build: .
    command: gunicorn backend.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: tasktrackr_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```
# 🔐 Authentication Flow
- Register → /api/users/register/
- Login → /api/users/token/
- Copy access token
- Use it in headers:
```
Authorization: Bearer <access_token>
```
# 🌍 Deployment
Deployed via Gunicorn + Docker Compose.
Can easily be extended for Render, Railway, or AWS ECS deployments.

## 🧩 Author
Developed by Özkan Çimenli
📧 cimenliozkan1@gmail.com