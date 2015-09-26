__author__ = '1'


def test_login(app):
    app.session.login("administrator","root")
    assert app.session.is_logged_in_as("administrator")
