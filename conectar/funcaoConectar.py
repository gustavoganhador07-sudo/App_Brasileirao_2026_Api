import sqlite3

def conectar():
    return sqlite3.connect("./Bancodados/Brasileirao26DB.db")  # banco no mesmo diretório