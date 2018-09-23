import unittest
from app import create_app
from app.models import db
from app.models.entry import Entry
from nose.tools import eq_


class TestEntry(unittest.TestCase):

    def setUp(self):
        self.app = create_app('config.TestConfig')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_add_entry(self):
        entry = Entry(title='hello', text='hi')
        db.session.add(entry)
        db.session.commit()

        # print(db.session.query(Entry).count())
        eq_(db.session.query(Entry).count(), 1)
