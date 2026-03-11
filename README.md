# Blog API with Redis Cache

Test assignment: Python Backend Developer

---

## Stack

- FastAPI  
- PostgreSQL  
- Redis  
- SQLAlchemy (async)  
- Docker Compose

---

## Architecture

Client > FastAPI Router > Service Layer > Redis Cache > Repository > PostgreSQL

---

## Cache strategy

### cache-aside

GET /posts/{id}

1. check Redis  
2. if cache miss → query Postgres  
3. store result in Redis

cache TTL: 3600 seconds

---

## Quick Start

### 1. Clone repository

```bash
git clone https://github.com/Madmammoth/blog-cache-api.git  
cd blog-cache-api
```

### 2. Configure environment

```bash
cp .env.example .env
```

### 3. Run services

```bash
docker compose up --build
```

---

## API docs:

```
http://localhost:8000/docs
```

---

## API

### Create post

```
POST /posts
```

### Get post

```
GET /posts/{id}
```

### Update post

```
PUT /posts/{id}
```

### Delete post

```
DELETE /posts/{id}
```

---

## Tests

```bash
docker compose exec api python -m pytest -v
```

- cache miss  
- cache hit
- cache invalidation on update

---

## Database

### PostgreSQL

Optimization: index on the title column

---

## Docker Services

- postgres
- redis
- api