from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    data_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/add")
def contact():
    return render_template("add.html")

@app.route("/addpost", methods = ['POST'])
def addpost():
    title  = request.form['title']
    subtitle  = request.form['subtitle']
    author  = request.form['author']
    content  = request.form['content']

    post = BlogPost(title=title, subtitle=subtitle, author=author, content=content)

    return "/"

if __name__ == '__main__':
    app.run(debug=True)