# Clinic Partner Backend

Django REST API backend for Clinic Partner application with JWT authentication.

## Features

- Custom User authentication with email
- JWT token-based authentication
- PostgreSQL database
- RESTful API endpoints
- User registration and login
- Protected routes

## Tech Stack

- Python 3.10+
- Django 5.x
- Django REST Framework
- PostgreSQL
- JWT Authentication

## Setup Instructions

### Prerequisites

- Python 3.10 or higher
- PostgreSQL 15 or higher

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd clinic_backend
```

2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file in root directory:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=clinic_db
DB_USER=clinic_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

5. Create PostgreSQL database:
```sql
CREATE DATABASE clinic_db;
CREATE USER clinic_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE clinic_db TO clinic_user;
ALTER DATABASE clinic_db OWNER TO clinic_user;
```

6. Run migrations:
```bash
python manage.py migrate
```

7. Create superuser:
```bash
python manage.py createsuperuser
```

8. Run development server:
```bash
python manage.py runserver
```

## API Endpoints

### Authentication

- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login user
- `POST /api/auth/logout/` - Logout user
- `GET /api/auth/profile/` - Get user profile (protected)
- `POST /api/auth/token/refresh/` - Refresh access token

### Example Request

**Register:**
```json
POST /api/auth/register/
{
    "email": "doctor@clinic.com",
    "password": "SecurePass123!",
    "password2": "SecurePass123!",
    "first_name": "John",
    "last_name": "Doe",
    "phone": "1234567890",
    "user_type": "doctor"
}
```

**Login:**
```json
POST /api/auth/login/
{
    "email": "doctor@clinic.com",
    "password": "SecurePass123!"
}
```

## Project Structure
```
clinic_backend/
├── apps/
│   ├── accounts/      # User authentication
│   ├── appointments/  # Appointment management
│   ├── patients/      # Patient records
│   └── clinics/       # Clinic profiles
├── config/            # Django settings
├── venv/             # Virtual environment
├── .env              # Environment variables (not in git)
├── .gitignore        # Git ignore rules
├── manage.py         # Django management
└── requirements.txt  # Dependencies
```

## Development

- Admin panel: http://localhost:8000/admin/
- API root: http://localhost:8000/api/

Made by Chroma-labs Technologies Pvt. Ltd.
