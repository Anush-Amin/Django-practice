## Create a app which shows monthly challenges
1) Open the command prompt in system and go to the folder where project need to be created
2) Create the new django project using the command:
django-admin startproject monthly_challenges
-> monthly_challenges is project name which can be changed
3) Open the VS Code from monthly_challenges (outside one; inside there is one more monthly_challenges folder)
4) In django modules are called as apps
5) Create a new app using:
python manage.py startapp challenges
6) Now the structure of project looks like
MONTLY_CHALLENGES
  -> challenges
  -> monthly_challenges
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
14) Redirects: 
15) To make use of html files, create a templates folder inside the app folder (here app folder we have created is challenges) and inside this folder create the html file
16) In order to make this file to be used, go to settings.py file in the monthly_challenges folder. We can make the template be detected by adding "DIRS":[BASE_DIR / "challenges" / "templates"] inside TEMPLATES. This step is useful to detect a template which is used for all apps.
If we have to make the templates of all apps created to be detected then in settings.py file add the app name inside INSTALLED_APPS list. Make sure that "APP_DIRS": True in TEMPLATES
17) For creating the html file inside app folder it is kept in the folder templates>appname>html file. Here appname folder (should have name like if challenges is the app then templates>challenges>html file) is created to avoid confusion in detecting the html files with same name while rendering the template. Hence its the best practice to keep templates in this format
18) DTL: enhanced HTML files to create dynamic pages
Standard HTML syntax + Special DTL Syntax = Dynamic HTML page
* {{ variable }} : we can call the variable from python to html using curly braces
* filter: there are many built in filter which can be used
For example: {{variable|title}} if variable is "my FIRST post", the output will be "My First Post"
* tags: for tags is used for looping, url tag is used for constructing url
19) Template inheritance: Instead of writing the entire skeleton for all html files, we can create a html file which contains basic skeleton and this can be used by all other html files. Create this base.html file in templates folder. Use block tag where other files need to have dynamic changes. Use {% extends 'base.html' %} in the html files which uses base.html
Note: the path given here for base.html is absolute. To make django recognize this path, in monthly_challenges -> settings.py add BASE_DIR / "templates" in TEMPLATES list