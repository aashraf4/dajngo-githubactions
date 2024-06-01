from django.test import TestCase
from .models import Post

# Create your tests here.
class ModelTesting(TestCase):
    def setUp(self):
        self.blog = Post.objects.create(title="Test1 title", author="Author test", slug="slug test")
        
    def test_post_model(self):
        blog = self.blog
        self.assertTrue(isinstance(blog, Post))
    
    def test_post_return(self):
        blog = self.blog
        self.assertEqual(str(blog), 'Test1 title')
        