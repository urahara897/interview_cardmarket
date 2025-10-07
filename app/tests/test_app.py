import pytest
import sys
import os

# Make sure we can import our app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

@pytest.fixture
def client():
    """Set up a test client for our Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_main_page(client):
    """Check that the main page shows our message."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, DevopsCardmarket Interview!' in response.data

def test_custom_message(client):
    """Test that we can change the message with environment variables."""
    original_message = os.environ.get('APP_MESSAGE')
    os.environ['APP_MESSAGE'] = 'Hello, DevopsCardmarket Interview!'
    
    # Restart the app to pick up the new message
    from app import app
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b'Hello, DevopsCardmarket Interview!' in response.data
    
    # Put the original message back
    if original_message:
        os.environ['APP_MESSAGE'] = original_message
    else:
        os.environ.pop('APP_MESSAGE', None)

def test_health_check(client):
    """Make sure the health check endpoint works."""
    response = client.get('/health')
    assert response.status_code == 200
    assert b'Application is healthy' in response.data

def test_main_page_headers(client):
    """Check that the main page returns the right content type."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'text/html; charset=utf-8'
