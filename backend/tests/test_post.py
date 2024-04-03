import json


def test_create_post(test_client):
    response = test_client.post('/register', data={
        'username': 'teststudent',
        'nickname': 'teststudent',
        'password': 'password123',
        'email': 'teststudent@example.com',
        'role': 'Student'
    })
    assert response.status_code == 201
    assert b"Account added successfully!" in response.data

    response = test_client.post('/create_post', data={
        'username': 'teststudent',
        'title': 'Test Post',
        'msg': 'This is a test post',
        'salary': '100',
        'subject': 'Math',
        'available_time': 'Monday 9:00 AM'
    })
    assert response.status_code == 200
    assert b"Post created successfully" in response.data

    response = test_client.get('/getAllOpeningPostsByUsername', query_string={
        'username': 'teststudent'
    })
    assert response.status_code == 200
    assert b"Test Post" in response.data
    assert b"This is a test post" in response.data
    assert b"100" in response.data
    assert b"Math" in response.data
    assert b"Monday 9:00 AM" in response.data
    assert b"opening" in response.data

def test_create_post_wrong(test_client):
    response = test_client.post('/create_post', data={
        'username': 'teststudentttttt',
        'title': 'Test Post',
        'msg': 'This is a test post',
        'salary': '100',
        'subject': 'Math',
        'available_time': 'Monday 9:00 AM'
    })
    assert response.status_code == 401

def test_getAllOpeningPostsByUsername(test_client):
    response = test_client.get('/getAllOpeningPostsByUsername', query_string={
        'username': 'teststudent'
    })
    assert response.status_code == 200

def test_getAllOpeningPostsByUsername_wrong(test_client):
    response = test_client.get('/getAllOpeningPostsByUsername', query_string={
        'username': 'teststudentttt'
    })
    assert response.status_code == 401

def test_getAllClosedPostsByUsername(test_client):
    response = test_client.get('/getAllClosedPostsByUsername', query_string={
        'username': 'teststudent'
    })
    assert response.status_code == 200

def test_getAllClosedPostsByUsername_wrong(test_client):
    response = test_client.get('/getAllClosedPostsByUsername', query_string={
        'username': 'teststudentttt'
    })
    assert response.status_code == 401

def test_update_post(test_client):
    response = test_client.post('/update_post', data={
        'post_id': '1',
        'status': 'closed'
    })
    assert response.status_code == 500

    response = test_client.post('/update_post', data={
        'post_id': '1',
        'username': 'teststudent',
        'title': 'Test Post',
        'msg': 'This is a test post',
        'salary': '100-110',
        'subject': 'Math',
        'available_time': 'Monday 9:00 AM',
        'timezone': 'UTC -04:00'
    })
    assert response.status_code == 200
    assert b"Post updated successfully" in response.data

    response = test_client.get('/getAllOpeningPostsByUsername', query_string={
        'username': 'teststudent'
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['list']) == 1

def test_inactivate_posts(test_client):
    response = test_client.post('/inactivate_posts', data={
        'post_id_list': json.dumps([1])
    })
    assert response.status_code == 200
    assert b"Posts inactivated successfully" in response.data

    response = test_client.get('/getAllOpeningPostsByUsername', query_string={
        'username': 'teststudent'
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['list']) == 0

    response = test_client.get('/getAllClosedPostsByUsername', query_string={
        'username': 'teststudent'
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['list']) == 1

def test_activate_posts(test_client):
    response = test_client.post('/activate_post', data={
        'post_id': 1
    })
    assert response.status_code == 200
    assert b"Posts activated successfully" in response.data

    response = test_client.get('/getAllOpeningPostsByUsername', query_string={
        'username': 'teststudent'
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['list']) == 1

    response = test_client.get('/getAllClosedPostsByUsername', query_string={
        'username': 'teststudent'
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['list']) == 0

def test_delete_posts(test_client):
    response = test_client.post('/delete_posts', data={
        'post_id_list': json.dumps([1])
    })
    assert response.status_code == 200
    assert b"Posts deleted successfully" in response.data

    response = test_client.get('/getAllOpeningPostsByUsername', query_string={
        'username': 'teststudent'
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['list']) == 0

    response = test_client.get('/getAllClosedPostsByUsername', query_string={
        'username': 'teststudent'
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['list']) == 0

def test_GetPostById(test_client):
    response = test_client.post('/create_post', data={
        'username': 'teststudent',
        'title': 'Test Post',
        'msg': 'This is a test post',
        'salary': '100-110',
        'subject': 'Math',
        'available_time': 'Monday 9:00 AM'
    })
    assert response.status_code == 200
    assert b"Post created successfully" in response.data

    # response = test_client.get('/getAllOpeningPostsByUsername', query_string={
    #     'username': 'teststudent'
    # })
    # assert response.status_code == 200
    # data = json.loads(response.data)
    # for post in data['list']:
    #     print(post['post_id'])

    response = test_client.get('/getPostByPostID', query_string={
        'post_id': 2
    })
    assert response.status_code == 200
    assert b"Test Post" in response.data
    assert b"This is a test post" in response.data
    assert b"100-110" in response.data
    assert b"Math" in response.data
    assert b"Monday 9:00 AM" in response.data
    assert b"opening" in response.data

def test_GetPostByPostID_wrong(test_client):
    response = test_client.get('/getPostByPostID', query_string={
        'post_id': 100
    })
    assert response.status_code == 401

def test_GetAllOpeningPost(test_client):
    response = test_client.get('/getAllOpeningPost')
    assert response.status_code == 200

def test_GetUserNameByPostID(test_client):
    response = test_client.get('/GetUserNameByPostID', query_string={
        'post_id': 2
    })
    assert response.status_code == 200
    assert b"teststudent" in response.data

def test_GetUserNameByPostID_wrong(test_client):
    response = test_client.get('/GetUserNameByPostID', query_string={
        'post_id': 100
    })
    assert response.status_code == 401