menu = """
Escolha uma opção:
1 - Depositar
2 - Sacar
3 - Visualizar saldo
0 - Sair
"""
saldo = 0
limite = 500.0
extrato = ''
quantidade_saques = 0
LIMITE_SAQUES = 3

while True:
        
    opcao = input(menu)

    if opcao == '1':
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        if valor_deposito < 0:
            print('Não é permitido valor negativo')
        else:
            saldo += valor_deposito
            extrato = extrato + f'Depósito de R${valor_deposito:.2f}\n'

    elif opcao == '2':
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        if valor_saque > limite:
            print("Ultrapassou o limite do valor do saque. MAX: R$500.0")
        elif quantidade_saques >= LIMITE_SAQUES:
            print("Alcançado o limite de saques permitidos. MAX: 3")
        elif valor_saque > saldo:
            print("Saldo insuficiente")
        elif valor_saque < 0:
            print("Não é permitido valor negativo")
        else:
            saldo -= valor_saque
            quantidade_saques += 1
            extrato += f"Saque de R${valor_saque:.2f}\n"

    elif opcao == '3':
        print(extrato)
        print(f'Saldo atual da conta: {saldo}')
    
    elif opcao == '0':
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Por favor, digite um número válido.")
