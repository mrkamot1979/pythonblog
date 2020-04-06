from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password ='secret'
        )

        self.post = Post.objects.create (
            title = 'A good title',
            body = 'nice body content',
            author = user.self
        )

    def test_string_representation(self):
        post = Post(title = 'A sample title')

        self.assertEqual(str(post), post.title)