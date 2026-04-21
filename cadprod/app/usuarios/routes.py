from flask import render_template, request, redirect, url_for, flash
from app.usuarios import bp
from app.models import Usuario
from app import db

@bp.route('/')
def listar():
    usuarios = Usuario.query.all()
    return render_template('usuarios/listar.html', usuarios=usuarios)

@bp.route('/criar', methods=['GET', 'POST'])
def criar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        
        if not nome or not email:
            flash('Preencha todos os campos!', 'error')
            return render_template('usuarios/criar.html')
        
        existe = Usuario.query.filter_by(email=email).first()
        if existe:
            flash('Este email já está cadastrado!', 'error')
            return render_template('usuarios/criar.html')
        
        usuario = Usuario(nome=nome, email=email)
        db.session.add(usuario)
        db.session.commit()
        
        flash(f'Usuário {nome} criado!', 'success')
        return redirect(url_for('usuarios.listar'))
    
    return render_template('usuarios/criar.html')

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    usuario = Usuario.query.get_or_404(id)
    
    if request.method == 'POST':
        usuario.nome = request.form.get('nome')
        usuario.email = request.form.get('email')
        db.session.commit()
        
        flash('Usuário atualizado!', 'success')
        return redirect(url_for('usuarios.listar'))
    
    return render_template('usuarios/editar.html', usuario=usuario)

@bp.route('/deletar/<int:id>')
def deletar(id):
    usuario = Usuario.query.get_or_404(id)
    nome = usuario.nome
    
    db.session.delete(usuario)
    db.session.commit()
    
    flash(f'Usuário {nome} removido!', 'success')
    return redirect(url_for('usuarios.listar'))