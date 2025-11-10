import sqlite3

conn = sqlite3.connect("clientes.db")
sql_create_table_clientes = '''
CREATE TABLE IF NOT EXISTS clientes (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome Text,
email Text
);
'''
conn.execute(sql_create_table_clientes)
conn.close()