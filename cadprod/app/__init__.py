from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'eca1fb79fed5ad334412975c00d72d72'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.produtos import bp as produtos_bp
    app.register_blueprint(produtos_bp, url_prefix='/produtos')

    from app.usuarios import bp as usuarios_bp
    app.register_blueprint(usuarios_bp, url_prefix='/usuarios')


    with app.app_context():
        db.create_all()

    return app


