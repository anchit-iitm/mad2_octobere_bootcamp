from app import app_celery
from celery_context import appContext

@app_celery.task(base=appContext)
def add(a, b):
    import time
    time.sleep(5)
    return a+b

@app_celery.task(base=appContext)
def hello():
    print("hello_world")
    return "hello"

@app_celery.task(base=appContext)
def search_category(a):
    from models import Category
    cat = Category.query.filter_by(id=a).first()
    if cat:  
        print("name", cat.name, "desc", cat.description)
        return cat.id
    else:
        return "Not Found"
    
@app_celery.task(base=appContext)
def test_email():
    from models import User
    all_users = User.query.all()
    for user in all_users:
        if not user.roles[0].name == 'admin':
            print(user.email)
            from flask_mail import Message
            email_reciver = user.email
            email_subject = 'Test Email'
            email_body = f'we are trying to send an email, {user.email}'
            email_html = '<html><body>'
            email_html += f'<h1>hi, {user.email}</h1>'
            email_html += '<p>this is a test email</p>'
            email_html += '<a href="https://google.com"><button>redirect</button></a>'
            email_html += '</body></html>'

            var1 = Message(subject=email_subject, recipients=[email_reciver], html=email_html)
            var1.body = email_body
            # var1.html = email_html
            from mailer import mailer
            mailer.send(var1)
    return 'Emails were out'