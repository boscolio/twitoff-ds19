"""Main app/routing file for TwitOff"""

from flask import Flask, render_template
from .models import DB, User, insert_example_users


def create_app():
    """Create and configure a Flask application"""

    app = Flask(__name__)
    app.config['SQLAlchemy_DATABASE_URI'] = "sqlite:///db.sqlite3"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    #TODO - make rest of application
    @app.route('/')
    def root():
        DB.drop_all() # deletes any present databases
        DB.create_all() # creates the database
        insert_example_users() # calls insert user function in models.py
        return render_template("base.html", title="Home", users=User.query.all())

    return app