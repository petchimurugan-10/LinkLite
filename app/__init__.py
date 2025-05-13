from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import redis
import click

db = SQLAlchemy()
redis_client = None

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    global redis_client
    redis_client = redis.Redis.from_url(os.getenv('REDIS_URL'), decode_responses=True)
    from .routes import main_bp
    app.register_blueprint(main_bp)

    # Register CLI command
    @app.cli.command("init-db")
    @click.echo
    def init_db_command():
        db.create_all()
        click.echo("Initialized the database.")

    return app