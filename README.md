Instruction to Download the project .........
Step 1: Install Docker (if not installed), Visual Studio,python and Django \n  
Step 2: Clone the Django Project \n
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
![Screenshot 2025-03-19 064529](https://github.com/user-attachments/assets/f2da4916-e2c4-4188-a2dd-c8e413266d40)
![Screenshot 2025-03-19 064625](https://github.com/user-attachments/assets/ad6fdb83-d880-4338-aa7e-7b9659fdc8bb)
![Screenshot 2025-03-19 064405](https://github.com/user-attachments/assets/8c399f1f-2987-40b5-b0ff-34a3bc6b8884)
![Screenshot 2025-03-19 064939](https://github.com/user-attachments/assets/03cae350-150c-45c7-946c-b6c11d4f50a3)
![Screenshot 2025-03-19 065354](https://github.com/user-attachments/assets/4b047b85-0dd1-4433-acbc-f5a885c75c31)
![Screenshot 2025-03-19 065626](https://github.com/user-attachments/assets/0c5ab715-a77a-49ba-a6dd-aecc65611c1f)
