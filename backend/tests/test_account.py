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

    response = test_client.post('/register', data={
        'username': 'teststudent2',
        'nickname': 'teststudent2',
        'password': 'password123',
        'email': 'teststudent2@example.com',
        'role': 'Student'
    })
    assert response.status_code == 201
    assert b"Account added successfully!" in response.data

    response = test_client.post('/register', data={
        'username': 'teststudent3',
        'nickname': 'teststudent3',
        'password': 'password123',
        'email': 'teststudent3@example.com',
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
        'username': 'teststudent12',
        'nickname': 'teststudent12',
        'password': 'password123',
        'email': 'teststudent2example.com',
        'role': 'Student'
    })
    assert response.status_code == 400
    assert b"Invalid email format" in response.data

def test_validate_username(test_client):
    response = test_client.post('/validate_username', data={
        'username': 'teststudent12'
    })
    assert response.status_code == 201

def test_validate_email_wrong(test_client):
    response = test_client.post('/validate_email', data={
        'email': 'teststudent12'
    })
    assert response.status_code == 200
    assert b"Email Format is Wrong!" in response.data

def test_validate_email(test_client):
    response = test_client.post('/validate_email', data={
        'email': 'teststudent12@example.com'
    })
    assert response.status_code == 201
    assert b"ok" in response.data

def test_activate(test_client):
    response = test_client.get('/getActivationToken', query_string={
        'username': 'teststudent'
    })
    assert response.status_code == 200
    token = response.get_json()['token']
    response = test_client.get('/activate', query_string={
        'token': token
    })
    assert response.status_code == 200

    response = test_client.get('/getActivationToken', query_string={
        'username': 'teststudent'
    })
    assert response.status_code == 200
    token = response.get_json()['token']
    assert token == None

def test_activate_wrong(test_client):
    response = test_client.get('/activate', query_string={
        'token': None
    })
    assert response.status_code == 400
    response = test_client.get('/activate', query_string={
        'token': '1234567890'
    })
    assert response.status_code == 401

def test_login_wrong(test_client):
    """Test wrong login."""
    response = test_client.post('/login', data={
        'username': 'teststudentttt',
        'password': 'password1234'
    })
    assert response.status_code == 404
    assert b"User not found" in response.data

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

def test_get_student_profile_by_username(test_client):
    # Assuming there's a fixture or setup step that adds this student to the test database
    # Attempt to retrieve the student profile
    response = test_client.get('/getStudentProfileByUsername', data={'username': 'teststudent'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['user_info']['username'] == 'teststudent'
    assert data['user_info']['email'] == 'teststudent@example.com'

def test_get_student_profile_by_username_wrong(test_client):
    # Assuming there's a fixture or setup step that adds this student to the test database
    # Attempt to retrieve the student profile
    response = test_client.get('/getStudentProfileByUsername', data={'username': 'teststudenttt'})
    assert response.status_code == 401

def test_get_tutor_profile_by_username(test_client):
    # Assuming there's a fixture or setup step that adds this tutor to the test database
    # Attempt to retrieve the tutor profile
    response = test_client.get('/getTutorProfileByUsername', query_string={'username': 'testtutor'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['user_info']['username'] == 'testtutor'
    assert data['user_info']['nickname'] == 'testtutor'

def test_get_tutor_profile_by_username_wrong(test_client):
    # Assuming there's a fixture or setup step that adds this tutor to the test database
    # Attempt to retrieve the tutor profile
    response = test_client.get('/getTutorProfileByUsername', query_string={'username': 'testtutorrr'})
    assert response.status_code == 401

def test_update_student_profile(test_client):
    response = test_client.post('/updateStudentProfile', data={
        'username': 'teststudent',
        'nickname': 'newnickname',
        'email': 'newteststudent@example.com',
        'message': 'new message',
        'timezone': 'UTC -04:00'
    })
    assert response.status_code == 200
    assert b"profile updated" in response.data
    data = response.get_json()
    assert data['user_info']['nickname'] == 'newnickname'
    assert data['user_info']['email'] == 'newteststudent@example.com'
    assert data['user_info']['msg'] == 'new message'
    assert data['user_info']['timezone'] == 'UTC -04:00'
    assert data['user_info']['username'] == 'teststudent'

def test_update_student_profile_wrong(test_client):
    response = test_client.post('/updateStudentProfile', data={
        'username': 'teststudenttttt',
        'nickname': 'newnickname',
        'email': 'newteststudent@example.com',
        'message': 'new message',
        'timezone': 'UTC -04:00'
    })
    assert response.status_code == 401

def test_update_tutor_profile(test_client):
    response = test_client.post('/updateTutorProfile', data={
        'username': 'testtutor',
        'nickname': 'newnickname',
        'email': 'newtesttutor@example.com',
        'password': 'newpassword',
        'message': 'new message',
        'timezone': 'UTC -04:00',
        'subjects': json.dumps(['Math', 'Physics']),
        'salary': '20-30'
    })
    assert response.status_code == 200
    assert b"profile updated" in response.data
    data = response.get_json()
    assert data['user_info']['nickname'] == 'newnickname'
    assert data['user_info']['email'] == 'newtesttutor@example.com'
    assert data['user_info']['msg'] == 'new message'
    assert data['user_info']['timezone'] == 'UTC -04:00'
    assert data['user_info']['username'] == 'testtutor'
    # assert data['user_info']['subjects'] == ["Math", 'Physics']
    assert data['user_info']['salary'] == '20-30'
    response = test_client.post('/updateTutorProfile', data={
        'username': 'testtutorabcd',
        'nickname': 'newnickname',
        'email': 'newtesttutor@example.com',
        'password': 'newpassword',
        'message': 'new message',
        'timezone': 'UTC -04:00',
        'subjects': json.dumps(['Math', 'Physics']),
        'salary': '20-30'
    })
    assert response.status_code == 401
    

def test_update_password(test_client):
    response = test_client.post('/updatePassword', data={
        'username': 'teststudent',
        'old_pass': 'password123',
        'new_pass': 'newpassword'
    })
    assert response.status_code == 200
    assert b"Password updated successfully!" in response.data

def test_update_password_wrong_old(test_client):
    response = test_client.post('/updatePassword', data={
        'username': 'teststudent',
        'old_pass': 'wrongpassword',
        'new_pass': 'newpassword'
    })
    assert response.status_code == 411
    assert b"Incorrect Old Password" in response.data

def test_update_password_wrong_username(test_client):
    response = test_client.post('/updatePassword', data={
        'username': 'teststudentttt',
        'old_pass': 'password123',
        'new_pass': 'newpassword'
    })
    assert response.status_code == 404
    assert b"User not found" in response.data

def test_get_all_tutors(test_client):
    response = test_client.get('/getAllTutor')
    assert response.status_code == 200 
    data = response.get_json()
    assert len(data['list']) > 0

def test_student_request_matching(test_client):
    response = test_client.post('/studentRequestMatching', query_string={
        'student_username': 'teststudent',
        'tutor_username': 'testtutor',
    })
    assert response.status_code == 200
    assert b"Request sent successfully!" in response.data

    response = test_client.post('/studentRequestMatching', query_string={
        'student_username': 'teststudent2',
        'tutor_username': 'testtutor',
    })
    assert response.status_code == 200
    assert b"Request sent successfully!" in response.data

    response = test_client.post('/studentRequestMatching', query_string={
        'student_username': 'teststudent3',
        'tutor_username': 'testtutor',
    })
    assert response.status_code == 200
    assert b"Request sent successfully!" in response.data

def test_student_request_matching_wrong(test_client):
    response = test_client.post('/studentRequestMatching', query_string={
        'student_username': 'teststudentttt',
        'tutor_username': 'testtutor',
    })
    assert response.status_code == 404
    assert b"Student or Tutor not found" in response.data

def test_tutor_confirm_matching(test_client):
    response = test_client.post('/tutorConfirmMatching', query_string={
        'student_username': 'teststudent',
        'tutor_username': 'testtutor',
    })
    assert response.status_code == 200
    assert b"Request sent successfully!" in response.data

def test_tutor_confirm_matching_wrong(test_client):
    response = test_client.post('/tutorConfirmMatching', query_string={
        'student_username': 'teststudent',
        'tutor_username': 'testtutorrrr',
    })
    assert response.status_code == 404
    assert b"Student or Tutor not found" in response.data

def test_tutor_reject_matching(test_client):
    response = test_client.post('/tutorRejectMatching', query_string={
        'student_username': 'teststudent2',
        'tutor_username': 'testtutor',
    })
    assert response.status_code == 200
    assert b"Request sent successfully!" in response.data

def test_tutor_reject_matching_wrong(test_client):
    response = test_client.post('/tutorRejectMatching', query_string={
        'student_username': 'teststudent2222',
        'tutor_username': 'testtutor222',
    })
    assert response.status_code == 404
    assert b"Student or Tutor not found" in response.data

def test_student_cancel_matching(test_client):
    response = test_client.post('/studentCancelMatching', query_string={
        'student_username': 'teststudent3',
        'tutor_username': 'testtutor',
    })
    assert response.status_code == 200
    assert b"Request sent successfully!" in response.data

def test_student_cancel_matching_wrong(test_client):
    response = test_client.post('/studentCancelMatching', query_string={
        'student_username': 'teststudent333',
        'tutor_username': 'testtutor',
    })
    assert response.status_code == 404
    assert b"Student or Tutor not found" in response.data

def test_get_students_asked_tutors(test_client):
    response = test_client.get('/getStudentsAskedTutor', query_string={
        'student_username': 'teststudent3',
    })
    assert response.status_code == 200

def test_get_students_asked_tutors_wrong(test_client):
    response = test_client.get('/getStudentsAskedTutor', query_string={
        'student_username': 'teststudent333',
    })
    assert response.status_code == 404
    assert b"Student not found" in response.data

def test_get_students_matched_tutors(test_client):
    response = test_client.get('/getStudentMatchedTutor', query_string={
        'student_username': 'teststudent3',
    })
    assert response.status_code == 200

def test_get_students_matched_tutors_wrong(test_client):
    response = test_client.get('/getStudentMatchedTutor', query_string={
        'student_username': 'teststudent333',
    })
    assert response.status_code == 404
    assert b"Student not found" in response.data

def test_get_tutors_asked_students(test_client):
    response = test_client.get('/getTutorsAskedStudent', query_string={
        'tutor_username': 'testtutor',
    })
    assert response.status_code == 200

def test_get_tutors_asked_students_wrong(test_client):
    response = test_client.get('/getTutorsAskedStudent', query_string={
        'tutor_username': 'testtutorrrr',
    })
    assert response.status_code == 404
    assert b"Tutor not found" in response.data

def test_get_tutors_matched_students(test_client):
    response = test_client.get('/getTutorMatchedStudent', query_string={
        'tutor_username': 'testtutor',
    })
    assert response.status_code == 200

def test_get_tutors_matched_students_wrong(test_client):
    response = test_client.get('/getTutorMatchedStudent', query_string={
        'tutor_username': 'testtutorrrr',
    })
    assert response.status_code == 404
    assert b"Tutor not found" in response.data