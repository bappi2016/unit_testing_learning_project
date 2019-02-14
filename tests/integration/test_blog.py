from  unittest import TestCase
from blog import Blog

from unittest.mock import patch
class TestBlog(TestCase):

    def test_create_post_in_blog(self):
        blog_object = Blog('test_post_title', 'test_post_author')
        blog_object.create_post('post_title','post_content')

        self.assertEqual(blog_object.posts[0].title,'post_title')
        self.assertEqual(blog_object.posts[0].content, 'post_content')
    def test_json(self):
        blog_object = Blog('test_title','test_author') # Given data to test
        blog_object.create_post('post_title', 'post_content')
        expected = {'title':'test_title',
                    'author':'test_author',
                    'posts':[{'title':'post_title',
                    'content':'post_content'}]}

        self.assertDictEqual(expected,blog_object.json())

    def test_json_no_post(self):
        blog_object = Blog('test_title', 'test_author')  # Given data to test

        expected = {'title': 'test_title',
                    'author': 'test_author',
                    'posts': []
                    }

        self.assertDictEqual(expected, blog_object.json())

