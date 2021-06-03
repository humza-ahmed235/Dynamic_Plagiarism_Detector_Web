from flask import Flask
from . import views
def create_app():
    app = Flask(__name__)



    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    app.register_blueprint(views.bp)
    app.add_url_rule('/', endpoint='index') #so that urlfor('index') also becomes correct just like urlfor('bpname.index') where index is the name for the view function
    return app