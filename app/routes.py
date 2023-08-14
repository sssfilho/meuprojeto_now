from app import app, db
from flask import render_template, url_for, flash, redirect, request
from app.forms import Contato
from app.models import ContatoModels
import time 

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html', title = 'Início')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title = 'Sobre')

@app.route('/projeto', methods=['GET','POST'])
def projeto():
    return render_template('projeto.html', title='projeto')
    

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    dados_formulario = None
    formulario = Contato()
    if formulario.validate_on_submit():
        flash('SEU FORMULARIO FOI ENVIADO COM SUCESSO !!!')
        nome = formulario.nome.data
        email = formulario.email.data
        telefone = formulario.telefone.data
        conteudo = formulario.conteudo.data
        novo_contato = ContatoModels(nome=nome, email=email, telefone=telefone, conteudo=conteudo)
        db.session.add(novo_contato)
        db.session.commit()


        
    return render_template('contato.html', title='Contato', formulario = formulario, dados_formulario = dados_formulario)
        

@app.route('/teste')    
def teste():
    return render_template('teste.html')
        
   

