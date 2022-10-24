import sqlite3 as sql

con =sql.connect('dados.db')

#INSERT===========================================================================================================
def inserir(i):
    with con:
        cur = con.cursor()
        insert = 'INSERT INTO inventario (nome, local, descricao, marca, data_da_compra,valor_da_compra,serie, imagem) VALUES(?,?,?,?,?,?,?,?)'
        cur.execute(insert,i)

#UPDATE===========================================================================================================
def update(i):
    with con:
        cur = con.cursor()
        update = 'UPDATE inventario set nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?'
        cur.execute(update,i)

#DELETE===========================================================================================================
def delete(i):
    with con:
        cur = con.cursor()
        delete = 'DELETE FROM inventario WHERE ID =?'
        cur.execute(delete,i)

#SELECT INDIVIDUAL================================================================================================
def select_individual(id):
    ver_um_dado=[]
    with con:
        cur = con.cursor()
        select = 'SELECT * FROM inventario WHERE id=?'
        cur.execute(select,id)

        rows = cur.fetchall()
        for row in rows:
            ver_um_dado.append(row)

#SELECT===========================================================================================================
def select():
    ver_dados=[]

    with con:
        cur = con.cursor()
        select = 'SELECT * FROM inventario'
        cur.execute(select)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)

    return ver_dados