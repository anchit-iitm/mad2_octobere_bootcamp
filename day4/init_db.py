from models import db, user_datastore
from app import create_app

app, _ = create_app()

with app.app_context():
    db.create_all()
    print("db created")
    user_datastore.find_or_create_role(name='admin')
    user_datastore.find_or_create_role(name='manager')
    user_datastore.find_or_create_role(name='customer')
    db.session.commit()

    if not user_datastore.find_user(email='a@abc.com'):
        admin_user = user_datastore.create_user(email='a@abc.com', password='a')
        # admin_user = user_datastore.create_user(email='a@abc.com', password='a', roles=['admin'])
        # role = user_datastore.find_role('admin')
        # user_datastore.add_role_to_user(admin_user, role)
        user_datastore.add_role_to_user(admin_user, 'admin')
        db.session.commit()