import os
from django.test import TestCase  # noqa
from django.contrib.auth.models import User

from django.conf import settings
from unittest.mock import patch


class TestRegisterView(TestCase):
    @classmethod
    def setUp(cls):
        if(os.path.exists(os.path.join(settings.MEDIA_ROOT, "users", "random"))):
            os.rmdir(os.path.join(settings.MEDIA_ROOT, "users", "random"))
    
    def test_get_register_view(self):
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        response = self.client.post(
            "/register/",
            {
                "username": "random",
                "email": "testuser@example.com",
                "password1": "testpassword",
                "password2": "testpassword",
            },
        )
        self.assertEqual(response.status_code, 302)




class TestUserLoginView(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="random", email="testuser@example.com", password="randomuser"
        )
        
    @classmethod
    def tearDownClass(cls):
        media_dir = settings.MEDIA_ROOT
        username = cls.user.username
        os.rmdir(os.path.join(media_dir, 'users', username))

    def test_get_login_view(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)
        
    def test_user_directory(self):
        username = self.user.username
        media_dir = settings.MEDIA_ROOT
        user_dir = os.path.join(media_dir, 'users', username)
        self.assertTrue(os.path.isdir(user_dir)) # asserts user directory is created with each user
        self.assertEqual(len(os.listdir(user_dir)), 0) # asserts user directory is empty

    def test_login(self):
        username = self.user.username
        password = self.user.password
        response = self.client.post(
            "/login/", {"username": username, "password": password}
        )
        profile = self.user.profile.user_id
        self.assertEqual(profile, self.user.id) # asserts profile is created with each user
        self.assertEqual(response.status_code, 200)
        
    def test_logout(self):
        response = self.client.get("/logout/")
        self.assertEqual(response.status_code, 200)

