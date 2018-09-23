from tests import BaseTestCase
from app.models import db
from app.models.entry import Entry
from nose.tools import eq_


class TestApi(BaseTestCase):

    def test_show_entries(self):
        entry = Entry(title='hello', text='hi')
        db.session.add(entry)
        db.session.commit()

        response = self.client.get('/')
        print(response.data)

        eq_(response.status_code, 200)
