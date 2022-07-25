import requests


def test_add_store_success():
    body = {
        "id": 0,
        "petId": 0,
        "quantity": 0,
        "shipDate": "2022-07-25T15:17:56.529Z",
        "status": "placed",
        "complete": 'true'
    }
    response = requests.post("https://petstore.swagger.io/v2/store/order", json=body)
    assert response.status_code == 200


def test_add_store_fail():
    body = {
        "id": 10,
        "petId": 53534334343434343434343,
        "quantity": 0,
        "shipDate": "2022-07-25T15:17:56.529Z",
        "status": "placed",
        "complete": 'true'
    }
    response = requests.post("https://petstore.swagger.io/v2/store/order", json=body)
    assert response.status_code == 500


def test_get_order_success():
    response = requests.get("https://petstore.swagger.io/v2/store/order/{orderId}".format(orderId=3))
    assert response.status_code == 200


def test_get_order_fail():
    response = requests.get("https://petstore.swagger.io/v2/store/order/{orderId}".format(orderId=153434343434343))
    assert response.status_code == 404


def test_delete_order_success():
    response = requests.delete("https://petstore.swagger.io/v2/store/order/{orderId}".format(orderId=3))
    assert response.status_code == 200


def test_delete_order_fail():
    response = requests.delete("https://petstore.swagger.io/v2/store/order/{orderId}".format(orderId=153434343434343))
    assert response.status_code == 404


def test_get_inventory_success():
    response = requests.get("https://petstore.swagger.io/v2/store/inventory")
    assert response.status_code == 200


def test_get_inventory_fail():
    response = requests.get("https://petstore.swagger.io/v2/store/inventoryy")
    assert response.status_code == 404
