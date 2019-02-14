from post import Post
class Blog:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.posts = []
    # The __repr__ method simply tells Python how to print objects of a class
    # also __repr__ is used by the standalone Python interpreter to display a class in printable format.
    def __repr__(self): # will return string representation of the Blog class with binded by its attribute
        return '{} by {} ({} post{})'.format(self.title, self.author,len(self.posts),'s' if len(self.posts) != 1 else '') # This will help when we debugging our blog object

    def create_post(self, title, content): # here we create a post and put it in self.post list
        self.posts.append(Post(title,content))

    def json(self): # This method will return some string representation of the blog
        return {
            'title':self.title,
            'author':self.author,
            'posts': [post.json() for post in self.posts]


        }



