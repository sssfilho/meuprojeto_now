from app import app, db
from flask import render_template, url_for, flash, redirect, request, session
from app.forms import Contato, Cadastro
from app.models import ContatoModels, CadastroModel
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

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        user = CadastroModel.query.filter_by(email = email, senha = senha).first()
        
        if user and user.senha == senha:
            session['user_id'] = user.id
            flash('Seja bem vindo')
            time.sleep(3)
            return redirect(url_for('index'))
        else:
            flash('Senha ou email incorreto!')

    return render_template('login.html')
        
@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    print('Acessou a rota de cadastro')
    cadastro = Cadastro()
    if cadastro.validate_on_submit():
        try:
            nome = cadastro.nome.data
            sobrenome = cadastro.sobrenome.data
            email = cadastro.email.data
            senha = cadastro.senha.data
            novo_cadastro = CadastroModel(nome=nome, sobrenome=sobrenome, email=email, senha=senha)
            db.session.add(novo_cadastro)
            db.session.commit()
            flash('Seu cadastro foi realizado com sucesso!')
        except Exception as e:
            flash('Ocorreu um erro ao cadastrar! Entre em contato como suporte: adm@admin.com')
            print(str(e))
    return render_template('cadastro.html', titulo='Cadastro', cadastro=cadastro)

   

