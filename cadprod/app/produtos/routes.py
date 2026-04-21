from flask import request, render_template, redirect, url_for, flash
from app.produtos import bp
from app.models import Produto
from app import db

@bp.route('/')
def listar():
    produtos = Produto.query.all()  
    return render_template('produtos/listar.html', produtos=produtos)

@bp.route('/criar', methods=['GET', 'POST'])
def criar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        preco = request.form.get('preco')
        quantidade = request.form.get('quantidade', 0)
        
        if not nome or not preco:
            flash('Preencha nome e preço!', 'error')
            return render_template('produtos/criar.html')
        
        try:
            preco = float(preco)
            quantidade = int(quantidade)
            
            produto = Produto(
                nome=nome,
                preco=preco,
                quantidade=quantidade
            )
            
            db.session.add(produto)
            db.session.commit()
            
            flash(f'Produto "{nome}" criado com sucesso!', 'success')
            return redirect(url_for('produtos.listar'))
            
        except ValueError:
            flash('Preço ou quantidade inválidos!', 'error')
    
    return render_template('produtos/criar.html')

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    produto = Produto.query.get_or_404(id)
    
    if request.method == 'POST':
        produto.nome = request.form.get('nome')
        produto.preco = float(request.form.get('preco'))
        produto.quantidade = int(request.form.get('quantidade'))
        
        db.session.commit() 
        
        flash('Produto atualizado!', 'success')
        return redirect(url_for('produtos.listar'))
    
    return render_template('produtos/editar.html', produto=produto)

@bp.route('/deletar/<int:id>')
def deletar(id):
    produto = Produto.query.get_or_404(id)
    nome = produto.nome
    
    db.session.delete(produto)
    db.session.commit()
    
    flash(f'Produto "{nome}" removido!', 'success')
    return redirect(url_for('produtos.listar'))
