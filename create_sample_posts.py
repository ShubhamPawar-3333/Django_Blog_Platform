# create_sample_posts.py
import os
import django

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_platform.settings")

# Initialize Django
django.setup()

from blog_app.models import BlogPost
from django.contrib.auth.models import User

def create_sample_posts():
    # Assume 'admin' is the username of your superuser
    author = User.objects.get(username='admin')

    posts_data = [
        {"title": "The Rise of AI in 2025", "content": "Artificial Intelligence continues to transform industries in 2025, from healthcare to entertainment..."},
        {"title": "Top 10 Python Libraries for Data Science", "content": "Python's ecosystem offers powerful libraries like Pandas, NumPy, and TensorFlow for data analysis..."},
        {"title": "How Django Simplifies Web Development", "content": "Django's 'batteries-included' philosophy makes building web apps faster and more secure..."},
        {"title": "My Journey as a Python Developer", "content": "Starting as a beginner, I've learned Python's versatility through projects like this blog platform..."},
        {"title": "The Future of Remote Work", "content": "Remote work trends in 2025 show a shift towards hybrid models, with tools like Slack and Zoom..."},
        {"title": "Understanding Machine Learning Basics", "content": "Machine learning involves algorithms like regression and neural networks to predict outcomes..."},
        {"title": "Building Scalable APIs with Django REST", "content": "Django REST Framework simplifies creating RESTful APIs for mobile and web applications..."},
        {"title": "Why I Love Open-Source Software", "content": "Open-source projects like Django foster collaboration and innovation in the tech community..."},
        {"title": "Exploring Cloud Computing in 2025", "content": "Cloud platforms like AWS and Google Cloud dominate, offering scalability for startups and enterprises..."},
        {"title": "Tips for Writing Clean Python Code", "content": "Follow PEP 8 guidelines, use meaningful variable names, and write modular, reusable code..."},
        {"title": "The Impact of Blockchain on Finance", "content": "Blockchain technology is revolutionizing finance with secure, decentralized transactions..."},
        {"title": "Getting Started with Git and GitHub", "content": "Version control with Git and collaboration on GitHub are essential for modern developers..."},
        {"title": "A Day in the Life of a Software Engineer", "content": "From coding sprints to debugging, my day involves problem-solving and team collaboration..."},
        {"title": "The Best Practices for Database Design", "content": "Normalize your database, use indexes, and optimize queries for performance in Django apps..."},
        {"title": "How to Deploy a Django App to Heroku", "content": "Deploying Django to Heroku involves setting up a Procfile, requirements.txt, and environment variables..."},
        {"title": "The Role of Testing in Software Development", "content": "Unit tests, integration tests, and Django's testing framework ensure robust, bug-free code..."},
        {"title": "Exploring Web Scraping with Python", "content": "Use libraries like BeautifulSoup and Scrapy to extract data from websites for analysis..."},
        {"title": "The Growth of E-Commerce in 2025", "content": "E-commerce platforms are leveraging AI, mobile apps, and secure payments to drive sales..."},
        {"title": "Mastering Django ORM for Efficient Queries", "content": "Django's ORM simplifies complex database queries with Python syntax, improving productivity..."},
        {"title": "Why Community Matters in Tech", "content": "Tech communities on platforms like Stack Overflow and GitHub foster learning and innovation..."},
    ]

    for data in posts_data:
        BlogPost.objects.create(
            title=data["title"],
            content=data["content"],
            author=author
        )
    print("Sample blog posts created successfully!")

if __name__ == "__main__":
    create_sample_posts()