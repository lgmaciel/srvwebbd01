from flask import Flask, request, render_template

import sqlite3

def model_listar_clientes():
    with sqlite3.connect("clientes.db") as conn:
        sql_listar_clientes = '''
            SELECT id, nome, email FROM clientes;
            '''
        cur = conn.cursor()
        cur.execute(sql_listar_clientes)
        return cur.fetchall() # retorna uma lista de tuplas (id, nome, email)

def model_cadastrar_cliente(nome, email):
    with sqlite3.connect("clientes.db") as conn:
        sql_cadastrar_cliente = '''
        INSERT INTO clientes (nome, email)
        VALUES (?, ?);
    '''
        conn.execute(sql_cadastrar_cliente, (nome, email))

srv = Flask(__name__)

@srv.get("/cadastrar")
def get_form_cadastro():
    return render_template("form_cadastro.html")

@srv.post("/cadastrar")
def cadastrar_cliente():
    nome =  request.form["nome"]  # <input name='nome' ...>
    email = request.form["email"] # <input name='email' ...>
    model_cadastrar_cliente(nome, email)
    return "<h3>Cadastrado</h3>"

@srv.get("/listar")
def get_listagem_clientes():
    clientes = model_listar_clientes() # acesso à model
    #clientes é uma lista de tuplas (id, nome, email)
    return render_template("listagem.html", lista_clientes = clientes)

if __name__ == "__main__":
    srv.run(host="localhost",
            port=5000,
            debug=True)