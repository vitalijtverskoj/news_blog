import click
from werkzeug.security import generate_password_hash

from blog.extensions import db


@click.command('init-db')
def init_db():
    from wsgi import app

    # import models for creating tables
    from blog.models import User

    db.create_all()


@click.command('create-init-user')
def create_init_user():
    from blog.models import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(email='Admin@example.com',name='Admin' , password=generate_password_hash('test123'), is_staff=True)
        )
        db.session.add(
            User(email='Alice@example.com',name='Alice' , password=generate_password_hash('test123'), is_staff=False)
        )
        db.session.add(
            User(email='Jon@example.com',name='Jon' , password=generate_password_hash('test123'), is_staff=False)
        )
        db.session.add(
            User(email='Mike@example.com',name='Mike' , password=generate_password_hash('test123'), is_staff=False)
        )
        db.session.commit()
