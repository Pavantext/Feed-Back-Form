# Feed Back Form
 ### Project Description
The Django Feedback System is a web application designed to collect user feedback through a structured and interactive form. The project includes a dynamic feedback questionnaire, user-friendly input forms, and an administration interface for managing submitted data. This application was built using the Django framework and is deployed on PythonAnywhere.
you can visit the  [site here](https://pavantext6.pythonanywhere.com/) to test project

<p align="center">
<a href="https://codeclimate.com/github/pkini2002/Social-media-web-app/maintainability">
<img src="https://api.codeclimate.com/v1/badges/b79b9943a5cb4340c05f/maintainability" /></a>
<a href="https://codeclimate.com/github/pkini2002/Social-media-web-app/test_coverage">
<img src="https://api.codeclimate.com/v1/badges/b79b9943a5cb4340c05f/test_coverage" /></a>
</p>

<p align="center">
<a href="https://www.python.org/"><img src="https://forthebadge.com/images/badges/made-with-python.svg" border="0" title="Made with Python" />
</p>

<p align="center">
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif" border="0" alt="Powered by Django." title="Powered by Django." /></a>
</p>


<br>

### Technologies Used
#### Backend:
- Django (Python)
#### Frontend:
- HTML, CSS
#### Database:
- SQLite (default Django database) or any database configured in the settings.
#### Deployment:
- PythonAnywhere

### Features
#### Dynamic Feedback Questions:
- Includes various feedback categories such as ticket support, IT support, security, housekeeping, and more.
- Radio button choices for ease of input.
#### User-Friendly Form:
- Intuitive form layout with placeholders and validation for fields such as name, email, and mobile number.
- Textarea inputs for open-ended feedback and improvement suggestions.
#### Django Admin Interface:
- Manage and review all feedback submissions through Django's default admin panel.
#### Security:
- CSRF protection to secure the feedback form.
- Session-based token to prevent duplicate form submissions.
#### Responsive Design:
- Works seamlessly across devices, maintaining a consistent layout and experience.
### Installation and Setup
- Follow these steps to set up the project locally or deploy it on your own server:

1. Create a Virtual Environment for the Project

   - If u don't have a virtualenv installed

   ```bash
   pip install virtualenv
   ```
   **For Windows Users**
   ```bash
   virtualenv env
   env/Scripts/activate
   ```

   **For Linux Users**
   ```bash
   virtualenv env
   source env/bin/activate
   ```
    <br>
2. Install Django
```bash
pip install django
```
<br>

3. Fork the Repository:
Fork the [repo](https://github.com/Pavantext/Feed-Back-Form.git)
   - Clone the repo to your local system
     
   ```git
   git clone https://github.com/Pavantext/Feed-Back-Form.git
   cd feedback
   ```
   Make sure you have python installed on your system.

      <br>
4. Make migrations/ Create db.sqlite3

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   <br>
5. Create a super user.
   This is to access Admin panel and admin specific pages.

   ```djangotemplate
   python manage.py createsuperuser
   ```
   
   Enter your username, email and password.
      <br>
6. Run server
   ```bash
   python manage.py runserver
   ```
<br>

# Deployment on PythonAnywhere
1. configure the static  files & set DEBUT to False in the `settings.py` file:
   ```python
   STATIC_URL = '/static/'
   STATIC_ROOT = '/home/<your-username>/<your-project-name/static`
   DEBUG = False
   ```

2. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

# Screenshots
### Feedback Form:
![Screenshot (22)](https://github.com/user-attachments/assets/801f4340-b750-4c73-8512-358aa0edbb67)
<br<
![Screenshot (23)](https://github.com/user-attachments/assets/c9900e19-90fd-487a-9177-d210e4f1d119)
<br>
![Screenshot (24)](https://github.com/user-attachments/assets/49a14aaa-8f55-4660-a297-4ef9ad0cce5a)
<br>
### Thank You Page:
![Screenshot (21)](https://github.com/user-attachments/assets/83e490d9-c4c4-492e-96b2-d1d64a270836)

 #### Usage
1. Fill out the feedback form, including ratings for various categories and suggestions.
2. Submit the form to save the feedback.
3. Admin users can log in to the Django admin interface to review submissions.
   <br>
 #### Future Enhancements
- Add user authentication for personalized feedback forms.

- 
- Export feedback data to CSV or Excel.
- Implement analytics dashboards to visualize feedback trends.
