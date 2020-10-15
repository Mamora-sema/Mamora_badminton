from flask import Flask, render_template, url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sweater import app, db
from sweater import News, Message, Article, Urgent

@app.route('/timetable')
def timetable():

    return render_template('timetable.html')


@app.route('/')
def index():

    news = News.query.order_by(News.date.desc()).all()
    return render_template('index.html', news=news)


@app.route('/news/<int:id>/del')
def news_delete(id):
    news = News.query.get_or_404(id)
    try:
        db.session.delete(news)
        db.session.commit()
        return redirect("/")

    except:
        return "При удалении статьи произошла ошибка"


@app.route('/news/<int:id>/update', methods=["POST", 'GET'])
def news_update(id):
    news = News.query.get(id)

    if request.method == "POST":
        news.title = request.form['title']
        news.intro = request.form['intro']
        news.text = request.form['text']


        try:
            db.session.commit()
            return redirect("/")
        except:
            return "При добавлении статьи произошла ошибка"

    else:

        return render_template("news_update.html", news=news)


@app.route('/news/<int:id>')
def news_detail(id):
    news = News.query.get(id)
    return render_template('news_detail.html', news=news)


@app.route('/urgent_create', methods=["POST", 'GET'])
def urgent_create():

    if request.method == "POST":

        text = request.form['text']
        urgent = Urgent(text=text)



        db.session.add(urgent)
        db.session.commit()
        return redirect("/urgent_create")


    else:
        return render_template('urgent_create.html')


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
        return "При удалении сообщения произошла ошибка"


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
            return "При обновлении статьи произошла ошибка"

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


@app.route('/create_news', methods=["POST", 'GET'])
def create_news():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        news = News(title=title, intro=intro, text=text)

        try:
            db.session.add(news)
            db.session.commit()
            return redirect("/")
        except:
            return "При добавлении статьи произошла ошибка"

    else:
        return render_template("create_news.html")


@app.route('/news_selection')
def news_selection():
    return render_template("news_selection.html")


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
        return render_template('message.html', message=message)