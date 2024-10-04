from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post


class PostModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            email="test@mail.com",
            username="test",
            password="test",
        )
        cls.post = Post.objects.create(
            title="My title",
            body="This is my content.",
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "My title")
        self.assertEqual(self.post.body, "This is my content.")
        self.assertEqual(self.post.author.email, "test@mail.com")
