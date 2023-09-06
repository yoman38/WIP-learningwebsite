from flask import render_template, redirect, url_for, flash, abort, request
from flask_login import login_user, logout_user, login_required, current_user
from online_learning_platform import app, db, bcrypt
from online_learning_platform.models import User, Course, Content
from online_learning_platform.forms import RegistrationForm, LoginForm, CourseForm, ContentForm

@app.route("/")
@app.route("/home")
def home():
    courses = Course.query.all()
    return render_template('home.html', courses=courses)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/course/new", methods=['GET', 'POST'])
@login_required
def new_course():
    form = CourseForm()
    if form.validate_on_submit():
        course = Course(title=form.title.data, description=form.description.data, creator=current_user)
        db.session.add(course)
        db.session.commit()
        flash('Your course has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_course.html', title='New Course', form=form, legend='New Course')

@app.route("/course/<int:course_id>")
def course(course_id):
    course = Course.query.get_or_404(course_id)
    return render_template('course.html', title=course.title, course=course)

@app.route("/course/<int:course_id>/update", methods=['GET', 'POST'])
@login_required
def update_course(course_id):
    course = Course.query.get_or_404(course_id)
    if course.creator != current_user:
        abort(403)
    form = CourseForm()
    if form.validate_on_submit():
        course.title = form.title.data
        course.description = form.description.data
        db.session.commit()
        flash('Your course has been updated!', 'success')
        return redirect(url_for('course', course_id=course.id))
    elif request.method == 'GET':
        form.title.data = course.title
        form.description.data = course.description
    return render_template('create_course.html', title='Update Course', form=form, legend='Update Course')

@app.route("/course/<int:course_id>/delete", methods=['POST'])
@login_required
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    if course.creator != current_user:
        abort(403)
    db.session.delete(course)
    db.session.commit()
    flash('Your course has been deleted!', 'success')
    return redirect(url_for('home'))

@app.route("/course/<int:course_id>/content/new", methods=['GET', 'POST'])
@login_required
def new_content(course_id):
    course = Course.query.get_or_404(course_id)
    form = ContentForm()
    if form.validate_on_submit():
        content = Content(title=form.title.data, body=form.body.data, course=course)
        db.session.add(content)
        db.session.commit()
        flash('Your content has been created!', 'success')
        return redirect(url_for('course', course_id=course.id))
    return render_template('create_content.html', title='New Content', form=form, legend='New Content')

@app.route("/course/<int:course_id>/content/<int:content_id>/update", methods=['GET', 'POST'])
@login_required
def update_content(course_id, content_id):
    content = Content.query.get_or_404(content_id)
    if content.course.creator != current_user:
        abort(403)
    form = ContentForm()
    if form.validate_on_submit():
        content.title = form.title.data
        content.body = form.body.data
        db.session.commit()
        flash('Your content has been updated!', 'success')
        return redirect(url_for('course', course_id=course.id))
    elif request.method == 'GET':
        form.title.data = content.title
        form.body.data = content.body
    return render_template('create_content.html', title='Update Content', form=form, legend='Update Content')

@app.route("/course/<int:course_id>/content/<int:content_id>/delete", methods=['POST'])
@login_required
def delete_content(course_id, content_id):
    content = Content.query.get_or_404(content_id)
    if content.course.creator != current_user:
        abort(403)
    db.session.delete(content)
    db.session.commit()
    flash('Your content has been deleted!', 'success')
    return redirect(url_for('course', course_id=course.id))
