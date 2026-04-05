Finance Dashboard Backend

Project Overview

This project is a backend system for a Finance Dashboard that allows users to manage financial records based on their roles. It provides APIs for handling transactions, applying role-based access control, and generating summary analytics for dashboard visualization.

The system is designed with clean architecture, proper validation, and scalable logic suitable for real-world applications.

---

Features

Role-Based Access Control

The system supports three roles:

- Admin
  
  - Full access to all records
  - Can create, update, delete records
  - Can view analytics for all users

- Analyst
  
  - Can view all records
  - Can access analytics
  - Cannot modify data

- Viewer
  
  - Can only view their own records
  - Can see their own analytics

---

Financial Records Management

Each financial record contains:

- Amount
- Type (Income / Expense)
- Category (Food, Rent, Salary, etc.)
- Date
- Description
- User (owner)

Supported operations:

- Create record
- Read records
- Update record
- Delete record

---

Filtering Support

Users can filter records using query parameters:

- By type:
  
  /api/records/?type=expense

- By category:
  
  /api/records/?category=food

- By date range:
  
  /api/records/?start_date=2026-04-01&end_date=2026-04-30

- Combined filters:
  
  /api/records/?type=expense&category=food

---

Dashboard Analytics

The backend provides summary data for dashboard:

- Total Income
- Total Expense
- Net Balance
- Category-wise expense breakdown

API:

GET /api/summary/

---

🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- SQLite

---

Setup Instructions

1. Clone the repository

git clone https://github.com/your-username/finance-dashboard-backend.git
cd finance-dashboard-backend

2. Create virtual environment

python -m venv venv
venv\Scripts\activate

3. Install dependencies

pip install django djangorestframework

4. Run migrations

python manage.py makemigrations
python manage.py migrate

5. Create superuser

python manage.py createsuperuser

6. Run server

python manage.py runserver

---

API Endpoints

Method| Endpoint| Description
GET| /api/records/| Get records
POST| /api/records/| Create record
PUT/PATCH| /api/records/{id}/| Update record
DELETE| /api/records/{id}/| Delete record
GET| /api/summary/| Dashboard analytics

---

Access Control Logic

- Admin & Analyst
  - Can view all records
- Viewer
  - Can only view their own records

This is enforced using:

- Custom permission class
- Queryset filtering in views

---

Validation & Error Handling

- Amount must be greater than 0
- Type must be either "income" or "expense"
- Category must match type
- Proper error responses for invalid input

---

Assumptions

- Categories are predefined based on type
- SQLite is used for simplicity
- Authentication is session-based
- No frontend included (API-only project)

---

Additional Notes

- Clean separation of concerns (models, views, serializers)
- Role-based logic implemented at backend level
- Designed for easy integration with frontend dashboards

---

Conclusion

This project demonstrates:

- Backend design
- Role-based authorization
- Data filtering & aggregation
- API development using Django REST Framework

---
