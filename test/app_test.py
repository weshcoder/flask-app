from flask import url_for

def tests_app(test_client):
    response = test_client.get(url_for('app.courses'), follow_redirects=True)
    assert response.status_code == 200
