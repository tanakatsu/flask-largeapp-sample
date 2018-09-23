from app.models import db
from app.models.entry import Entry
from tests import BaseTestCase
from nose.tools import eq_


class TestEntry(BaseTestCase):

    def test_add_entry(self):
        entry = Entry(title='hello', text='hi')
        db.session.add(entry)
        db.session.commit()

        # print(db.session.query(Entry).count())
        eq_(db.session.query(Entry).count(), 1)
