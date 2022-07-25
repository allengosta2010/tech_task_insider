import requests


def test_upload_image_success():
    data = {'dir': '/uploads/', 'submit': 'Submit'}
    files = {'file': ('file.txt', open('file.txt', 'r'))}
    response = requests.post("https://petstore.swagger.io/v2/pet/{petId}/uploadImage".format(petId=1),
                             files=files, data=data)
    assert response.status_code == 200


def test_upload_image_fail():
    data = {'dir': '/uploads/', 'submit': 'Submit'}
    files = {}
    response = requests.post("https://petstore.swagger.io/v2/pet/{petId}/uploadImage".format(petId=1),
                             files=files, data=data)
    assert response.status_code == 415


def test_add_new_pet_a_store_success():
    body = {
        "id": 10,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    response = requests.post("https://petstore.swagger.io/v2/pet", json=body)
    deserialized_response = response.json()
    assert response.status_code == 200
    assert deserialized_response['id'] == body['id']


def test_add_new_pet_a_store_fail():
    response = requests.post("https://petstore.swagger.io/v2/pet")
    print(response.text)
    assert response.status_code == 415
    # assert deserialized_response['id'] == error_body['id']


def test_change_pet_success():
    body = {
        "id": 10,
        "category": {
            "id": "0",
            "name": "string11"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    response = requests.put("https://petstore.swagger.io/v2/pet", json=body)
    deserialized_response = response.json()
    assert response.status_code == 200
    assert deserialized_response['id'] == body['id']


def test_change_pet_fail():
    response = requests.put("https://petstore.swagger.io/v2/pet")
    print(response.text)
    assert response.status_code == 415


def test_find_by_status_success():
    response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
    assert response.status_code == 200


def test_find_by_status_fail():
    response = requests.get("https://petstore.swagger.io/v2/pet/findByStatuss")
    print(response.text)
    assert response.status_code == 404


def test_get_pet_success():
    response = requests.get("https://petstore.swagger.io/v2/pet/{petId}".format(petId=1))
    assert response.status_code == 200


def test_get_pet_fail():
    response = requests.get("https://petstore.swagger.io/v2/pet/{petId}".format(petId=5555555555555555))
    assert response.status_code == 404


def test_update_pet_success():
    body = {
        "id": 10,
        "name": "apple_and_banana",
        "status": "sold"
    }
    response = requests.post("https://petstore.swagger.io/v2/pet", json=body)
    deserialized_response = response.json()
    assert response.status_code == 200
    assert deserialized_response['id'] == body['id']


def test_update_pet_fail():
    body = {
        "name": 55555555555,
        "status": 555555
    }
    response = requests.post("https://petstore.swagger.io/v2/pet/{petId}".format(petId=1), json=body)
    assert response.status_code == 415


def test_delete_pet_success():
    response = requests.delete("https://petstore.swagger.io/v2/pet/{petId}".format(petId=1))
    assert response.status_code == 200


def test_delete_pet_fail():
    response = requests.delete("https://petstore.swagger.io/v2/pet/{petId}".format(petId=15455335353535353))
    assert response.status_code == 404