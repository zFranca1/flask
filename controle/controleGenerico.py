from Conectarbanco import *
from modelo.Cliente import *
import json
import datetime

class ControleGenerico:

    def __init__(self):
        self.ob = Banco()
        self.ob.configura(ho="localhost", db="aulas", us="root",se="ifsp")

    def incluir(self,objeto):
        self.ob.abrirConexao();
        sql = "insert into {} ".format(objeto.tabelaBanco)+'('
        sql+= '{}'.format(objeto.lista)
        sql+= ') values ({})'.format(objeto.dadosInserir)

        print(sql)
        try:
           self.ob.execute(sql)
           self.ob.gravar()
        except:
           print("Houve um erro")
           self.ob.descarte()

    def incluirGeral(self, objeto):
        self.ob.abrirConexao();
        sql = "insert into {} ".format(objeto.tabelaBanco) + '('
        sql += '{}'.format(objeto.lista)
        sql += ') values ({})'.format(objeto.dadosInserir)

        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except:
            print("Houve um erro")
            self.ob.descarte()

        sql = 'select max(idvenda) from venda'
        valor = self.ob.selectQuery(sql)
        objeto.idvenda = valor[0][0]

        itens = objeto.itens
        for i in itens:
            idvenda = objeto.idvenda
            idproduto = i[0]
            qtde = i[1]
            preco = i[2]
            sql = "insert into  itemvenda (idvenda,idproduto,qtde,valor) "
            sql += 'values ({},{},{},{})'.format(idvenda,idproduto,qtde,preco)
            try:
                self.ob.execute(sql)
                self.ob.gravar()
            except:
                print("Houve um erro")
                self.ob.descarte()

    def alterar(self,objeto):
        self.ob.abrirConexao();
        sql = "update {} ".format(objeto.tabelaBanco)
        sql += 'set {}'.format(objeto.dadosUpdate)  

        print(sql)
        try:
           self.ob.execute(sql)
           self.ob.gravar()
        except:
           print("Houve um erro")
           self.ob.descarte()

    def delete(self, objeto):
        self.ob.abrirConexao();
        sql = "delete from {} ".format(objeto.tabelaBanco)
        sql += objeto.dadosDelete

        print(sql)
        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except:
            print("Houve um erro")
            self.ob.descarte()

    def procuraRegistro(self,objeto):
        self.ob.abrirConexao();
        objeto = self.ob.selectQuery(objeto.dadosPesquisa)
        return objeto

    def apagar(self,entrada):
        self.ob.abrirConexao();
        sql = "delete from cliente where idcliente = {}".format(entrada)
        self.ob.execute(sql)
        self.ob.gravar()

    def listarTodos(self,objeto):
        self.ob.abrirConexao();
        dados = self.ob.selectQuery("select * from {}".format(objeto.tabelaBanco))
        return dados




