# Package Info
1. In __django/polls__ build with `python setup.py sdist`
2. This creates the directory __dist__ and builds the new package __django-polls-0.1.tar.gz__
3. To install the package: `pip install --user django-polls/dist/django-polls-0.1.tar.gz`
4. To uninstall: `pip uninstall django-polls`

## Updating Models, Migrations
1. Update models in `models.py`
2. `python manage.py makemigrations` to create migrations for those changes
3. `python manage.py sqlmigrate [model_name] [migration_id]` doesn't actually r un migration, prints out the SQL Django thinks is required for your migs
4. `python manage.py check` checks for any problems in project without making migs or touching db
5. `python manage.py migrate` to apply those changes to the db

## Layout
mysite/
- manage.py
- mysite/
	- __init__.py
	- settings.py
	- urls.py
	- wsgi.py
- polls/
	- __init__.py
	- admin.py
	- migrations/
		- __init__.py
		- 001_initial.py
		- models.py
		- static/
			- polls/
				- images/
					- background.gif
				- style.css
		- templates/
			- polls/
				- detail.html
					- index.html
					- results.html
		- tests.py
		- urls.py
		- views.py
	- templates/
		- admin/
			- base_site.html
			- index.html
