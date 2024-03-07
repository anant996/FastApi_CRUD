from fastapi.testclient import TestClient
from app.main import app
from app.utils.dummy_db import demo_db

client = TestClient(app)

def test_homepage():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to the homepage. Go to [Swagger UI](http://127.0.0.1:8000/docs) for testing."

def test_read_db():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == [{"1":{"id":1,"name":"Anant","email":"anant@gmail.com."},"2":{"id":2,"name":"Raj","email":"raj@yahoo.com"},"3":{"id":3,"name":"Anant","email":"anantt@gmail.com"}},200]

def test_create_db():
    id = 5
    name = "Vegeta"
    email = "vegeta@gmail.comm"
    response = client.post(f"/user?id={id}&name={name}&email={email}",)
    assert response.status_code == 200  
    assert response.json() == [{"message": "User created successfully","user": {"id": 5,"name": "Vegeta","email": "vegeta@gmail.comm"}},201]

def test_get_user_by_id():
    response = client.get("/user/3")
    assert response.status_code == 200
    assert response.json() == [{"id": 3,"name": "Anant","email": "anantt@gmail.com"},200]

def test_get_user_by_name():
    response = client.get("/users/Anant")
    assert response.status_code == 200
    assert response.json() == [[{"id": 1,"name": "Anant","email": "anant@gmail.com."},{"id": 3,"name": "Anant","email": "anantt@gmail.com"}],200]

def test_get_user_by_nameemail():
    name = "Anant"
    email = "anantt@gmail.com"
    response = client.get(f"/user?name={name}&email={email}")
    assert response.status_code == 200
    assert response.json() == [[{"id": 3,"name": "Anant","email": "anantt@gmail.com"}],200]

def test_update_db():
    id = 1
    name = "Rajender"
    email = "raj@gmail.com"
    response = client.put(f"/user/1?id={id}&name={name}&email={email}")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == [{"message": "User updated successfully","user": {"id": 1,"name": "Rajender","email": "raj@gmail.com"}},200]

def test_delete_from_db():
    response = client.delete("/user/1")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == [{'message': 'User deleted successfully'}, 200]
