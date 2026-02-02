import sqlite3 as sql

class TransactionObject():

    database = 'clientes.db'
    conn = None
    cur = None
    connected = False

    def connect(self):

        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):

        TransactionObject.conn.close()
        TransactionObject.connected = False

    def excute(self, sql, parms = None):

        if TransactionObject.connected:

            if parms == None:

                TransactionObject.cur.execute(sql)
            
            else:

                TransactionObject.cur.execute(sql, parms)
            
            return True
        
        else:
            return False
        
    def fetchall(self):

        return TransactionObject.cur.fetchall()
    
    def persist(self):

        if TransactionObject.connected:

            TransactionObject.conn.commit()
        
            return True
        
        else:

            return False
    
    @staticmethod
    def initDB():

        trans = TransactionObject()
        trans.connect()

        trans.excute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
        
        trans.persist()
        trans.disconnect()

    @staticmethod
    def insert(nome, email, cpf, sobrenome):

        trans = TransactionObject()

        trans.connect()
        trans.excute("INSERT INTO clientes VALUES(NULL, ?,?,?,?)", (nome, sobrenome, email, cpf))
        trans.persist()
        trans.disconnect()
    
    @staticmethod
    def view():

        trans = TransactionObject()

        trans.connect()
        trans.excute("SELECT * FROM clientes ")

        rows = trans.fetchall()

        trans.disconnect()

        return rows
    
    @staticmethod
    def search(nome = '', email = '', sobrenome = '', cpf = ''):

        trans = TransactionObject()

        trans.connect()
        trans.excute("SELECT * FROM clientes WHERE nome=? or sobrenome=? or email=? or cpf=?", (nome, sobrenome, email, cpf))
        rows = trans.fetchall()
        trans.disconnect()

        return rows
    
    @staticmethod
    def delete(id):

        trans = TransactionObject()
        
        trans.connect()
        trans.excute("DELETE FROM clientes WHERE id =?", (id,))
        trans.persist()
        trans.disconnect()

    @staticmethod
    def update(id, nome, sobrenome, email, cpf):

        trans = TransactionObject()

        trans.connect()
        trans.excute("UPDATE clientes SET nome =?, sobrenome=?, email=?, cpf=? WHERE id =?", (nome, sobrenome, email, cpf, id))
        trans.persist()
        trans.disconnect()


def view():
    return TransactionObject.view()

def search(nome='', sobrenome='', email='', cpf=''):
    return TransactionObject.search(nome, email, sobrenome, cpf)

def insert(nome, email, cpf, sobrenome):
    return TransactionObject.insert(nome, email, cpf, sobrenome)

def update(id, nome, sobrenome, email, cpf):
    return TransactionObject.update(id, nome, sobrenome, email, cpf)

def delete(id):
    return TransactionObject.delete(id)

TransactionObject.initDB()