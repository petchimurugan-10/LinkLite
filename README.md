# URL Shortener

A simple and efficient URL shortening service built with Flask, PostgreSQL, and Redis. This project allows users to shorten long URLs, redirect using shortened URLs, and view click statistics for each shortened URL. It includes URL validation, caching with Redis, and click tracking.

## Features

- **URL Shortening**: Convert long URLs into short, shareable links.
- **Redirection**: Redirect shortened URLs to their original links.
- **Click Tracking**: Track the number of clicks on each shortened URL.
- **Stats Page**: View click statistics (IP address, user agent) for each shortened URL.
- **Caching**: Use Redis to cache shortened URLs for faster redirection.
- **URL Validation**: Ensure only valid URLs are shortened.

## Screenshots

Below are some screenshots of the URL Shortener in action.

### Homepage

\
*The homepage where users can enter a URL to shorten.*

### Shortened URL

\
*The result after shortening a URL, showing the shortened link.*

### Stats Page

\
*The stats page showing click details for a shortened URL.*

## Prerequisites

To run this project, you need the following software installed:

- **Python 3.10+**
- **PostgreSQL 14+**
- **Redis 6+**
- **Docker** and **Docker Compose** (optional, for Docker setup)
- **Git** (to clone the repository)

## Installation

### Option 1: Local Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/petchimurugan-10/Url-Shortener.git
   cd Url-Shortener
   ```

2. **Set Up a Virtual Environment**:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up PostgreSQL**:

   - Install PostgreSQL:

     ```bash
     sudo apt install postgresql postgresql-contrib
     sudo systemctl start postgresql
     sudo systemctl enable postgresql
     ```
   - Create a user and database:

     ```bash
     sudo -u postgres psql
     ```

     ```sql
     CREATE USER myuser WITH PASSWORD 'password';
     CREATE DATABASE urlshortener;
     GRANT ALL PRIVILEGES ON DATABASE urlshortener TO myuser;
     \q
     ```
   - Configure `pg_hba.conf` to allow password authentication:

     ```bash
     sudo nano /etc/postgresql/14/main/pg_hba.conf
     ```

     Change the line for `localhost` to:

     ```
     host    all             all             127.0.0.1/32            md5
     ```

     Reload PostgreSQL:

     ```bash
     sudo systemctl reload postgresql
     ```

5. **Set Up Redis**:

   - Install Redis:

     ```bash
     sudo apt install redis-server
     sudo systemctl start redis
     sudo systemctl enable redis
     ```
   - Verify Redis is running:

     ```bash
     redis-cli ping
     ```

     Should return `PONG`.

6. **Configure Environment Variables**: Create a `.env` file in the project root:

   ```bash
   nano .env
   ```

   Add:

   ```
   FLASK_ENV=development
   SECRET_KEY=your-secret-key
   DATABASE_URL=postgresql://myuser:password@localhost:5432/urlshortener
   REDIS_URL=redis://localhost:6379/0
   ```

   Replace `your-secret-key` with a secure key (e.g., generate with `python -c "import secrets; print(secrets.token_hex(16))"`).

7. **Run the Application**:

   ```bash
   python run.py
   ```

   The app will be available at `http://localhost:5000`.

### Option 2: Docker Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/petchimurugan-10/Url-Shortener.git
   cd Url-Shortener
   ```

2. **Create a** `.env` **File**:

   ```bash
   nano .env
   ```

   Add:

   ```
   FLASK_ENV=development
   SECRET_KEY=your-secret-key
   DATABASE_URL=postgresql://myuser:password@postgres:5432/urlshortener
   REDIS_URL=redis://redis:6379/0
   ```

3. **Run with Docker Compose**:

   ```bash
   docker-compose up --build
   ```

   The app will be available at `http://localhost:5000`.

## Usage

1. **Shorten a URL**:

   - Go to `http://localhost:5000`.
   - Enter a URL (e.g., `https://example.com`) and submit.
   - You’ll receive a shortened URL (e.g., `http://localhost:5000/abc123`).

2. **Redirect**:

   - Visit the shortened URL (e.g., `http://localhost:5000/abc123`).
   - You’ll be redirected to the original URL.

3. **View Stats**:

   - Go to `http://localhost:5000/stats/abc123` to see click statistics for the shortened URL.

## Project Structure

```
Url-Shortener/
├── app/
│   ├── __init__.py      # Flask app setup
│   ├── models.py        # Database models (Urls, Clicks)
│   ├── routes.py        # Application routes
│   ├── static/          # Static files (CSS, JS)
│   └── templates/       # HTML templates
├── .env.example         # Example environment file
├── Dockerfile           # Docker configuration for the app
├── docker-compose.yml   # Docker Compose configuration
├── requirements.txt     # Python dependencies
└── run.py               # Entry point for the app
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
