from app import create_app
from flask_login import LoginManager
from models import User
from flask import Blueprint, render_template, jsonify,request,send_file, Flask

app = create_app()

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.errorhandler(401)
def unauthorized(error):
    return render_template('unauthorized.html', title='Processamento')


if __name__ == "__main__":
    app.run(debug=True)

