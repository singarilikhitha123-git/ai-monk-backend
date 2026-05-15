# AI Monk – Backend

A FastAPI backend for storing and retrieving **Nested Tags Tree** hierarchies using PostgreSQL (Neon).

## Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy ORM
- PostgreSQL (Neon serverless)
- Pydantic

## Features

- `GET /trees` — fetch all saved tree hierarchies
- `POST /trees` — save a new tree hierarchy
- `PUT /trees/{id}` — update an existing tree hierarchy
- Tree data stored as JSON in PostgreSQL
- CORS enabled for frontend access
- Auto-creates the `trees` table on startup

## Project Structure

```
backend/
  main.py          # FastAPI app, routes
  models.py        # SQLAlchemy Tree model
  database.py      # DB engine and session setup
  requirements.txt
  .env.example
```

## Getting Started

### Prerequisites

- Python 3.10+
- A PostgreSQL database (e.g. [Neon](https://neon.tech))

### Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create env file
cp .env.example .env
# Edit .env and add your DATABASE_URL

# Start server
uvicorn main:app --reload --port 8000
```

API runs at `http://localhost:8000`

Interactive docs at `http://localhost:8000/docs`

## Environment Variables

| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string |

Example:
```
DATABASE_URL=postgresql://user:password@host/dbname?sslmode=require
```

## Database Schema

```sql
CREATE TABLE trees (
  id         SERIAL PRIMARY KEY,
  tree       JSON NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now()
);
```

## API Reference

### GET /trees
Returns all saved trees.
```json
[
  { "id": 1, "tree": { "name": "root", "children": [...] } }
]
```

### POST /trees
Save a new tree.
```json
// Request body
{ "tree": { "name": "root", "children": [...] } }

// Response
{ "id": 1, "tree": { ... } }
```

### PUT /trees/{id}
Update an existing tree.
```json
// Request body
{ "tree": { "name": "root", "children": [...] } }

// Response
{ "id": 1, "tree": { ... } }
```

## Deployment

Deployed on **Render**. Set `DATABASE_URL` in Render's Environment Variables.

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
