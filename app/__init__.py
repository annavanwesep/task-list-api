from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None, foo=None):
    app = Flask(__name__)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "DATABASE_URL")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get( 
            "SQLALCHEMY_TEST_DATABASE_URI")

    # Import models here for Alembic setup


    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.models.task import Task
    
    # Register Blueprints here
    from flask import Blueprint
    from .routes import tasks_bp, goals_bp
    from app.models.goal import Goal


    app.register_blueprint(tasks_bp)
    app.register_blueprint(goals_bp)
    
    
    return app
