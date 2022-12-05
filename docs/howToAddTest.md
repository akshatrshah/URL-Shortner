### Get Started with Creating APIs in Django

-  If you are completely new to django,  start with building a basic app from django. [Refer](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)
- See how to add tests for your project [Refer](https://docs.djangoproject.com/en/4.1/topics/testing/)

# How to add tests for this repo?

- in the folder shortner refer to tests folder. 
- file test_views tests the different view handler for the application
- file test_models tests different models by checking whether the database calls are working
- file test_urls test whether the right handlers are called for a view.

When you run the tests we define a seperate settings.py, in url_shortner_server folder which should be used while testing. It enables to create a in-memory database which is created and deleted after each run.

run :
python3 url_shortner_server/manage.py migrate --settings=url_shortner_server.settingtest 
then for running the tests:
python3 manage.py test shortner.tests.test-filename --settings=url_shortner_server.settingtest