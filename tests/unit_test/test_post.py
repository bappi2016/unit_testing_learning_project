from unittest import TestCase
from post import Post
class PostTest(TestCase): # at first inherit the TestCase class from unittest module
    def test_create_post(self):
        # in every method inside a test class we will use  a test prefix to ensure that its a test method
        # NOw create a new post object, because we gonna need to test it
        post_object = Post('test_title','test_content')
        # NOw the TestCase API will use the self object to access its attribute and gonna check the matches property
        self.assertEqual('test_title',post_object.title)
        # assertEqual will take two argument, first test_title which is the actual title we are given to check or test which
        # will check is the title matches with Post title that is
        #post_object.title which is expected title.
        self.assertEqual('test_content',post_object.content)

    def test_json(self):
        post_object = Post('test_title', 'test_content')
        expected_data = {'title':'test_title',
                         'content':'test_content'}
        self.assertDictEqual(expected_data,post_object.json())
