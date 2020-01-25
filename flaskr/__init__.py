from flask import Flask
from . import views
def create_app():
    app = Flask(__name__)



    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    app.register_blueprint(views.bp)
    app.add_url_rule('/', endpoint='index')
    return app