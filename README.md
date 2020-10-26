## Financepeer Assessment task

Django application with user authentication system and upload JSON file to database, displaying the data to the user

Steps to run:

1. git clone git@github.com:biradardd/financepeer.git

2. cd financepeer

3. virtualenv venv

4. venv\scripts\activate

5. pip install requirements.txt

6. provide your PostgreSQL credentials in 'financepeer/settings/dev.py' or for quick testing you can use SQLite3 which is commented in the same dev.py file

7. python manage.py migrate

8. python manage.py runserver 
