from flask_testing import TestCase
from application import app, routes
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(WTF_CSRF_ENABLED=False, DEBUG=True, SECRET_KEY=getenv('MY_SECRET_KEY'), SQLALCHEMY_DATABASE_URI='mysql+pymysql://' + str(getenv('DB_USERNAME'))+ ':' + str(getenv('DB_PASSWORD')) + '@localhost:3307/test' )
        return app

class TestService(TestBase):
    
    def test_generate_letter(name):
        assert routes.generate_letter("Smith") == 'g'                                                            
