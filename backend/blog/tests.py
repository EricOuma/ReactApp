from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Post, Category

class TestModelPost(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(username='test_user1', password='1q2w3e4r')
        test_post = Post.objects.create(category_id=1, author_id=1, title='Test Post', excerpt='Post Excerpt', content='Post Content', status='published')
    
    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        excerpt = f"{post.excerpt}"
        content = f"{post.content}"
        status = f"{post.status}"
        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'Test Post')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'Test Post')
        self.assertEqual(str(cat), 'django')

class PostTest(APITestCase):

    def test_view_posts(self):
        url = reverse('listcreate')
        # self.client.force_authenticate(user=None)
        res = self.client.get(url, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_create_post(self):
        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_user(username='test_user1', password='1q2w3e4r')
        data = {"author":1, "title":'Test Post', "excerpt":'Post Excerpt', "content":'Post Content', "status":'published'}
        url = reverse('listcreate')
        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
