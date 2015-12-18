## Updating Models, Migrations
1. Update models in `models.py`
2. `python manage.py makemigrations` to create migrations for those changes
3. `python manage.py sqlmigrate [model_name] [migration_id]` doesn't actually r un migration, prints out the SQL Django thinks is required for your migs
4. `python manage.py check` checks for any problems in project without making migs or touching db
5. `python manage.py migrate` to apply those changes to the db
