# URL Shortener
A simple and efficient URL shortening service built with Flask, PostgreSQL, and Redis. This project allows users to shorten long URLs, redirect using shortened URLs, and view click statistics for each shortened URL. It includes URL validation, caching with Redis, and click tracking.
Features

URL Shortening: Convert long URLs into short, shareable links.
Redirection: Redirect shortened URLs to their original links.
Click Tracking: Track the number of clicks on each shortened URL.
Stats Page: View click statistics (IP address, user agent) for each shortened URL.
Caching: Use Redis to cache shortened URLs for faster redirection.
URL Validation: Ensure only valid URLs are shortened.

## Screenshots
Below are some screenshots of the URL Shortener in action.
Homepage
The homepage where users can enter a URL to shorten.
Shortened URL
The result after shortening a URL, showing the shortened link.
Stats Page
The stats page showing click details for a shortened URL.
Prerequisites
To run this project, you need the following software installed:

Python 3.10+
PostgreSQL 14+
Redis 6+
Docker and Docker Compose (optional, for Docker setup)
Git (to clone the repository)

### Installation
#### Option 1: Local Setup

Clone the Repository:
git clone https://github.com/petchimurugan-10/Url-Shortener.git
cd Url-Shortener


#### Set Up a Virtual Environment:
python3 -m venv .venv
source .venv/bin/activate


#### Install Dependencies:
pip install -r requirements.txt


#### Set Up PostgreSQL:

Install PostgreSQL:sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql


Create a user and database:sudo -u postgres psql

CREATE USER myuser WITH PASSWORD 'password';
CREATE DATABASE urlshortener;
GRANT ALL PRIVILEGES ON DATABASE urlshortener TO myuser;
\q


Configure pg_hba.conf to allow password authentication:sudo nano /etc/postgresql/14/main/pg_hba.conf

Change the line for localhost to:host    all             all             127.0.0.1/32            md5

Reload PostgreSQL:sudo systemctl reload postgresql




#### Set Up Redis:

Install Redis:sudo apt install redis-server
sudo systemctl start redis
sudo systemctl enable redis


Verify Redis is running:redis-cli ping

Should return PONG.


#### Configure Environment Variables:Create a .env file in the project root:
nano .env

Add:
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://myuser:password@localhost:5432/urlshortener
REDIS_URL=redis://localhost:6379/0

Replace your-secret-key with a secure key (e.g., generate with python -c "import secrets; print(secrets.token_hex(16))").

Run the Application:
python run.py

The app will be available at http://localhost:5000.


### Option 2: Docker Setup

Clone the Repository:
git clone https://github.com/your-username/Url-Shortener.git
cd Url-Shortener


Create a .env File:
nano .env

Add:
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://myuser:password@postgres:5432/urlshortener
REDIS_URL=redis://redis:6379/0


Run with Docker Compose:
docker-compose up --build

The app will be available at http://localhost:5000.


Usage

## Shorten a URL:

Go to http://localhost:5000.
Enter a URL (e.g., https://example.com) and submit.
You’ll receive a shortened URL (e.g., http://localhost:5000/abc123).


## Redirect:

Visit the shortened URL (e.g., http://localhost:5000/abc123).
You’ll be redirected to the original URL.


## View Stats:

Go to http://localhost:5000/stats/abc123 to see click statistics for the shortened URL.



## Project Structure
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

## Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes and commit (git commit -m "Add your feature").
Push to your branch (git push origin feature/your-feature).
Open a Pull Request.

