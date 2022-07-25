import requests


def test_create_users_array_success():
    body = [
        {
            "id": 0,
            "username": "string",
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 0
        }
    ]
    response = requests.post("https://petstore.swagger.io/v2/user/createWithArray", json=body)
    assert response.status_code == 200


def test_create_users_array_fail():
    response = requests.post("https://petstore.swagger.io/v2/user/createWithArray")
    assert response.status_code == 415


def test_create_users_list_success():
    body = [
        {
            "id": 0,
            "username": "string",
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 0
        }
    ]
    response = requests.post("https://petstore.swagger.io/v2/user/createWithList", json=body)
    assert response.status_code == 200


def test_create_users_list_fail():
    response = requests.post("https://petstore.swagger.io/v2/user/createWithList")
    assert response.status_code == 415


def test_get_user_success():
    response = requests.get("https://petstore.swagger.io/v2/user/{username}".format(username="string"))
    assert response.status_code == 200


def test_get_user_fail():
    response = requests.get("https://petstore.swagger.io/v2/user/{username}".format(username="string323232"))
    assert response.status_code == 404


def test_put_user_success():
    body = {
        "id": 0,
        "username": "string",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }
    response = requests.put("https://petstore.swagger.io/v2/user/{username}".format(username="string"), json=body)
    assert response.status_code == 200


def test_put_user_fail():
    response = requests.put("https://petstore.swagger.io/v2/user/{username}".format(username="13433434"))
    assert response.status_code == 415


def test_delete_user_success():
    response = requests.delete("https://petstore.swagger.io/v2/user/{username}".format(username="string"))
    assert response.status_code == 200


def test_delete_user_fail():
    response = requests.delete("https://petstore.swagger.io/v2/user/{username}".format(username="13433434"))
    assert response.status_code == 404


def test_get_user_login_success():
    response = requests.get("https://petstore.swagger.io/v2/user/login?username=test&password=test")
    assert response.status_code == 200


def test_get_user_login_fail():
    response = requests.get("https://petstore.swagger.io/v2/user/loginn")
    assert response.status_code == 404


def test_get_user_logout_success():
    response = requests.get("https://petstore.swagger.io/v2/user/logout")
    assert response.status_code == 200


def test_get_user_logout_fail():
    response = requests.get("https://petstore.swagger.io/v2/user/logoutt")
    assert response.status_code == 404


def test_create_user_success():
    body = {
        "id": 0,
        "username": "string",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }
    response = requests.post("https://petstore.swagger.io/v2/user", json=body)
    assert response.status_code == 200


def test_create_user_fail():
    body = {
        "id": "sssss",
        "username": "string",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": "0"
    }
    response = requests.post("https://petstore.swagger.io/v2/user", json=body)
    assert response.status_code == 500