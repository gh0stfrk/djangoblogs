from django.test import TestCase
from users.models import User
from blog.models import Post


class TestCreatePost(TestCase):
    @classmethod
    def setUpTestData(cls):
        author = User.objects.create_user(username="random", password="randomuser")
        post = Post.objects.create(
            title="Test Post", content="Test Content", author=author
        )
        cls.post_id = post.id

    def test_view_detail_post(self):
        response = self.client.get(f"/detail/{self.post_id}/")
        self.assertEqual(response.status_code, 200)

    def test_create_post_from_view(self):
        self.client.login(username="random", password="randomuser")
        response = self.client.get(
            "/create-post/", data={"title": "Test Post", "content": "Test Content"}
        )
        self.assertEqual(response.status_code, 200)


class TestCreatePostView(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username="random", password="randomuser")

    def test_create_post_view(self):
        self.client.login(username="random", password="randomuser")
        response = self.client.get("/create-post/")
        self.assertEqual(response.status_code, 200)

    def test_create_post_view_not_logged_in(self):
        response = self.client.get("/create-post/")
        self.assertEqual(response.status_code, 302)

    def test_create_post_form_render(self):
        self.client.login(username="random", password="randomuser")
        response = self.client.get("/create-post/")
        text = response.content.decode()
        self.assertIn("Create Post", text)
        self.assertTemplateUsed(response, "blog/create_post.html")
