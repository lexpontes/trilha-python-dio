from datetime import datetime

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3
ultimo_dia = datetime.now().day

def resetar_saques():
    global numero_saques
    numero_saques = 0

while True:
    dia_atual = datetime.now().day
    if dia_atual != ultimo_dia:
        resetar_saques()
        ultimo_dia = dia_atual

    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES_DIARIOS:
            valor = float(input("Informe o valor do saque: "))
            if valor <= limite_saque and valor <= saldo:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso!")
            elif valor > saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            else:
                print("Operação falhou! O valor do saque excede o limite de R$ 500,00.")
        else:
            print("Operação falhou! Número máximo de saques diários excedido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if extrato:
            print(extrato, end="")
        else:
            print("Não foram realizadas movimentações.")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
