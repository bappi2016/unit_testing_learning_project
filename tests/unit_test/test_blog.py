from  unittest import TestCase
from blog import Blog
class TestBlog(TestCase):
    def test_blog(self):
        blog_object = Blog('test_title','test_author')
        self.assertEqual('test_title',blog_object.title)
        self.assertEqual('test_author',blog_object.author)
        self.assertListEqual([],blog_object.post)

    def test_repr(self):
        blog_object = Blog('test_title', 'test_author')
        blog_object2 = Blog('Life is sucks', 'Ajmal Hussain')

        # Here we didn't set any blog title or author name yet. but we will. Now with _repr_() method we will check the blog post title and
        # author name (the string representation of it) directly without assigning any arguments or variable.
        # This is called TDD. Think it before you make it.
        #self.assertEqual(blog_object.__repr__(),'Test title by Test Author (0 posts)') # In the second arguments we pass the string or anything what we will want to pass in the repr() method but at first we will put it here. That is how TDD works.
        self.assertEqual(blog_object.__repr__(), 'test_title by test_author (0 posts)')
        self.assertEqual(blog_object2.__repr__(), 'Life is sucks by Ajmal Hussain (0 posts)')

    def test_multiple_post_repr(self):
        blog_object = Blog('test_title', 'test_author')
        blog_object.posts = ['post']

        blog_object2 = Blog('test_title', 'test_author')
        blog_object2.posts = ['post1','post2']

        self.assertEqual(blog_object.__repr__(), 'test_title by test_author (1 post)')
        self.assertEqual(blog_object2.__repr__(), 'test_title by test_author (2 posts)')

    def test_create_post_in_blog(self):
        blog_object = Blog('test_post_title', 'test_post_author')
        blog_object.create_post('post_title','post_content')

        self.assertEqual(blog_object.posts[0].title,'post_title')
        self.assertEqual(blog_object.posts[0].content, 'post_content')