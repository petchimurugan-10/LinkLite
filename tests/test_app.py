# tests/test_app.py
import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_shorten_url(client):
    response = client.post('/', data={'url': 'https://example.com'})
    assert response.status_code == 302
    assert b'Short URL' in client.get('/').data