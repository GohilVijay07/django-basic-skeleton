<div align="center">

# 🚀 Django Learning Project 2026

### A Professional Django + PostgreSQL Starter Project

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-5.2.10-green?style=for-the-badge&logo=django)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

</div>

---

## 📖 About The Project

This is a professional Django learning project built using **Django 5.2.10** and **PostgreSQL**.  
It demonstrates backend setup, database integration, authentication system, and admin configuration.

Perfect for beginners who want to understand real-world Django project structure.

---

## ✨ Features

✔ Django 5.2.10 Setup  
✔ PostgreSQL Database Integration  
✔ Virtual Environment Configuration  
✔ Admin Panel Access  
✔ Database Migrations  
✔ Superuser Creation  
✔ Clean Project Structure  

---

# ⚙️ Installation & Setup Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/learning26.git
cd learning26
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate (Windows)

```bash
venv\Scripts\activate
```

### Activate (Mac/Linux)

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Setup PostgreSQL Database

Open PostgreSQL and run:

```sql
CREATE DATABASE learning26;
```

Update your `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'learning26',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 5️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 6️⃣ Create Admin User

```bash
python manage.py createsuperuser
```

---

## 7️⃣ Run Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

Admin panel:

```
http://127.0.0.1:8000/admin/
```

---

# 📂 Project Structure

```
learning26/
│
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── learning26/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│
└── your_app_name/
```

---

# 🔐 Security Best Practices

- Never upload `venv/`
- Never upload `.env`
- Keep SECRET_KEY private
- Keep database credentials secure

Add this to `.gitignore`:

```
venv/
__pycache__/
*.pyc
.env
```

---

# 🚀 Future Enhancements

- User Registration System
- Custom User Model
- REST API (Django REST Framework)
- Deployment on Cloud (Render / Railway / AWS)
- Docker Support

---

<div align="center">

## 👨‍💻 Author

### Vijay Gohil  
BCA Student | Django Learner  
Ahmedabad, India 🇮🇳  

---

⭐ If you like this project, don't forget to star it!

</div>
