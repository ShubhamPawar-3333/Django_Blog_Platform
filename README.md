# Blog Platform with Analytics

## Description
Welcome to the Blog Platform with Analytics, a modern web application built with Django, designed to create, manage, and analyze blog posts. This project is perfect for developers, students, or hobbyists looking to explore Django’s capabilities, build a content management system, and implement analytics features. It’s an ideal learning tool or portfolio piece for showcasing full-stack development skills.

## Features
- **User Authentication**: Secure login and logout functionality for managing blog posts and comments.
- **Blog Management**: Create, read, update, and comment on blog posts with a clean, user-friendly interface.
- **Analytics Dashboard**: Track post views, unique visitors, and popular content in real-time.
- **Responsive Design**: Styled with CSS for a professional, mobile-friendly experience.
- **Scalable Architecture**: Modular Django apps for blogs and analytics, ready for expansion.

## Installation
Follow these steps to set up the Blog Platform with Analytics locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ShubhamPawar-3333/Django_Blog_Platform.git
   cd Django_Blog_Platform
   ```

2. **Set Up a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    
    ```
4. **Apply Migrations:**
    ```bash
    python manage.py migrate

    ```

5. **Create a Superuser (for admin access):**
    ```bash
    python manage.py createsuperuser

    ```
    Follow the prompts to set a username, email, and password.

6. **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```
    Visit `http://127.0.0.1:8000/` in your browser to explore the platform.

## Usage
To use the Blog Platform with Analytics:

- Log in with your superuser credentials at `http://127.0.0.1:8000/accounts/login/`.
- Create blog posts at `http://127.0.0.1:8000/blogs/create/`.
- View posts and add comments at `http://127.0.0.1:8000/blogs/`.
- Check analytics at `http://127.0.0.1:8000/analytics/dashboard/` after viewing posts.

## Requirements
- Python 3.8+: Ensure Python is installed on your system.
- Django 5.1+: The project relies on Django for its framework (listed in `requirements.txt`).
- Git: Required for cloning the repository.