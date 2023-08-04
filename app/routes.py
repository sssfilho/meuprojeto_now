from app import app 
from flask import render_template, url_for, flash, redirect, request
from app.forms import Contato
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
    if request.method == 'POST':
        flash('SEU FORMULARIO FOI ENVIADO COM SUCESSO !!!')
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        conteudo = request.form.get('conteudo')

        dados_formulario = {
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'conteudo': conteudo
        }
        
    return render_template('contato.html', title='Contato', formulario = formulario, dados_formulario = dados_formulario)
        
        
   

