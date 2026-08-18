from .utils import *
from ..routers.user import get_db, get_current_user
from ..models import Todos

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get("/user/")
    assert response.status_code == 200
    assert response.json()["username"] == "thomas_test"
    assert response.json()["email"] == "thomas@mail.com"
    assert response.json()["first_name"] == "Thomas"
    assert response.json()["last_name"] == "Fere"
    assert response.json()["role"] == "admin"
    assert response.json()["phone_number"] == "6946216731"


def test_change_password_success(test_user):
    response = client.put("/user/password", json={"password": "testpassword", "new_password": "newpassword"})

    assert response.status_code == 204


def test_change_password_invalid_current_password(test_user):
    response = client.put("/user/password", json={"password": "wrong_pass", "new_password": "newpassword"})

    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect password"}


def test_change_phone_number_success(test_user):
    response = client.put("/user/phonenumber/2222222")
    assert response.status_code == 204
