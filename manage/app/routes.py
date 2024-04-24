from flask import render_template, flash, redirect, url_for
from flask import request
from app import app
from app.forms import ForgotPasswordForm, LoginForm, RegistrationForm, TaskForm

# Define a list to store tasks
tasks = []

# Define a dummy user database
users = {'admin': 'password'}  # This is just for demonstration, use a real database in a real application


@app.route('/')
@app.route('/index')
@app.route('/index/<name>')
def index(name=None):
    first_name='Siri'
    return render_template('index.html', first_name=first_name, name=name)

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(users=users )
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        users[username] = password
        # for example, users['john'] = '12345' will add this user to the users dictionary
        #now the dictionary will be like {'admin': 'password', 'john': '12345'}
        print(users)
        flash('Registration successful! Please sign in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        print(username,password)
        if username in users and users[username] == password:
            # Check if the username exists and the password matches
            print(users)
            flash('Login successful!', 'success')
            return redirect(url_for('task_dashboard'))
        else:
            flash('Invalid username or password!', 'danger')
            return render_template('login.html', title='Sign In', form=form)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm()
    form1=LoginForm()
    if form.validate_on_submit():
        username=form1.username.data
        new_password = form.new_password.data
        confirm_new_password = form.confirm_new_password.data
        
        print("New Password:", new_password)
        print("Confirm Password:", confirm_new_password)
        if  new_password == confirm_new_password:
            # users[username] = new_password  # Update the password in the user database
            # form1.password.data=new_password
            # print("New Login password", form1.password.data)
            users[username]=new_password
            print("Updated Users:", users)  # Print the updated users dictionary
            flash('Your password has been changed successfully!', 'success')
            return redirect(url_for('login'))  # Redirect to login page after successful password reset
        else:
            # if username not in users:
            #     print("Username not found in users dictionary.")
            if new_password != confirm_new_password:
                print("New password and confirm password do not match.")
            flash('An error occurred. Please try again.', 'danger')
            # Here you can handle different error scenarios, like if username is not found or passwords don't match

    return render_template('forgot_password.html', title='Reset Password', form=form)


@app.route('/task_dashboard')
def task_dashboard():
    return render_template('task_dashboard.html', tasks=tasks)  # Pass tasks to the template

@app.route('/create_task', methods=['GET', 'POST'])
def create_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = {
            'title': form.title.data,
            'description': form.description.data,
            'assign_to': form.assign_to.data,
            'priority': form.priority.data,
            'duedate':form.duedate.data
        }
        tasks.append(task)  # Append the new task to the tasks list
        flash('Task created successfully!', 'success')
        return redirect(url_for('task_dashboard'))
    return render_template('create_task.html', title='Create Task', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500


