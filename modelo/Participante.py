from datetime import date, datetime

class Participante:

    def __init__(self):

        self.__idparticipante=""
        self.__nome=""
        self.__flag=0
        self.__email=""
        self.__cpf=""
        self.__lista='nome,email,cpf'

        self.__dadosInserir=""
        self.__dadosUpdate=""
        self.__dadosDelete=""
        self.__dadosPesquisa=""
        self.__tabelaBanco = 'participante'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = "'{}','{}','{}'".format(self.nome, self.email,self.cpf)
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = "nome='{}',endereco='{}' where idaluno={}".format(self.nome, self.email,self.idparticipante)
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where idaluno={}".format(self.idparticipante)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from aluno where idaluno={}".format(self.idparticipante)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def idparticipante(self):
        return self.__idparticipante

    @idparticipante.setter
    def idparticipante(self, entrada):
        self.__idparticipante = entrada

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,entrada):
        self.__nome=entrada

    @property
    def flag(self):
        return self.__flag

    @flag.setter
    def flag(self, entrada):
        self.__flag = entrada

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, entrada):
        self.__email = entrada

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, entrada):
        self.__cpf = entrada



    def __repr__(self):
        return  self.nome

