import os
from django.test import TestCase 
from django.contrib.auth.models import User

from django.conf import settings
from unittest.mock import patch


class TestRegisterView(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
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
        pass

    def test_get_login_view(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)
        

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
        

class TestAboutView(TestCase):
    def test_get_about_view(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)


class TestProfileView(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="random", email="testuser@example.com", password="randomuser"
        )
        
    def test_login_required(self):
        response = self.client.get("/profile/")
        self.assertEqual(response.status_code, 302)
        
    
    def test_get_profile_view(self):
        self.client.login(username="random", password="randomuser")
        response = self.client.get("/profile/")
        self.assertEqual(response.status_code, 200)