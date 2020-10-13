from flask import Flask, render_template, url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_BINDS'] = {
    'message': 'sqlite:///message.db'
}
db = SQLAlchemy(app)







class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)



    def __repr__(self):
        return '<Article %r>' % self.id




class Message(db.Model):

    __bind_key__ = 'message'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Text, nullable=False)
    Surname = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return '<Message %r>' % self.Name



@app.route('/timetable')
def timetable():
    return render_template('timetable.html')


@app.route('/')
def index():

    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template('index.html', articles=articles)




@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template('posts.html', articles=articles)


@app.route('/posts/<int:id>')
def posts_detail(id):
    article = Article.query.get(id)
    return render_template('posts-detail.html', article=article)


@app.route('/posts/<int:id>/del')
def posts_delete(id):
    article = Article.query.get_or_404(id)
    try:
        db.session.delete(article)
        db.session.commit()
        return redirect("/posts")

    except:
        return "При удалении статьи произошла ошибка"

@app.route('/message/<int:id>/del')
def message_delete(id):

    message = Message.query.get_or_404(id)
    try:
        db.session.delete(message)
        db.session.commit()
        return redirect("/message")

    except:
        return "При удалении статьи произошла ошибка"


@app.route('/message/<int:id>/update', methods=["POST", 'GET'])
def message_update(id):
    message = Message.query.get(id)

    if request.method == "POST":
        message.Name = request.form['Name']
        message.Surname = request.form['Surname']
        message.text = request.form['text']


        try:
            db.session.commit()
            return redirect("/message")
        except:
            return "При добавлении статьи произошла ошибка"

    else:

        return render_template("message_update.html", message=message)


@app.route('/posts/<int:id>/update', methods=["POST", 'GET'])
def create_update(id):
    article = Article.query.get(id)

    if request.method == "POST":
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']


        try:
            db.session.commit()
            return redirect("/posts")
        except:
            return "При добавлении статьи произошла ошибка"

    else:

        return render_template("post_update.html", article=article)


@app.route('/create-article', methods=["POST", 'GET'])
def create_article():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect("/posts")
        except:
            return "При добавлении статьи произошла ошибка"

    else:
        return render_template("create-article.html")


@app.route('/message', methods=["POST", 'GET'])
def message():
    if request.method == "POST":
        Name = request.form['Name']
        Surname = request.form['Surname']
        text = request.form['text']
        message = Message(Name=Name, Surname=Surname, text=text)

        try:
            db.session.add(message)
            db.session.commit()
            return redirect("/message")
        except:
            return "При добавлении статьи произошла ошибка"

    else:

        message = Message.query.order_by(Message.date.desc()).all()
        return render_template('message.html', message = message)



if __name__ == "__main__":
    app.run(debug=True)