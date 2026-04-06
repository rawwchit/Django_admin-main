# Django Authentication System

A clean, modern, and secure Django-based authentication system featuring Email-based Login, Signup, and a sleek User Dashboard. This project uses a custom User model and is designed with a responsive, attractive UI.

## 🚀 Features

- **Email-based Authentication**: Users log in using their email address instead of a username.
- **Custom User Model**: Includes a `name` field and standard Django security features.
- **Modern UI/UX**: Responsive design with clean typography, soft shadows, and interactive feedback using Vanilla CSS.
- **Form Validation**: Real-time error handling (e.g., "Email does not exist, please signup").
- **Admin Dashboard**: Full control for administrators to view, block, or delete users.
- **Secure Logout**: CSRF-protected logout functionality.

## 🛠️ Tech Stack

- **Framework**: Django 6.0+
- **Database**: SQLite (Development) / Recommended: PostgreSQL (Production)
- **Frontend**: HTML5, Vanilla CSS3 (Modern UI)
- **Language**: Python 3.10+

---

## 💻 Installation & Setup

Follow these steps to get the project running on your local machine (Windows, macOS, or Linux).

### 1. Clone the Repository
```bash
git clone https://github.com/ShreeshonGit/Django_admin
cd Django_admin
```

### 2. Set Up a Virtual Environment (Recommended)
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations
This creates the necessary tables in the database.
```bash
python manage.py makemigrations accounts
python manage.py migrate
```

### 5. Create an Admin User (Superuser)
You will need this to access the admin panel and manage users.
```bash
python manage.py createsuperuser
```
*Follow the prompts to set your email, name, and password.*

### 6. Run the Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## 📂 Project Structure

- `accounts/`: Main application folder.
    - `models.py`: Custom User model definition.
    - `views.py`: Logic for Login, Signup, and Logout.
    - `templates/`: Modern HTML templates using a `base.html` layout.
- `my_project/`: Project configuration (settings, URLs).
- `requirements.txt`: List of Python dependencies.

---

## 🛡️ Admin Capabilities

Administrators can manage the entire user base by visiting:
`http://127.0.0.1:8000/admin/`

**From the Admin Panel, you can:**
- **View Users**: See a list of all registered users and their details.
- **Block Users**: Uncheck the `is_active` box to prevent a user from logging in.
- **Delete Users**: Permanently remove user records.
- **Permissions**: Grant other users "Staff" or "Superuser" status.

---

## 🗄️ Database Choice

While this project currently uses **SQLite** for ease of setup, **PostgreSQL** is highly recommended for production environments. 

**To switch to PostgreSQL:**
1. Install PostgreSQL on your system.
2. Install the adapter: `pip install psycopg2-binary`.
3. Update the `DATABASES` setting in `my_project/settings.py` with your PostgreSQL credentials.

---

## 📝 License
This project is open-source and available under the MIT License.