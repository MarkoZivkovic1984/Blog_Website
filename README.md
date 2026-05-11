# Blog Backend Service (Flask)

A production-style backend web service built with Flask, PostgreSQL, and Docker.  
The application supports user authentication, content management, and RESTful APIs, and is deployed in a live environment.

## 🚀 Features
- User authentication (registration, login, session management)
- CRUD operations for blog posts
- Comment system with relational data handling
- REST API endpoints
- Rich text editing (CKEditor)
- Email integration (contact form)
- Deployed with PostgreSQL in production

## 🛠️ Tech Stack
- Python (Flask)
- PostgreSQL
- SQLAlchemy ORM
- Docker / Docker Compose
- Flask-Login / Flask-WTF
- CKEditor

## 🧱 Architecture
- `routes/` – API and view logic
- `models/` – database models
- `extensions.py` – app extensions setup
- `main.py` – application entry point

## 🌐 Deployment
The application is containerized and deployed using Docker with a PostgreSQL database on a cloud platform (Render).

Clone the repository:

git clone https://github.com/MarkoZivkovic1984/Blog_Website.git

Navigate to the project folder:

cd Blog_Website

Install dependencies:

pip install -r requirements.txt

Run the application:

python main.py

📌 Notes
Users must be logged in to leave comments
Admin-only functionality is implemented for managing posts
This project is built for learning and practice purposes
Users must be logged in to leave comments
Admin-only functionality is implemented for managing posts
This project is built for learning and practice purposes


Also it requires Valid Gmail app and valid Password for app from gmail.
