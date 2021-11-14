import re
from flask import (render_template, redirect,
                   url_for, request)
from models import db, Project, app
import datetime

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-project', methods=["GET", "POST"])
def add_project():
    if request.form:
        date = request.form["date"].split("-")
        day = int(request.form['day'])
        month = int(date[0])
        year = int(date[1])
        new_project = Project(title= request.form['title'], created = datetime.datetime(year, month, day),
                    description= request.form['description'], skills= request.form['skills'],
                    link= request.form['link'])
        # project_in_db = session.query(Project).filter(Project.name==row[0]).one_or_none()
        # if project_in_db == None:
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')


@app.route('/about')
def about():
    return render_template('about.html')





if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')