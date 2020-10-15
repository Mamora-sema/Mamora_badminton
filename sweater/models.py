from sweater import db

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


class News(db.Model):

    __bind_key__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return '<News %r>' % self.Name


class Urgent(db.Model):

    __bind_key__ = 'urgent'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)



    def __repr__(self):
        return '<Urgent %r>' % self.Name
