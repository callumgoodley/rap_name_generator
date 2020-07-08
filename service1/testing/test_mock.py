from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(WTF_CSRF_ENABLED=False, DEBUG=True, SECRET_KEY=getenv('MY_SECRET_KEY'), SQLALCHEMY_DATABASE_URI='mysql+pymysql://' + str(getenv('DB_USERNAME'))+ ':' + str(getenv('DB_PASSWORD')) + '@localhost:3307/test' )        
        return app

class TestResponse(TestBase):
    def test_name(self):
        with patch('requests.post') as p:
            
            p.return_value.text = "99.75"

            response = self.client.post(url_for('home'), data=dict(first_name="John", last_name="Smith"), follow_redirects=True)
            
            self.assertIn(b"99.75", response.data)
