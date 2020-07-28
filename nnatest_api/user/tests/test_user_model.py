import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_create_user():
    assert get_user_model().objects.count() == 0
    user = get_user_model().objects.create_user(
        email="test@server.com", password="pass1234", name="foo"
    )
    assert get_user_model().objects.count() == 1
    assert not user.is_superuser
    assert user.name == "foo"
    assert user.email == "test@server.com"
    assert user.check_password("pass1234")


@pytest.mark.django_db
def test_new_user_email_normalized():
    user = get_user_model().objects.create_user(
        email="test@SERVER.com", password="pass1234", name="foo"
    )
    assert user.email == "test@server.com"


@pytest.mark.django_db
def test_create_invalid_user():
    with pytest.raises(ValueError):
        get_user_model().objects.create_user(None, "password")


@pytest.mark.django_db
def test_create_super_user():
    user = get_user_model().objects.create_superuser(
        "superuser@admin.com", "pass123"
    )
    assert user.is_staff
    assert user.is_superuser
