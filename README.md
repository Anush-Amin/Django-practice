## Create a app which shows monthly challenges
1) Open the command prompt in system and go to the folder where project need to be created
2) Create the new django project using the command:
django-admin startproject monthly_challenges
> monthly_challenges is project name which can be changed
3) Open the VS Code from monthly_challenges (outside one; inside there is one more monthly_challenges folder)
4) In django modules are called as apps
5) Create a new app using:
python manage.py startapp challenges
6) Now the structure of project looks like
MONTLY_CHALLENGES
  > challenges
  > monthly_challenges
  manage.py
7) URLs: What are URLs?
* example.com/  --> Show starting (home) page
* example.com/posts --> Show list of all posts
* example.com/posts/python-is-great --> Shows a specific post
8) Views: What are Views?
* The logic that is executed for different URLs(and http methods)
* Can be class or function (every view is a standalone function or class)
* Code handles the requests and returns responses
10) To run the server:
python manage.py runserver
11) To start with the project, inside challenges > views.py write function:
def index(request):
    return HttpResponse("This works!")
12) Create a urls.py file inside challenges and add code there
13) Now add code to urls.py file in monthly_challenges folder