import click
from werkzeug.security import generate_password_hash

from blog.extensions import db


@click.command('create-admin')
def create_admin():
    from blog.models import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(email='Admin@example.com', first_name='Admin' , last_name='Admin', password=generate_password_hash('test123'), is_staff=True)
        )
        db.session.commit()


@click.command('create-init-tags')
def create_init_tags():
    from blog.models import Tag
    from wsgi import app

    with app.app_context():
        tags = ('flask', 'django', 'python', 'gb', 'sqlite')
        for item in tags:
            db.session.add(Tag(name=item))
        db.session.commit()
    click.echo(f'Created tags: {", ".join(tags)}')
