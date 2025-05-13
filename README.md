# URL Shortener
A Flask-based URL shortener with PostgreSQL and Redis.

## Setup
1. Install Docker and Python.
2. Create a `.env` file with `SECRET_KEY`, `DATABASE_URL`, and `REDIS_URL`.
3. Run `docker-compose up`.
4. Access at `http://localhost:5000`.

## Features
- Shorten URLs with unique codes.
- Redirect short URLs to original URLs.
- Track clicks with IP and user agent.
- View click statistics.

## Running Tests
```bash
pytest
