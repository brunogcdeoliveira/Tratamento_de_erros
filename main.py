from exception import SaldoInsuficienteError


class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


cliente = Cliente('John Doe', '123.456.789-00', 'Desenvolvedor')


# print(cliente.nome)
# print(cliente.cpf)
# print(cliente.profissao)
#
# # Posso acrescentar um atributo na classe por meio da atribuição de valor
# cliente.idade = 23
# print(cliente.idade)


class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 100
        self.__agencia = 0
        self.__numero = 0

        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__set_numero(numero)
        # ZeroDivisionError
        # ContaCorrente.taxa_operacao = ContaCorrente.total_contas_criadas/30
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = ContaCorrente.total_contas_criadas / 30

    # Getters e Setters
    @property
    def agencia(self):
        return self.__agencia

    def __set_agencia(self, valor):
        if not isinstance(valor, int):
            raise ValueError("Agênca não é um inteiro", valor)
        if valor <= 0:
            raise ValueError("Agênca menor ou igual a 0")
        self.__agencia = valor

    @property
    def numero(self):
        return self.__numero

    def __set_numero(self, valor):
        if not isinstance(valor, int):
            raise ValueError("Numero da conta não é um inteiro")
        if valor <= 0:
            raise ValueError("Numero da conta menor ou igual a 0")
        self.__numero = valor

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, int):
            raise ValueError("Saldo da conta não é um inteiro")
        self.__saldo = valor

    # Outros métodos
    def transferir(self, valor, favorecido):
        favorecido.depositar(valor)

    def sacar(self, valor):
        if (self.saldo < valor):
            raise SaldoInsuficienteError('Saldo insuficiente')
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor


def main():
    import sys

    contas = []
    cont = 0
    while True :
        try:
            nome = input('Nome do cliente: \n')
            agencia = (input('Número da agencia: \n'))
            numero = (input('Número da conta: \n'))
            cliente = Cliente(nome, None, None)

            conta_corrente = ContaCorrente(cliente, agencia, numero)
            contas.append(conta_corrente)

        except ValueError as E:
            print(E.args)
            sys.exit()
        except KeyboardInterrupt:
            print(f'\n\n{len(contas)}(s) contas criadas')
            sys.exit()


# if __name__ == '__main__':
#     main()


conta_corrente = ContaCorrente(None, 400, 1123456)
# conta_corrente.depositar(-100)
# print(f'Saldo: {conta_corrente.saldo}')
conta_corrente.sacar(101)
print(f'Saldo: {conta_corrente.saldo}')
