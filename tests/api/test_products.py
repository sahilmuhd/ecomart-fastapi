from fastapi.testclient import TestClient
from app.main import app
from app.db.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate

client = TestClient(app)

def test_create_product():
    product_data = ProductCreate(name="Test Product", price=10.99, description="A test product", store_id=1)
    response = client.post("/api/v1/products/", json=product_data.dict())
    assert response.status_code == 201
    assert response.json()["name"] == product_data.name

def test_read_product():
    response = client.get("/api/v1/products/1")
    assert response.status_code == 200
    assert "name" in response.json()

def test_update_product():
    product_update_data = ProductUpdate(name="Updated Product", price=12.99)
    response = client.put("/api/v1/products/1", json=product_update_data.dict())
    assert response.status_code == 200
    assert response.json()["name"] == product_update_data.name

def test_delete_product():
    response = client.delete("/api/v1/products/1")
    assert response.status_code == 204
    response = client.get("/api/v1/products/1")
    assert response.status_code == 404