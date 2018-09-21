from app.models import db, Base

class User(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def __init__(self, name=None):
        super(User, self).__init__()
        self.name = name

    def __repr__(self):
        return '<User id={id} name={name!r}>'.format(
            id=self.id, name=self.name)
