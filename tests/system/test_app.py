from unittest import TestCase
from unittest.mock import patch
from blog import Blog
from post import Post
import app


class TestApp(TestCase):

    def setUp(self):
        self.blog = Blog('test_blog_title', 'test_author_name')
        app.blogs = {'test_blog_title': self.blog}  # declare a blogs dictionary that contain a single blog
        # we set app.blogs equal to a dictionary, which is a mapping of
        # name or title of the blog - test_blog_title  to blog object that we created here blog_object

    def test_print_blog(self):

        with patch('builtins.print',return_value = 'Q') as mocked_print:
            app.print_blog()
            mocked_print.assert_called_with('test_blog_title by test_author_name (0 posts)')

    def test_input_menu_promt(self):
        with patch('builtins.input',return_value = 'Q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMT)

    @patch('builtins.input',return_value = 'Q')
    def test_input_menu_with_patch_decorator(self,mocked_input):
        app.menu()
        mocked_input.assert_called_with(app.MENU_PROMT)

    def test_check_menu_call_print(self):
        with patch('app.print_blog') as mocked_print_blog_is_call:
            with patch('builtins.input',return_value= 'Q'):
                app.menu()
                mocked_print_blog_is_call.assert_called()

    @patch('builtins.input')
    def test_ask_create_blog(self,mocked_input):
        mocked_input.side_effect = ('Test','Test Author')
        app.ask_create_blog()
        self.assertIsNotNone(app.blogs.get('Test')) # Assert there is a blog with key 'Test'


    def test_ask_read_blog(self):
        # Now we have to create a blog post with Title and Author
        #blog = Blog('Test', 'Author')
        # Here we have to create a dictionary which key is 'Test-Blog' and value is the blog object
        app.blogs = {'Test': self.blog}
        with patch('builtins.input',return_value = 'Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(self.blog)

    def test_print_posts(self): # In this test we gonna check is in the print_posts function, the another print_post(post) is called or not

        # Now we have to create a blog post with Title and Author
        #blog = Blog('Test', 'Author')
        # Now create a blog post
        self.blog.create_post('Test Post','Test Content')
        # Here we have to create a dictionary which key is 'Test-Blog' and value is the blog object
        app.blogs = {'Test': self.blog}
        # And here we gonna check 'print_post(post) is called or not
        with patch('app.print_post') as mocked_print_post:
            app.print_posts(self.blog) # we have to call the print_posts(blog) function first, because print_post(post) is inside this function
            mocked_print_post.assert_called_with(self.blog.posts[0])

    def test_print_post(self):
        post: object = Post('Post Title','Post Content')
        expected_print = """ 
    
    ======Post Title============
    
    Post Content
    
    
    
    """
        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)





    # We are importing the patch decorator from unittest.mock.
    # It replaces the actual sum function (that's why we need it 'app.sum'as
    # the arguments of the @patch decorator function) with a mock function that
    # behaves exactly how we want. In this case, our mock function
    # always returns 9 (for assert purpose). During the lifetime of our test, the sum
    # function is replaced with its mock version.


    #When a function is decorated using @patch, a mock of the class,
    # method or function passed as the target to @patch is returned
    # and passed as an argument to the decorated function.

    @patch('builtins.input')
    def test_ask_create_post(self,mocked_input):
        #blog = Blog('Test','Author')
        app.blogs = {'Test':self.blog}
        mocked_input.side_effect = ('Test','Test Title','Test Content')
        app.ask_create_post()
        self.assertEqual(self.blog.posts[0].title,'Test Title')
        self.assertEqual(self.blog.posts[0].content, 'Test Content')

    @patch('builtins.input')
    def test_menu_calls_create_blog(self,input_mocked_menu):
        with patch('app.ask_create_blog') as mocked_ask_create_blog:
            #input_mocked_menu.side_effect = ('C','Test Create Blog','Test Author','Q')
            input_mocked_menu.side_effect = ('C', 'Q')
            app.menu()
        #self.assertIsNotNone(app.blogs['Test Create Blog'])
            mocked_ask_create_blog.assert_called()

    @patch('builtins.input')
    def test_menu_calls_read_blog(self, input_mocked_menu):
        with patch('app.ask_read_blog') as mocked_ask_read_blog:
            # input_mocked_menu.side_effect = ('C','Test Create Blog','Test Author','Q')
            input_mocked_menu.side_effect = ('R', 'Q')
            app.menu()
            # self.assertIsNotNone(app.blogs['Test Create Blog'])
            mocked_ask_read_blog.assert_called()

    @patch('builtins.input')
    def test_menu_calls_create_post(self, input_mocked_menu):
        with patch('app.ask_create_post') as mocked_ask_create_post:
            # input_mocked_menu.side_effect = ('C','Test Create Blog','Test Author','Q')
            input_mocked_menu.side_effect = ('P', 'Q')
            app.menu()
            # self.assertIsNotNone(app.blogs['Test Create Blog'])
            mocked_ask_create_post.assert_called()
