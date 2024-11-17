import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Import environment variables if `env.py` exists
if os.path.exists("env.py"):
    import env  # noqa

# Initialize Flask app
app = Flask(__name__)

# Configure app
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

# Import routes after app and db are set up to avoid circular imports
from taskmanager import routes  # noqa

# Create the database tables within an application context
with app.app_context():
    db.create_all()