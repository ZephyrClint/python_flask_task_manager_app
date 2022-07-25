from app import app
from flask import render_template

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
    return render_template('index.html', current_title='Custom Title')

# flask routes by default expect GET requests
# allowing for POST requests is done by manually specifying


@app.route('/about', methods=['GET', 'POST'])
def about():
    form = forms.AddTaskForm()
    if form.validate_on_submit():  # checks whether any data was entered
        # accesses data entered through the input field
        print('Submitted title', form.title.data)
        return render_template('about.html', form=form, title=form.title.data)
    return render_template('about.html', form=form)
