from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)

    def __repr__(self):
        return '<Entry id={id} title={title!r}>'.format(
            id=self.id, title=self.title)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def __repr__(self):
        return '<User id={id} name={name!r}>'.format(
            id=self.id, name=self.name)
