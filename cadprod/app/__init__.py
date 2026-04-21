from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'eca1fb79fed5ad334412975c00d72d72'

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.produtos import bp as produtos_bp
    app.register_blueprint(produtos_bp, url_prefix='/produtos')

    from app.usuarios import bp as usuarios_bp
    app.register_blueprint(usuarios_bp, url_prefix='/usuarios')

    return app


