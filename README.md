# TodoApp — FastAPI Full-Stack Application

A full-stack todo application built with FastAPI, PostgreSQL, and JWT authentication. Includes user registration, role-based authorization, a server-rendered Jinja2 frontend, and a comprehensive test suite.

**Live demo:** https://todo-fastapi-doim.onrender.com

## Features

- User registration and login with JWT-based authentication
- Password hashing with bcrypt
- Role-based access control (admin routes)
- Full CRUD for todos, scoped per user
- Server-rendered HTML frontend with Jinja2 templates
- REST API with automatic OpenAPI docs at `/docs`
- Alembic database migrations
- 27+ unit and integration tests

## Tech Stack

- **Backend:** FastAPI, SQLAlchemy, Pydantic
- **Database:** PostgreSQL
- **Auth:** JWT (python-jose), bcrypt
- **Frontend:** Jinja2 templates, Bootstrap, vanilla JS
- **Testing:** pytest, pytest-asyncio
- **Migrations:** Alembic
- **Deployment:** Render

## Screenshots

![Login Page](./docs/screenshots/login.png)
![Todo Dashboard](./docs/screenshots/dashboard.png)
![Swagger API Docs](./docs/screenshots/swagger.png)



## Local Setup

### Prerequisites

- Python 3.11+
- PostgreSQL running locally

### Installation

1. Clone the repository:
```bash
   git clone https://github.com/thomasfere/FastAPI.git
   cd FastAPI
```

2. Create and activate a virtual environment:
```bash
   python -m venv fastapienv
   source fastapienv/bin/activate  # On Windows: fastapienv\Scripts\activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Create a `.env` file in the project root (see `.env.example`):

DATABASE_URL=postgresql://user:password@localhost/TodoApplicationDatabase
SECRET_KEY=your-secret-key-here



5. Create the database:
```bash
   createdb TodoApplicationDatabase
```

6. Run migrations:
```bash
   alembic upgrade head
```

7. Start the server:
```bash
   uvicorn TodoApp.main:app --reload
```

Visit `http://localhost:8001` to use the app, or `http://localhost:8001/docs` for the interactive API documentation.

## Running Tests

```bash
pytest --disable-warnings
```

Tests use an in-memory SQLite database and mock authentication via FastAPI's dependency override system.


## API Overview

Interactive docs available at `/docs` when the server is running.

Key endpoints:

- `POST /auth/` — Register a new user
- `POST /auth/token` — Log in, receive JWT
- `GET /todos/` — List authenticated user's todos
- `POST /todos/todo` — Create a todo
- `PUT /todos/todo/{id}` — Update a todo
- `DELETE /todos/todo/{id}` — Delete a todo
- `GET /admin/todo` — List all todos (admin only)

## License

MIT