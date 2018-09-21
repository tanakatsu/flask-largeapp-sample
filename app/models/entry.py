from app.models import db, Base


class Entry(Base):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)

    def __init__(self, title=None, text=None):
        super(Entry, self).__init__()
        self.title = title
        self.text = text

    def __repr__(self):
        return '<Entry id={id} title={title!r}>'.format(
            id=self.id, title=self.title)
