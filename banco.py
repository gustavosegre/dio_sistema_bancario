class Banco:
    def __init__(self):
        self.saldo_conta = 0
        self.transacoes = []
        self.saques = 0
        self.limite_saques = 3

    def opcoes(self):
        opcao = input('Digite sua opção: ')
        if opcao == 'd':
            valor_deposito = float(input('Digite o valor a depositar: '))
            self.deposito(valor_deposito)
        elif opcao == 's':
            valor_saque = float(input('Digite o valor a sacar: '))
            self.saque(valor_saque)
        elif opcao == 'e':
            self.extrato()
        else:
            print('Digite uma opção válida')

    def deposito(self, depositar):
        self.saldo_conta += depositar
        self.transacoes.append(('Deposito', depositar))
        print('Foi depositado em sua conta o valor de: R$', depositar)
        print('Saldo total da sua conta é: ', self.saldo_conta)

    def saque(self, sacar):
        if self.saques >= self.limite_saques:
            print('Limite de saques excedido')
            return

        if self.saldo_conta < sacar:
            print('Não sera possível sacar por falta de saldo')
        else:
            self.saldo_conta -= sacar
            self.saques += 1
            self.transacoes.append(('Saque', sacar))
            print(f'Saque de R$: {sacar} foi realizado')
            print('Seu saldo total é de: R$', self.saldo_conta)

    def extrato(self):
        print('Extrato:')
        for tipo, valor in self.transacoes:
            print(f'{tipo}: R$ {valor}')
        print('Saldo atual da conta:', self.saldo_conta)


cliente1 = Banco()
cliente1.opcoes()
cliente1.deposito(1000)
cliente1.saque(100)
cliente1.saque(100)
cliente1.deposito(2000)
cliente1.saque(200)
cliente1.extrato()
