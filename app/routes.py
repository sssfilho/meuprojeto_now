from app import app 
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html', tittle = 'Início')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', tittle = 'Sobre')

@app.route('/projeto')
def projeto():
    return render_template('projeto.html', tittle = 'projeto')

@app.route('/contato')
def contato():
    return render_template('contato.html', tittle = 'contato')

