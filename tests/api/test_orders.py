from fastapi.testclient import TestClient
from app.main import app
from app.db.models.order import Order
from app.schemas.order import OrderCreate, OrderUpdate

client = TestClient(app)

def test_create_order():
    order_data = {
        "product_id": 1,
        "quantity": 2,
        "customer_id": 1
    }
    response = client.post("/api/v1/orders/", json=order_data)
    assert response.status_code == 201
    assert response.json()["product_id"] == order_data["product_id"]
    assert response.json()["quantity"] == order_data["quantity"]

def test_get_order():
    response = client.get("/api/v1/orders/1")
    assert response.status_code == 200
    assert "product_id" in response.json()

def test_update_order():
    order_update_data = {
        "quantity": 3
    }
    response = client.put("/api/v1/orders/1", json=order_update_data)
    assert response.status_code == 200
    assert response.json()["quantity"] == order_update_data["quantity"]

def test_delete_order():
    response = client.delete("/api/v1/orders/1")
    assert response.status_code == 204
    response = client.get("/api/v1/orders/1")
    assert response.status_code == 404