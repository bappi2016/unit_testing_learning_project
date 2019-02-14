i am started to learn automation testing with python. This is my second project with udemy courses.

course link:



OK, there are couple of things to consider before any testing
1. does the thing we wanna test depends only on itself or does have any
external dependency.like a database or web api or etc.
Here our test dosen't depends on anything so we didn't need any external file import now
Now create a new python package inside  our the directory tests and  named it  unit_test for unit testing

One thing you have to know is , we use unit testing, when the there is no dependency in any method , functions or classes.
And thus we gonna put then in unit_test. OK now lets create a PostTest class to test the post class inside unit_test packages.

In unit test every test suit is a class.