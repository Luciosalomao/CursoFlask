from flask import render_template
from app.usuarios import bp

@bp.route('/')
def listar():
    usuarios = []
    return render_template('usuarios/listar.html', usuarios=usuarios)

@bp.route('/criar')
def criar():
    return render_template('usuarios/criar.html')

