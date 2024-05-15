# Variáveis para armazenar transações e saldo
transacoes_deposito = []
transacoes_saque = []
saldo = 0

def depositar(valor):
    if valor > 0:
        global saldo, transacoes_deposito
        saldo += valor
        transacoes_deposito.append(valor)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido. O valor do depósito deve ser positivo.")
def sacar(valor):
    global saldo, transacoes_saque
    saques_hoje = len(transacoes_saque)
    limite_diario = 3
    limite_saque = 500

    if saques_hoje < limite_diario and valor <= limite_saque and valor <= saldo:
        saldo -= valor
        transacoes_saque.append(valor)
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        if saques_hoje >= limite_diario:
            print(f"Limite de saques diários excedido ({limite_diario} saques).")
        elif valor > limite_saque:
            print(f"Limite de valor por saque excedido (R$ {limite_saque:.2f}).")
        else:
            print("Saldo insuficiente para realizar o saque.")

def exibir_extrato():
    print("\n--- Extrato da Conta ---")
    for deposito in transacoes_deposito:
        print(f"Depósito: R$ {deposito:.2f}")
    for saque in transacoes_saque:
        print(f"Saque: R$ {-saque:.2f}") 
    print(f"\nSaldo atual: R$ {saldo:.2f}")

while True:
    print("\n--- Menu de Opções ---")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("0. Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        valor_deposito = float(input("Valor do depósito: R$ "))
        depositar(valor_deposito)
    elif opcao == 2:
        valor_saque = float(input("Valor do saque: R$ "))
        sacar(valor_saque)
    elif opcao == 3:
        exibir_extrato()
    elif opcao == 0:
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
