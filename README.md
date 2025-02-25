# 💼 Job Portal Project

<div align="center" style="background-color:#0D1117; padding: 20px; border-radius: 10px;">

<img src="https://media.giphy.com/media/3o7TKPdUkkbxi3f3bW/giphy.gif" width="400" alt="Job Portal gif" />

</div>

## 📖 About the Project

This is a **Job Portal** built using **Django (Python)**, **HTML**, **CSS**, and **MySQL**. It enables employers to post job listings and job seekers to apply for jobs. The project includes user authentication and a fully responsive interface.

---

## 📋 Features

- ✔️ User authentication (Login & Registration)  
- ✔️ Employer job posting & management  
- ✔️ Job seeker profile creation & job application  
- ✔️ Admin dashboard for managing users & jobs  
- ✔️ Search & filter job listings  
- ✔️ Responsive design for all devices  
- ✔️ Secure password handling using Django's authentication system  

---

## 🖼️ Screenshots



### Job Listings
![Job Listings](./static/screenshots/Joblistings.png)

### Job Details Page
![Job Details Page](./static/screenshots/Jobdetail.png)

### Job Apply Page
![Employer Dashboard](./static/screenshots/jobapply.png)

### Admin Panel for Jobs
![Admin Panel](./static/screenshots/JobsAdmin.png)

### Admin Panel for JobApplications

![Admin Panel](./static/screenshots/JobapplicationAdmin.png)



### Login Page
![Login Page](./static/screenshots/login.png)

### Registration Page
![Registration Page](./static/screenshots/registration.png)

---

## 🛠️ Tech Stack

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="Python logo" />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" height="40" alt="Django logo" />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" height="40" alt="HTML5 logo" />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" height="40" alt="CSS3 logo" />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" height="40" alt="MySQL logo" />
</div>

---

## 📂 Setup

To run this project locally, follow these steps:

```bash
# Clone the repository
git clone https://github.com/your-username/job-portal.git

# Navigate to the project directory
cd job-portal

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver

# Access the application at:
http://localhost:8000
```

---

## 📊 Database Schema

- **Users**: Stores user credentials and roles (Employer, Job Seeker, Admin)
- **Jobs**: Contains job details such as title, description, location, etc.
- **Applications**: Tracks job applications with user and job references
- **Profiles**: Stores additional user information (for job seekers)

---

## 📌 Future Enhancements

- Implement job recommendation system
- Add email notifications for applications
- Support for resume upload & parsing
- Enhanced search with AI-powered suggestions

---

## 🔗 Connect with Me

<div align="left">
  <a href="mailto:saivivekgundeti7881@gmail.com">
    <img src="https://img.shields.io/static/v1?message=Gmail&logo=gmail&label=&color=D14836&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="Gmail logo"  />
  </a>
  <a href="https://www.instagram.com/_im_vivek_._" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Instagram&logo=instagram&label=&color=E4405F&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="Instagram logo"  />
  </a>
</div>

