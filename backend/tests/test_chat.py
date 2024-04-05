
def test_get_message(test_client):
    response = test_client.post('/register', data={
        'username': 'teststudent',
        'nickname': 'teststudent',
        'password': 'password123',
        'email': 'teststudent@example.com',
        'role': 'Student'
    })
    assert response.status_code == 201
    assert b"Account added successfully!" in response.data

    response = test_client.get('/getActivationToken', query_string={
        'username': 'teststudent'
    })
    assert response.status_code == 200
    token = response.get_json()['token']
    response = test_client.get('/activate', query_string={
        'token': token
    })
    assert response.status_code == 200

    response = test_client.post('/register', data={
        'username': 'testtutor',
        'nickname': 'testtutor',
        'password': 'password123',
        'email': 'testtutor@example.com',
        'role': 'Tutor'
    })
    assert response.status_code == 201
    assert b"Account added successfully!" in response.data

    response = test_client.get('/getActivationToken', query_string={
        'username': 'testtutor'
    })
    assert response.status_code == 200
    token = response.get_json()['token']
    response = test_client.get('/activate', query_string={
        'token': token
    })
    assert response.status_code == 200

    response = test_client.get('/get_message', query_string={
        'sender': 'teststudent',
        'receiver': 'testtutor'
    })
    assert response.status_code == 200

def test_send_message(test_client):
    response = test_client.post('/send_message', data={
        'sender': 'teststudent',
        'receiver': 'testtutor',
        'text': 'Hello!'
    })
    assert response.status_code == 200

    response = test_client.get('/get_message', query_string={
        'sender': 'teststudent',
        'receiver': 'testtutor'
    })
    assert response.status_code == 200
    assert b"Hello!" in response.data

    response = test_client.post('/send_message', data={
        'sender': 'teststudenttttt',
        'receiver': 'testtutor',
        'text': 'Hello!'
    })
    assert response.status_code == 400
    assert b"Sender not found" in response.data

    response = test_client.post('/send_message', data={
        'sender': 'teststudent',
        'receiver': 'testtutorrrrr',
        'text': 'Hello!'
    })
    assert response.status_code == 400
    assert b"Receiver not found" in response.data