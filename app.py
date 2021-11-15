import re
from flask import (render_template, redirect,
                   url_for, request)
from models import db, Project, app
import datetime

@app.route('/')
def index():
    projects= Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/add-project', methods=["GET", "POST"])
def add_project():
    if request.form:
        new_project = Project(title= request.form['title'], created =datetime.datetime.strptime(request.form['date'], '%Y-%m'),
                    description= request.form['desc'], skills= request.form['skills'],
                    link= request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')


#displays a non styled page and issues with creating ul for skills
@app.route('/detail/<id>')
def detail(id):
    project = Project.query.get_or_404(id)
    # projects = Project.query.all()
    return render_template('detail.html', project=project)


#need to create editproject.html for this to work
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    project = Project.query.get_or_404(id)
    if request.form:
        project.title = request.form['title']
        project.date = datetime.datetime.strptime(request.form['date'], '%Y-%m')
        project.description = request.form['desc']
        project.skills = request.form['skills']
        project.link = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editproject.html', project=project)


@app.route('/about')
def about():
    project = Project.query.all()
    return render_template('about.html', project=project)





if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')