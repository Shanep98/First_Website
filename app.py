import re
from flask import (Flask, render_template, redirect,
                   url_for, request)


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///pets.db'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')