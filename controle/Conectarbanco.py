import pymysql

class Banco:

   def __init__(self):
       self.servidor="localhost"
       self.usuario="root"
       self.senha="ifsp"
       self.banco="aulas"
       self.ponteiro =""

   def abrirConexao(self):
      self.con = pymysql.connect(host=self.servidor,db=self.banco, user=self.usuario, passwd=self.senha)
      self.ponteiro=self.con.cursor()
      

   def selectQuery(self,entrada):
      self.ponteiro.execute(entrada)
      resposta = self.ponteiro.fetchall()
      return resposta

   def executeQuery(self, entrada,dados):
       self.ponteiro.execute(entrada,dados)

   def execute(self, entrada):
       self.ponteiro.execute(entrada)

   def gravar(self):
      self.con.commit()

   def descarte(self):
      self.con.rollback()

   def configura(self,ho,db,se="ifsp",us='root'):
       self.servidor = ho
       self.usuario = us
       self.senha = se
       self.banco = db

   def mostraResultado(self,entrada):
       for i in entrada:
           print(i)