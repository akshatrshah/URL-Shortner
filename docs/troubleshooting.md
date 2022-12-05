### Get Started with Creating APIs in Django

-  If you are completely new to django,  start with building a basic app from django. [Refer](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)
- See how to add tests for your project [Refer](https://docs.djangoproject.com/en/4.1/topics/testing/)

# How to identify errors?

- First, read the stack trace for why the errors occurred.
- Run the automated tests to see which flows are affected by the error
- apply pdb debugger anywhere in the code to debug step by step an error. This significantly decreases the debugging time.
- if there are database errors, refer to settings.py as this has the database configuration. If running tests, make sure 
you use the settingtest.py as the setting file for tests.
- Make sure you apply the migrations first.