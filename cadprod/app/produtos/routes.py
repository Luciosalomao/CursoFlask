from flask import render_template
from app.produtos import bp

@bp.route('/')
def listar():
    produtos = []

    return render_template('produtos/listar.html', produtos=produtos)

@bp.route('/criar')
def criar():
    return render_template('produtos/criar.html')