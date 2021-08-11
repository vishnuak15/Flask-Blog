from flask import Blueprint
from flask import render_template, request
from flaskblog.models import Post


main = Blueprint('main',__name__)


@main.route("/")
@main.route("/home")
def index():
    page = request.args.get('page',1,type=int)
    post = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=3)
    # post = Post.query.all()
    return render_template('index.html', posts=post)


@main.route("/about")
def about():
    return render_template('about.html', title='About')

