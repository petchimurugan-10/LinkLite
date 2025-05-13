from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Urls, db
import string
import random
from . import redis_client
from .models import Clicks
from urllib.parse import urlparse
import re

main_bp = Blueprint('main', __name__)

# URL validation function
def is_valid_url(url):
    regex = re.compile(
        r'^(https?://)?'  # http:// or https://
        r'([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'  # domain
        r'(/.*)?$'  # optional path
    )
    return re.match(regex, url) is not None

# Function to generate a short code
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Index route with URL validation
@main_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form.get('url')
        if not original_url:
            flash('URL is required!', 'error')
            return redirect(url_for('main.index'))

        # Add URL validation before saving
        if not is_valid_url(original_url):
            flash('Invalid URL format!', 'error')
            return redirect(url_for('main.index'))

        # Check if URL already exists
        existing_url = Urls.query.filter_by(original_url=original_url).first()
        if existing_url:
            flash(f'Short URL: {request.host_url}{existing_url.short_code}', 'success')
            return redirect(url_for('main.index'))

        # Generate unique short code
        while True:
            short_code = generate_short_code()
            if not Urls.query.filter_by(short_code=short_code).first():
                break

        # Save to database
        new_url = Urls(original_url=original_url, short_code=short_code)
        db.session.add(new_url)
        db.session.commit()

        flash(f'Short URL: {request.host_url}{short_code}', 'success')
        return redirect(url_for('main.index'))

    return render_template('index.html')

# Click tracking function
def track_click(url_id, request):
    click = Clicks(
        url_id=url_id,
        ip_address=request.remote_addr,
        user_agent=request.headers.get('User-Agent')
    )
    db.session.add(click)
    db.session.commit()

# Redirect route
@main_bp.route('/<short_code>')
def redirect_url(short_code):
    # Check Redis cache
    cached_url = redis_client.get(f'url:{short_code}')
    if cached_url:
        url = Urls.query.filter_by(short_code=short_code).first()
        if url:
            # Track click
            track_click(url.id, request)
            return redirect(cached_url)

    # Query database if not in cache
    url = Urls.query.filter_by(short_code=short_code).first()
    if url:
        # Cache in Redis (e.g., expire after 1 hour)
        redis_client.setex(f'url:{short_code}', 3600, url.original_url)
        # Track click
        track_click(url.id, request)
        return redirect(url.original_url)
    else:
        flash('Invalid short URL!', 'error')
        return redirect(url_for('main.index'))

# Stats route
@main_bp.route('/stats/<short_code>')
def stats(short_code):
    url = Urls.query.filter_by(short_code=short_code).first()
    if not url:
        flash('Invalid short URL!', 'error')
        return redirect(url_for('main.index'))
    clicks = Clicks.query.filter_by(url_id=url.id).all()
    return render_template('stats.html', url=url, clicks=clicks)