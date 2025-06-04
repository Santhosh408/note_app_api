Notes API - Django REST Framework
A simple Django REST API project for user registration and note management using JWT Authentication and a custom user model.

Features:

- User registration with custom user model
- JWT-based authentication (`SimpleJWT`)
- Notes: create, update, delete, list
- Auto timestamps for creation and update
- Permissions: Authenticated users only
- APIView-based views for better control

Setup Instructions:

1. Clone the repository:

git clone https://github.com/Santhosh408/note_app_api.git
cd note_project

2. Create a virtual environment:

python -m venv env
env\Scripts\activate


3. Install dependencies:

pip install -r requirements.txt


4. Run migrations:

python manage.py makemigrations

python manage.py migrate


5. Run the server:

python manage.py runserver
