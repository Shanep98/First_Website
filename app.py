import re
from flask import (render_template, redirect,
                   url_for, request)



@app.route('/')
def index():
    return render_template('index.html', pets=pets)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')