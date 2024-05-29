from datetime import datetime

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Cadastrar Cliente
[c] Criar Conta
[l] Listar Contas
[i] Listar Clientes
[q] Sair

=> """

limite_saque = 500
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3
ultimo_dia = datetime.now().day
usuarios = []
contas = {}
nome_usuario = ""
id_cliente = 0
id_conta = 0
valor = 0
saldo = 0
extrato = ""

def criar_usuario(nome_usuario):
    if not usuarios:
        novo_id = 1
    else:
        ultimo_usuario = usuarios[-1]
        novo_id = ultimo_usuario["ID"] + 1

    usuarios.append({"ID": novo_id, "NOME": nome_usuario})
    return str(novo_id)

def criar_conta(id_cliente):
    if id_cliente in contas:
        print("Cliente já possui uma conta ativa.")
        return

    novo_id_conta = 1 if not contas else max(contas.keys()) + 1

    contas[novo_id_conta] = {"IDUSUARIO": id_cliente, "SALDO": 0, "EXTRATO": ""}

    print(f"Conta criada com sucesso para o cliente {id_cliente}! ID da conta: {novo_id_conta}")

def listar_contas():
    if not contas:
        print("Não há contas cadastradas.")
        return

    for id_conta, conta in contas.items():
        for usuario in usuarios:
            if usuario["ID"] == conta["IDUSUARIO"]:
                nome_cliente = usuario["NOME"]
                break
        else:
            nome_cliente = "Cliente não encontrado"

        print(f"Cliente: {nome_cliente} - ID Conta: {id_conta} - Saldo: R$ {conta['SALDO']:.2f}")
        print("-------------------------------------------------------------------------------")

def listar_clientes():
    for usuario in usuarios:
        cod_cliente = usuario["ID"]
        nome_cliente = usuario["NOME"]
        print(f"Cód. Cliente: {cod_cliente} - Nome: {nome_cliente}")
        print("-------------------------------------------------------------------------------")
        
def consulta_extrato(id_conta):
    ext_ini = "--------------------------------- EXTRATO ---------------------------------\n"
    ext_fim = "\n---------------------------------------------------------------------------\n"

    mensagem = ""

    if id_conta in contas:
        mensagem = f"{contas[id_conta]['EXTRATO']}\nSaldo: {contas[id_conta]['SALDO']:.2f}"
    else:
        mensagem = "Conta não encontrada"

    return ext_ini + mensagem + ext_fim

def depositar(id_conta, valor):
    if id_conta in contas:
        contas[id_conta]["SALDO"] += valor
        contas[id_conta]["EXTRATO"] += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
        return contas[id_conta]["SALDO"], consulta_extrato(id_conta)
    else:
        print("Conta não encontrada.")
        return None, None
        
def sacar(codigo_conta = id_conta, valor_saque = valor):
    if codigo_conta in contas:
        if valor_saque <= contas[codigo_conta]["SALDO"]:
            contas[codigo_conta]["SALDO"] -= valor_saque
            contas[codigo_conta]["EXTRATO"] += f"Saque: R$ {valor_saque:.2f}\n"
            print("Saque realizado com sucesso!")
            return contas[codigo_conta]["SALDO"], consulta_extrato(id_conta)
        else:
            print("Saldo insuficiente.")
            return None, None
    else:
        print("Conta não encontrada.")
        return None, None
        
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
        id_conta = int(input("Informe o Código da Conta: "))
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo, extrato = depositar(id_conta, valor)
            
            if saldo:
                print(f"Seu novo saldo é: {saldo:.2f}")
                print(extrato)
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES_DIARIOS:
            id_conta = int(input("Informe o Código da Conta: "))
            valor = float(input("Informe o valor do saque: "))
            if valor <= limite_saque:
                saldo, extrato = sacar(id_conta, valor)

                if saldo:
                    print(f"Seu novo saldo é: {saldo:.2f}")
                    print(extrato)
            else:
                print("Operação falhou! O valor do saque excede o limite de R$ 500,00.")
        else:
            print("Operação falhou! Número máximo de saques diários excedido.")

    elif opcao == "e":
        id_conta = int(input("Informe o Código da Conta: "))
        
        extrato = consulta_extrato(id_conta)
        
        if extrato:
            print(extrato)

    elif opcao == "u":
        nome_usuario = str(input("Informe o Nome do Cliente: "))
        
        if nome_usuario != "":
           novo_usuario = criar_usuario(nome_usuario)
           print (f"Novo Usuário criado com sucesso: " + novo_usuario + " - " + nome_usuario)
        else:   
           print ("ATENÇÃO: Nome de Cliente inválido. Tente Novamente!!!")

    elif opcao == "c":
        cod_cliente = int(input("Digite o Código do cliente: "))
        
        if any(usuario["ID"] == cod_cliente for usuario in usuarios):
            criar_conta(cod_cliente)
        else:
            print("Código de cliente não encontrado.")
        
    elif opcao == "l":
        listar_contas()

    elif opcao == "i":
        listar_clientes()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
