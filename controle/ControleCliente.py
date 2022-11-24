from Conectarbanco import *
from modelo.Cliente import *
from controle.controleGenerico import *


class ControleEvento(ControleGenerico):
    __lista = []

    def incluirCliente(self,cliente):
        self.incluir(cliente)

    def procurarCliente(self, cliente):
        self.ob.abrirConexao()
        cliente = self.ob.selectQuery(
            "select * from cliente where idcliente = {}".format(cliente))
        return cliente   

    def pesquisaCodigo(self,entrada):
        cliente = Cliente()
        cliente.idcliente = entrada
        cliente = self.procuraRegistro(cliente)
        retorno = Cliente()
        if len(cliente) >= 1:
            retorno.idcliente = cliente[0][0]
            retorno.nome = cliente[0][1]
            retorno.endereco = cliente[0][2]
            retorno.cidade = cliente[0][3]
            retorno.uf = cliente[0][4]
            retorno.cep = cliente[0][5]
            retorno.nascimento = cliente[0][6]
        return retorno     

    def listarTodosRegistros(self):
        cliente = Cliente()
        return self.listarTodos(cliente)

    def deleteCliente(self,id):
        cliente = Cliente()
        cliente.idcliente = id
        self.delete(cliente)

    def alterarCliente(self, cliente):
        self.alterar(cliente)    

