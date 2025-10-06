import pytest
import sys
import os

# Add the parent directory to the path so we can import the app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    """Test the hello endpoint returns the expected message."""
    response = client.get('/')
    assert response.status_code == 200  # nosec B101
    assert b'Hello, DevopsCardmarket Interview!' in response.data  # nosec B101

def test_hello_endpoint_with_custom_message(client):
    """Test the hello endpoint with custom environment variable."""
    import os
    original_message = os.environ.get('APP_MESSAGE')
    os.environ['APP_MESSAGE'] = 'Custom Test Message'
    
    # Recreate the app to pick up the new environment variable
    from app import app
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200  # nosec B101
        assert b'Custom Test Message' in response.data  # nosec B101
    
    # Restore original message
    if original_message:
        os.environ['APP_MESSAGE'] = original_message
    else:
        os.environ.pop('APP_MESSAGE', None)

def test_health_check(client):
    """Test that the application responds to health checks."""
    response = client.get('/health')
    assert response.status_code == 200  # nosec B101
    assert b'Application is healthy' in response.data  # nosec B101

def test_main_endpoint(client):
    """Test that the main endpoint works correctly."""
    response = client.get('/')
    assert response.status_code == 200  # nosec B101
    assert response.headers['Content-Type'] == 'text/html; charset=utf-8'  # nosec B101
