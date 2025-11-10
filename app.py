from flask import Flask, request, render_template

import sqlite3

def model_cadastrar_usuario(nome, email):
    with sqlite3.connect("clientes.db") as conn:
        sql_cadastrar_cliente = '''
        INSERT INTO clientes (nome, email)
        VALUES (?, ?);
    '''
        conn.execute(sql_cadastrar_cliente, (nome, email))

srv = Flask(__name__)

@srv.route("/")
def get_home():
    return render_template("form_cadastro.html")

@srv.route("/cadastrar",methods=['POST'])

def cadastrar_usuario():
    nome =  request.form["nome"]  # <input name='nome' ...>
    email = request.form["email"] # <input name='email' ...>
    model_cadastrar_usuario(nome, email)
    return "<h3>Cadastrado</h3>"

if __name__ == "__main__":
    srv.run(host="localhost",
            port=5000,
            debug=True)