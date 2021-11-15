from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column('ID', db.Integer, primary_key=True)
    title = db.Column('Title', db.String())
    created = db.Column('Created', db.Date)
    description = db.Column('Description', db.String())
    skills = db.Column('Skills', db.String())
    link = db.Column('Link', db.String())
    
    
    def __repr__(self):
       return f'''Project id: {self.id}
                Project Title: {self.title}
                Created: {self.created}
                Description: {self.description}
                Skills: {self.skills}
                Link: {self.link}'''