Instruction to Download the project .........
Step 1: Install Docker (if not installed), Visual Studio,python and Django  
Step 2: Clone the Django Project
Step 3: Build and Run the Docker Container
docker build -t django_project .
OR if using docker-compose, run:
docker-compose up --build
Step 4: Run Migrations and Create a Superuser
docker exec -it django_app python manage.py migrate
docker exec -it django_app python manage.py createsuperuser
step 7: Access the Django Project for user registration page http://127.0.0.1:8000/api/users/register/
through this you will the ACCESS_TOKEN
set 8: open the postman 
select get
select the Bearer Token and paste the ACCESS_TOKEN
you will get the data Raw/Json formate
set 9: To Download in CSV 
http://127.0.0.1:8000/tasks/export/
