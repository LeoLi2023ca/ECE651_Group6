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
    

def test_register_tutor(test_client):
    """Test tutor registration."""
    response = test_client.post('/register', data={
        'username': 'testtutor',
        'nickname': 'testtutor',
        'password': 'password123',
        'email': 'testtutor@example.com',
        'role': 'Tutor'
    })
    assert response.status_code == 201
    assert b"Account added successfully!" in response.data

def test_register_duplicate_user(test_client):
    """Test duplicate user registration."""
    response = test_client.post('/register', data={
        'username': 'teststudent',
        'nickname': 'teststudent',
        'password': 'password123',
        'email': 'teststudent@example.com',
        'role': 'Student'
    })
    assert response.status_code == 409
    assert b"Username or email already exists." in response.data

def test_register_wrong_email(test_client):
    """Test wrong email registration."""
    response = test_client.post('/register', data={
        'username': 'teststudent2',
        'nickname': 'teststudent2',
        'password': 'password123',
        'email': 'teststudent2example.com',
        'role': 'Student'
    })
    assert response.status_code == 400
    assert b"Invalid email format" in response.data

def test_login_invalid(test_client):
    """Test invalid login."""
    response = test_client.post('/login', data={
        'username': 'teststudent',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert b"Invalid username or password." in response.data

def test_login(test_client):
    """Test login."""
    response = test_client.post('/login', data={
        'username': 'teststudent',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert b"Login successful!" in response.data

def test_getStudentProfileByUsername(test_client):
    """Test get student profile by username."""
    response = test_client.get('/getStudentProfileByUsername')
    
    assert response.status_code == 200