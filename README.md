#steps to run server
1) clone the repo
   ### git clone https://github.com/sreeneha1/team4-backend.git
2) change the Current Dir to Project Dir
   ### cd team4-backend
3) Creating the virtual environment
   ### python -m venv venv
4) Activating the virtual environment
   ### source venv/bin/activate
5) Installing dependencies
   ### pip install -r requirements.txt
6)Making migrations to database
   ### python manage.py makemigrations
   ### python manage.py migrate
7)running the server
   ### python manage.py runserver
