import json

def test_register_student(test_client):
    """Test student registration."""
    response = test_client.post('/register', data={
        'username': 'teststudent',
        'nickname': 'teststudent',
        'password': 'password123',
        'email': 'teststudent@example.com',
        'role': 'Student'
    })
    assert response.status_code == 201
    assert b"Account added successfully!" in response.data

