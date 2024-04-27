from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    short_content = db.Column(db.String(5), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    photo_url= db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()




@app.route('/')
def home():
    posts = Post.query.all()
    return  render_template('index.html', posts=posts)

@app.route('/portfolio')
def test():
    
    return render_template('portfolio.html')

@app.route('/<title>', methods=('GET', 'POST'))
def project(title):
    print(title)
    post = Post.query.filter_by(title=title).first()
    return render_template('portfolio.html', post=post)

if __name__ == '__main__':
    app.run()