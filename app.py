from blog import Blog
# create a variable for the blog post template about how the blog post will appear
POST_TEMPLATE = """ 
    
    ======{}============
    
    {}
    
    
    
    """


# create a variable for the menu prom. Which will show the user to choose an option
MENU_PROMT = "Enter 'C' to create blog 'R' to read one 'L' to ' \
        'list blog 'Q' to quit 'P' to create post "
# blogs = dict {blog_title: 'title',content :'content'}
blogs = dict() # create a dictionary variable blogs with key value pair of blog_name: blog_object is the
# object of blog class which will call the method create_post(self, title, content):
# Create a function for menu

def menu():
    # which will show the user the available blog's
    # Let the user to make a choice
    # Do something with that choice
    # Eventually exit

    print_blog() # Now call the print blog function

    # create a variable selection which will show the available option for user
    selection = input(MENU_PROMT)
    while selection != 'Q': # if not Q , that means not quit
        if selection == 'C': # user will asked to create a blog
            ask_create_blog()
        elif selection == 'R': # user will asked to read a blog and will type a blog title
            ask_read_blog()
        elif selection == 'L': # user will asked to list the available blog post
            print_blog()
        elif selection == 'P': # user will asked to create a post
            ask_create_post()
        selection = input(MENU_PROMT) # it will appear below every option for another itarator



def ask_create_blog(): # function for create a blog

    blog_title = input('Enter your blog title') # blog_title will store the title
    author = input('Enter author name') # author will store the author name
    # dict  = {key:value} =  {blog_name = blogs[blog_title] : blog_object,which has an init method like = Blog(blog_title,author)}
    blogs[blog_title] = Blog(blog_title,author) # Blog will stored in our blogs dictionary


def ask_read_blog():
    title = input('Enter the blog title you want to read:')
    print_posts(blogs[title]) # will print the  value/content of blogs which key is matched with the title given by user


def ask_create_post():
    blog_title = input("Enter the blog title you want to post in:")
    title = input("Enter the blog title")
    content = input("Enter the blog content")
    blogs[blog_title].create_post(title,content) # Here we pass the two arguments
    # title , content that's why we don't need quotation here.

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title,post.content))



def print_blog():
    for key,blog in blogs.items(): # key:blog = blog_title:blog_post
        print('{}'.format(blog))
