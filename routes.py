from app import app, db
 # redirect, url_for => redirect to where the inserted data is shown
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from models import Task
from datetime import datetime

import forms

# visiting localhost:5000 without specifying the routes
# will lead to 'Page not found' error


@app.route('/')  # decorator for the method defined in the line below
# it is possible to define multiple routes for the same mehtod
@app.route('/index')
def index():
    # return '<h1>Hello World!</h1>' # plain strings/elements

    # it is possible to pass data through 'render_template' to be used inside the HTML file
    # this is possible since Flask is using a template engine named 'jinja'
    # return render_template('index.html', current_title='Custom Title')

    # get all cretted tasks, and pass them to the render_template function
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

# flask routes by default expect GET requests
# allowing for POST requests is done by manually specifying


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():  # checks whether any data was entered
        # accesses data entered through the input field
        print('Submitted title', form.title.data)
        # enter the data taken from input field to database
        task = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(task)
        db.session.commit()
        flash('Task added!')
        return redirect(url_for('index')) # url_for takes in the function name as the parameter, not the actual url
    return render_template('add.html', form=form)


@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id): # task_id is extracted from the url
    task = Task.query.get(task_id)
    form = forms.AddTaskForm()
    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            # since the title is already added, the changes only have to be commited
            db.session.commit()
            flash('Task has been updated')
            return redirect(url_for('index'))
        form.title.data = task.title
        return render_template('edit.html', form=form, task_id=task_id)
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    task = Task.query.get(task_id)
    form = forms.deleteTaskForm()
    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash('Task has been removed')
            return redirect(url_for('index'))
        return render_template('delete.html', form=form, task_id=task_id, title=task.title)
    else:
        flash('Task not found')
    return redirect(url_for('index'))
