def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito < 0:
        print('Não é permitido valor negativo')
    else:
        saldo += valor_deposito
        extrato += f'Depósito de R${valor_deposito:.2f}\n'
    return saldo, extrato

def sacar(*, saldo, valor_saque, limite, quantidade_saques, limite_saques, extrato):
    if valor_saque > limite:
        print("Ultrapassou o limite do valor do saque. MAX: R$500.0")
    elif quantidade_saques >= limite_saques:
        print("Alcançado o limite de saques permitidos. MAX: 3")
    elif valor_saque > saldo:
        print("Saldo insuficiente")
    elif valor_saque > 0:
        saldo -= valor_saque
        quantidade_saques += 1
        extrato += f"Saque de R${valor_saque:.2f}\n"
    else:
        print("Não é permitido valor negativo")
    
    return saldo, extrato, quantidade_saques

def exibir_extrato(saldo, /, *,extrato):
    print(extrato)
    print(f'Saldo atual da conta: {saldo}')

def criar_usuario(usuarios):
    cpf = input('Informe seu cpf: ')
    usuario = filtrar_usuarios(usuarios, cpf)
    if usuario:
        print('Usuário já cadastrado!')
        return
    nome = input('Informe seu nome completo: ')
    data_nascimento = input('Informe sua data de nascimento: (dd/mm/aaaa)')
    endereco = input('Informe seu endereço (logradouro, nro - bairro - cidade/sigla estado):')
    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco":endereco})
    print('Usuário foi cadastrado com sucesso!')

def filtrar_usuarios(lista, cpf_procurado):
    return [pessoa for pessoa in lista if pessoa.get('cpf') == cpf_procurado]

def criar_conta_corrente(agencia, nro_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(usuarios, cpf)
    if usuario:
        print('Conta criada com sucesso!')
        return {"agencia": agencia, "nro_conta": nro_conta, "usuario" : usuario}
    print('CPF não encontrado')

if __name__ == "__main__":
    
    menu = """
    Escolha uma opção:
    1 - Depositar
    2 - Sacar
    3 - Visualizar saldo
    4 - Criar Usuário
    5 - Criar Conta
    0 - Sair
    """
    saldo = 0
    limite = 500.0
    extrato = ''
    quantidade_saques = 0
    
    usuarios = []
    contas = []

    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    while True:
            
        opcao = input(menu)

        if opcao == '1':
            valor_deposito = float(input("Digite o valor que deseja depositar: "))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao == '2':
            valor_saque = float(input("Digite o valor que deseja sacar: "))
            saldo, extrato, quantidade_saques = sacar(saldo=saldo, valor_saque=valor_saque, 
                                        limite=limite, quantidade_saques=quantidade_saques, 
                                        limite_saques=LIMITE_SAQUES, extrato=extrato)
            
        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == '4':
            criar_usuario(usuarios)

        elif opcao == '5':
            numero_conta = len(contas) + 1
            conta = criar_conta_corrente(AGENCIA,numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == '0':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Por favor, digite um número válido.")