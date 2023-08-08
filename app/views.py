from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from forms import *

from app import app, login_manager


@app.route('/', methods=['GET'])
def home():
    posts = Post.all()[::-1]
    return render_template("posts.html", posts=posts)


@app.route('/post/create', methods=['GET', 'POST'])
@login_required
def create_post():
    if not current_user:
        return redirect(url_for('login'))
    form = PostForm(request.form)
    if form.validate_on_submit():
        post = Post.create(user_id=current_user.id, title=form.title.data, text=form.text.data)
        return redirect(url_for("post", id=post.id))
    return render_template("post_form.html", form=form, post=None)


@app.route('/post/<id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    post = Post.find(id)
    if not post or post.user != current_user:
        return redirect(url_for("home"))
    form = PostForm(request.form, title=post.title, text=post.text)
    if form.validate_on_submit():
        post.update(title=form.title.data, text=form.text.data)
        return redirect(url_for("post", id=post.id))
    return render_template("post_form.html", form=form, post=post)


@app.route('/post/<id>/remove', methods=['GET', 'POST'])
@login_required
def remove_post(id):
    post = Post.find(id)
    if not post or post.user != current_user:
        return redirect(url_for("home"))
    form = BaseForm(request.form)
    if form.validate_on_submit():
        post.delete()
        return redirect(url_for("user", id=current_user.id))
    return render_template("post_remove.html", form=form, post=post)


@app.route('/post/<id>', methods=['GET'])
def post(id):
    post = Post.query.filter_by(id=id).first()
    return render_template("post.html", post=post)


@login_manager.user_loader
def load_user(user_id):
    return User.find(user_id)


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('login'))


@app.route('/login',  methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.where(username=form.username.data).first()
        login_user(user)
        return redirect(url_for('home'))
    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/user/create',  methods=['GET', 'POST'])
def create_user():
    if len(User.all()) > 0 and current_user.is_anonymous:
        return redirect('home')
    form = CreateUserForm(request.form)
    if form.validate_on_submit():
        user = User.create(username=form.username.data, password=User.generate_password_hash(form.password.data))
        login_user(user)
        return redirect(url_for('home'))
    return render_template("create_user.html", form=form)


@app.route('/user/<id>/edit', methods=['GET', 'POST'])
@login_required
def edit_user(id):
    user = User.where(id=id)
    if user is current_user:
        return render_template("user.html", user=user)
    if current_user:
        return redirect('edit_user', id=current_user.id)
    return redirect(url_for('home'))


@app.route('/user/<id>', methods=['GET'])
def user(id):
    user = User.where(id=id).first()
    if user:
        posts = user.posts[::-1]
        return render_template("user.html", user=user, posts=posts)
    return redirect(url_for('home'))
