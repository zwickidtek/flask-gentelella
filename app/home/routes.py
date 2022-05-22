from app.home import blueprint
from flask import render_template
from flask_login import login_required
from os import chdir, getcwd


@blueprint.route('/index')
@login_required
def index():
    todos = get_todos()
    return render_template('index.html', todo=todos)


@blueprint.route('/<template>')
@login_required
def route_template(template):
    return render_template(template + '.html')




def get_todos():
    path='/home/jared/.local/share/evolution/tasks/system'
    retval = getcwd()
    chdir(path)
    with open('tasks.ics') as f:
        contents = f.readlines()
    list_of_todos = []
    for i in range(len(contents)):
        line = contents[i].lower()
        if 'begin' in line and 'vtodo' in line:
            summary = contents[i+3]
            status = contents[i+7]
            if 'complete' in line or '100' in line:
                continue
            withoutSum = summary[8:]
            list_of_todos.append(withoutSum[:len(withoutSum)-1])
    return list_of_todos
    chdir(retval)

