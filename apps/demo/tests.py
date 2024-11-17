# tests.py

from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class PostListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(user=self.user, text='This is a test post')
        self.comment = Comment.objects.create(user=self.user, post=self.post, text='This is a comment')

    def test_get_posts(self):
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('posts', response.data)  # Check that 'posts' key is in the response
        self.assertEqual(len(response.data['results']), 1)  # Since we created 1 post in setup
