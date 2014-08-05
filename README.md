Pyramid + uwsgi + nginx
=======================

Over the past week, I've been trying to get pyramid running with uwsgi and nginx.  I found a few documents on the subject but felt that everything that I found was lacking in one area or another.
I am in no way an expert; rather, I'm pretty new to web related development.
I'm writing this to help the other beginners who may be confused and frustrated. 

I am open to suggestions and "what were you thinking?" comments.  As I said, I'm a beginner... 

Let's begin. 

1. Get yourself virtualenv 

`$ pip install virtualenv`

2. Install virtualenvwrapper

This a really cool tool that makes working with virtual envs really easy

`$ pip install virtualenvwrapper`

make a directory where your virtual envs will live

`$ mkdir -p <path/to/venvs>`

In your `.bashrc` enter the line
 
`export WORKON_HOME=<path/to/venvs>`

Don't forget to source your terminal with the new `.bashrc`

`$ source ~/.bashrc`

3. Let's make a virtual env that we'll use for our project

`$ mkvirtualenv <virtual env name>`

You should see at the beginning of your command prompt the name of the virtual env `(<venv name>)user@host:<some/path>$ ` 

4. Install some python modules that we're going to be using.  We're starting off with pyramid

`$ pip install pyramid`

5. Create an app, for this example we're going to use the simple default app that's created using pcreate.

`$ pcreate -s starter app`

Now we can get to service our app

6. Install uwsgi 

`$ pip install uwsgi`
