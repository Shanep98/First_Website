import re
from flask import (render_template, redirect,
                   url_for, request)
from models import db, Project, app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-project', methods=["GET", "POST"])
def add_project():
    if request.form:
        new_project = Project(title= request.form['title'], created = request.form['created'],
                      description =request.form['description'], skills =request.form['skills'],
                      link= request.form['link'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')


@app.route('/about')
def about():
    return render_template('about.html')


# @app.route('/contact')
# def contact():
#     pass
#     return render_template('index.html#contact')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')