from flask_testing import TestCase
from application import app, routes
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(WTF_CSRF_ENABLED=False, DEBUG=True, SECRET_KEY=getenv('MY_SECRET_KEY'), SQLALCHEMY_DATABASE_URI='mysql+pymysql://' + str(getenv('DB_USERNAME'))+ ':' + str(getenv('DB_PASSWORD')) + '@localhost:3306/test' )
        return app

class TestService(TestBase):
    def test_generate_rap_name(name):
        assert routes.generate_rap_name("a", "66") == 'Young Fork'
        assert routes.generate_rap_name("d", "76") == 'Yung Mustard'
        assert routes.generate_rap_name("g", "86") == 'Lil Gambino'
        assert routes.generate_rap_name("j", "96") == 'Big Chopper'
        assert routes.generate_rap_name("m", "106") == 'Sick Baby'
        assert routes.generate_rap_name("p", "116") == 'Ill Thumb'
        assert routes.generate_rap_name("v", "126") == 'DJ Poppa'
        assert routes.generate_rap_name("z", "1000") == 'D Dripper'
        assert routes.generate_rap_name("s", "36") == 'Wavy Wizard'
