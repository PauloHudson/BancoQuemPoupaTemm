# Nome: Paulo Hudson Josué da Silva RA: 22222013-9
# Nome: kawan Mark Geronimo da Silva RA: 22222010-5
# função Menu....

import datetime
import json
# aqui estaos abrindo o arquivo txt, e validno cada linha do txt, em linhas separadas!!!.


def Options():
    print(   '-'*19)
    print(" 1. Novo Cliente\n 2. Apaga Cliente \n 3. Listar Clientes \n 4. Depósito \n 5. Débito \n 6. Transferência Entre Contas \n 7. ExtratoUP \n 8. Pagamento de Contas \n 9. Sair")
    print(  '-'*19)
Options()
# função Dados Solicitados
# função geral:
# Funções Principais.
# lista onde ficará as informações;
#----------------------------LISTAS TEMPORARIASSSSS-------------------------------------------------------------
Extrato = []
InfomacoesDosclientes = []
#---------------------------------------------------------------------------------------------------------------
ExtratoUP = []
ListaClientesFormat = []
#---------------------------------------------------------------------------------------------------------------
def OpenExtr():
    ExtratoUP.clear()
    with open("Extrato.txt", "r") as arquivo:
        conteudo = arquivo.readlines()

    for linha in conteudo:
        # estamos tirando os espacos embranco, dividndo a linah em uma lista de string separads por virgula e tirando os colchetes.
        lista_str = linha.strip().split(", ")
        lista = [item.strip("[]'") for item in lista_str]
        ExtratoUP.append(lista)
OpenExtr()

#------------------------------ abrir o arquivo txt.-------------------------------------------------------------
# precisamos retoranar um array de obj, com o readlines retornariamos uma string!. por isso json.
def opeen():
    ListaClientesFormat.clear()
    with open('Clientes.txt', 'r') as arquivo:
        for line in arquivo:
            if line in ListaClientesFormat:
                break
            else:
                try:
                    cliente = json.loads(line)
                    ListaClientesFormat.append(cliente)
                except json.JSONDecodeError:
                    # se alguma linha do json for invalida ele pula.
                    continue
opeen()


# --------------------------------------------------------------------------------------------------------------
def opcao1():
    print ('\033[31m'+'Digite Seus Dados'+'\033[0;0m')
    DicValues = {}
    ExtratoValues = []

    ExtratoValues.append(f"Data: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    DicValues["nome"] = input("Nome: ")
    DicValues['Tconta'] = input("Tipo de Conta (Plus ou Comum): ").lower()

    while(DicValues['Tconta'] != 'comum' and DicValues['Tconta'] != 'plus'):
        print('Digite somente plus ou comum')
        DicValues['Tconta'] = input("Tipo de Conta (Plus ou Comum): ").lower()
  
    cpf = int(input("CPF: "))
    # estamos percorrendo o arquivo txt que estamos a ler e validando se há esse cpf dentro dele.

    for cliente in ListaClientesFormat:
        if cliente.get('cpf') == cpf:
            print ('\033[31m'+'Usuário Já Cadastrado!!!'+'\033[0;0m')
            break

    else:
        DicValues["cpf"] = cpf
        ExtratoValues.append(f"CPF: {cpf}")
        DicValues["Senha"] = int(input("Senha: "))
        ExtratoValues.append(F"Senha: {DicValues['Senha']}")
        DicValues["Saldo"] = int(input("Valor inicial da Conta: "))
        ExtratoValues.append(F"Saldo: R$ {DicValues['Saldo']} ")
        # adicionando na lista local
        Extrato.append(ExtratoValues[:])
        # --------------------------------------------------------------------------------------------------------------
                    #FUNCAO QUE VAI MANDAR OS OBJS PARA O TXT
            # funcao para mandar para um txt as informacoesDosClientes..
        # precismaos importar o Json para mandar a lista de dicionarios.
        InfomacoesDosclientes.append(DicValues.copy())
        # ---------------
        with open("Clientes.txt", "a") as Clientes:
            for cliente in InfomacoesDosclientes:
                json.dump(cliente, Clientes)
                Clientes.write('\n')
        # -------------
        with open("Extrato.txt", "a") as infs:
            for cliente in Extrato:
                infs.write(str(cliente))
                infs.write('\n')

        # no final de cada execucao ele da um clear na lista de clientes, para nao adicionar clientes repetidos...
        InfomacoesDosclientes.clear()
        Extrato.clear()
        # --------------------------------------------------------------------------------------------------------------

    print('-'*19)
# funções principais.
# funcao se subscrever.
# basicamente ela vai pegar o valor da edicao e jogar dentro do txt, assim subscrevendo o atual.
def Subs():
    with open("Clientes.txt", "w") as Clientes:
        for cliente in ListaClientesFormat:
            json.dump(cliente, Clientes)
            Clientes.write('\n')

def Exts():
     with open("Extrato.txt", "w") as infs:
            for cliente in ExtratoUP:
                infs.write(str(cliente))
                infs.write('\n')
# --------------------------------------------------------------------------------------------------------------
def opcao2():
    print('\033[31m'+'Apagar Cliente'+'\033[0;0m')
    cpf = int(input("Digite o CPF: "))
    # basicamente uma variavel chamada cpf,
    #estamos percorrendo todo o array com os dic, chamando suas posiçoes de indice e os valores de cliente,
    #se for encontrado algum valor correspondente ao cpf informado pela var
    #removemos o indice inteiro, por isso enumeramos o array.
    #estamos iterando pelo array e ao mesmo tempo obtemos o indice.
    # for cliente in enumerate(ListaClientesFormat):
    for cliente in ListaClientesFormat:
        if cliente.get("cpf") == cpf:
            ListaClientesFormat.remove(cliente)
            Subs()

# --------------------------------------------------------------------------------------------------------------
def opcao3():
    print('\033[31m'+'Lista de Clientes'+'\033[0;0m')
    for inf in ListaClientesFormat:
        print("----" * 20)
        print(f"\033[33mNome\033[0m: {inf['nome']}, \033[33mTipo de de Conta\033[0m: {inf['Tconta']}, \033[33mCPF\033[0m: {inf['cpf']}, \033[33mSenha\033[0m: {inf['Senha']}, \033[33mSaldo\033[0m: R$ {inf['Saldo']} ")
        print("----" * 20)
# --------------------------------------------------------------------------------------------------------------
def opcao4():
    print('\033[31m'+'Função De Depósito'+'\033[0;0m')
    cpf = int(input("Digite o CPF: "))
    senha = int(input("Digite sua Senha: "))
    for indice, cliente in enumerate(ListaClientesFormat):
            if cliente.get('cpf') == cpf and cliente.get('Senha') == senha:
                ExtratoUP[indice].append(f"Data: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                valorAdepositar = float(input("Digite a Quantidade a Depositar: "))
                cliente["Saldo"] += valorAdepositar
                saldo = cliente["Saldo"]
                ExtratoUP[indice].append(f"Recebimento: + ${valorAdepositar}")
                ExtratoUP[indice].append(f"Tarifa: 0.0")
                ExtratoUP[indice].append(f"Saldo: R$ {saldo}")
                Exts()
                Subs()
                break
    else:
        print("senha ou usuário inválidos...")

# --------------------------------------------------------------------------------------------------------------        
def opcao5():
    banco = 0
    print('\033[31m'+'Função De Debito (SAQUE) '+'\033[0;0m')
    cpf = int(input("Digite o CPF: "))
    senha = int(input("Digite sua Senha: "))

    for indice, cliente in enumerate(ListaClientesFormat):
        if cliente.get('cpf') == cpf and cliente.get('Senha') == senha:
            valorAdepositar = float(input("Digite a Quantidade a Retirar: "))

            if cliente.get("Tconta") == 'comum':
                ExtratoUP[indice].append(f"Data: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                banco = (valorAdepositar * 0.05)
                cliente['Saldo'] -= banco
                ExtratoUP[indice].append(f"Saque: -R${valorAdepositar}")

                cliente['Saldo'] -= valorAdepositar

                ExtratoUP[indice].append(f"Tarifa: {banco:.2f}")

                

                saldo = cliente["Saldo"]
                ExtratoUP[indice].append(f"Saldo: R$ {saldo}")
                if cliente.get('Saldo') >= -1000:
                    Subs()
                    True
                else:
                    print("Operação Não Permitida Saldo inferior a R$ -1000.00")
                    cliente['Saldo'] += banco
                    ExtratoUP[indice].append(f"Reestituído: + {banco}")
                    cliente['Saldo'] += valorAdepositar
                    ExtratoUP[indice].append(f"Reestituído: + {valorAdepositar}")
                    ExtratoUP[indice].append(f"Saldo: R$ {saldo}:2.f")
                    break

            if cliente.get("Tconta") == 'plus':
                ExtratoUP[indice].append(f"Data: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                banco = (valorAdepositar * 0.03)
                cliente['Saldo'] -= banco
                ExtratoUP[indice].append(f"Saque: -R${valorAdepositar}")
                cliente['Saldo'] -= valorAdepositar
                ExtratoUP[indice].append(f"Tarifa: {banco:.2f}")
                saldo = cliente["Saldo"]
                ExtratoUP[indice].append(f"Saldo: R$ {saldo}")
                if cliente.get('Saldo') >= -5000:
                    Subs()
                    True
                else:
                    print("Operação Não Permitida Saldo inferior a R$ -5000.00")
                    ExtratoUP[indice].append(f"Data: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    cliente['Saldo'] += banco
                    ExtratoUP[indice].append(f"Reestituído: + {banco}")
                    cliente['Saldo'] += valorAdepositar
                    ExtratoUP[indice].append(f"Reestituído: + {valorAdepositar}")
                    ExtratoUP[indice].append(f"Saldo R$: {saldo}")
                    break

            print("\033[31m" + "Taxa de Movimentação de R$ \033[37m{:.2f}\033[31m!".format(banco) + "\033[0;0m")
            print("\033[31mSaldo De R$ \033[37m{:.2f}\033[31m!\033[0;0m".format(cliente['Saldo']))
            Exts()
            Subs()
            break
    else:
        print("senha ou usuário inválidos...")
        
# --------------------------------------------------------------------------------------------------------------
def opcao6():
    print('\033[31m'+'Digite As informacoes da conta de origem!'+'\033[0;0m')
    cpf = int(input("Digite o CPF: "))
    senha = int(input("Digite sua Senha: "))
    # 
    banco = 0
    # 
    for indice, cliente1 in enumerate(ListaClientesFormat):
        if cliente1.get('cpf') == cpf and cliente1.get('Senha') == senha:
            ValorTransferencia = int(input("Digite o valor a transferir: "))
            # valor de ExtratoUP na lista.
            #
            # validar se está negativo..
            if cliente1.get('Tconta') == 'comum':
                ExtratoUP[indice].append(f"Data: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                ExtratoUP[indice].append(f"Valor Transf.: - {ValorTransferencia}")
                banco = (ValorTransferencia * 0.05)
                ExtratoUP[indice].append(f"Tarifa: {banco:.2f}")
                cliente1['Saldo'] -= banco
                cliente1['Saldo'] -= ValorTransferencia 
                ExtratoUP[indice].append(f"Saldo R$ : {cliente1['Saldo']:.2f}")
                if cliente1.get('Saldo') >= -1000:
                    Subs()
                    True
                else:
                    print("Operação Não Permitida Saldo inferior a R$ -1000.00")
                    cliente1['Saldo'] += banco
                    ExtratoUP[indice].append(f"Rees.: + {banco}")
                    cliente1['Saldo'] += ValorTransferencia 
                    ExtratoUP[indice].append(f"Rees.: + {ValorTransferencia}")
                    ExtratoUP[indice].append(f"Saldo R$ : {cliente1['Saldo']:.2f}")
                    break


            if cliente1.get('Tconta') == 'plus':
                ExtratoUP[indice].append(f"Data: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                ExtratoUP[indice].append(f"Valor Transf.: - {ValorTransferencia}")
                banco = (ValorTransferencia * 0.03)
                ExtratoUP[indice].append(f"Tarifa: {banco:.2f}")
                cliente1['Saldo'] -= banco
                cliente1['Saldo'] -= ValorTransferencia 
                ExtratoUP[indice].append(f"Saldo: R$ {cliente1['Saldo']:.2f}")
                if cliente1.get('Saldo') >= -5000:
                    Subs()
                    True
                else:
                    # se não der certo, ele simplesmente volta o valor a conta.
                    print("Operação Não Permitida Saldo inferior a R$ -5000.00")
                    cliente1['Saldo'] += banco
                    ExtratoUP[indice].append(f"Rees.: + {banco}")
                    cliente1['Saldo'] += ValorTransferencia 
                    ExtratoUP[indice].append(f"Rees.: + {ValorTransferencia}")
                    ExtratoUP[indice].append(f"Saldo: R$ {cliente1['Saldo']:.2f}")
                    break
            # 
            print("\033[31m" + "Taxa de Movimentação de R$ \033[37m{:.2f}\033[31m!".format(banco) + "\033[0;0m")

            CpfNewAccount = int(input('\033[31m'+'CPF da conta a ser depositada: '+'\033[0;0m'))
            for indice, cliente2 in enumerate(ListaClientesFormat):
                if cliente2.get('cpf') == CpfNewAccount:
                    ExtratoUP[indice].append(f"Data: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    cliente2['Saldo'] += ValorTransferencia
                    ExtratoUP[indice].append(f"Recebido: {ValorTransferencia}")
                    ExtratoUP[indice].append(f"Tarifa: 0.0")
                    ExtratoUP[indice].append(f"Saldo: R$ {cliente2['Saldo']:.2f}")
                    Exts()
                    Subs()
                    break
                else:
                     print("---" *10)
                     print("Senha ou CPF inválidos")
                     print("---" *10)
                     break

        else:           
            print("---" *10)
            print("Senha ou CPF inválidos")
            print("---" *10)
            break
# --------------------------------------------------------------------------------------------------------------
def opcao7():
    cpf = input("Digite o CPF: ")
    senha = input("Digite sua Senha: ")
    print('\n----------------------------------------------------------------------------------------------------------------------')
    for elemento in ExtratoUP:
        if any(['CPF: ' + cpf in elemento and 'Senha: ' + senha in elemento]):
            for valor in elemento:
                if 'Data' in valor:
                    print()
                    print(valor.ljust(25), end=" ")
                else:
                    print(valor.ljust(25), end=" ")
            print()
            print('\n----------------------------------------------------------------------------------------------------------------------')
            break 
    else:
        print(f"Usuário ou senha inválida")

#-------------------------------------------------------------------------------------------------------------

def opcao8():
    print('\033[31m'+'Entrou na opção 8 - Pagamento de contas'+'\033[0;0m')
    cpf = int(input("CPF: "))
    senha = int(input("Senha: "))
    for indice, cliente in enumerate(ListaClientesFormat):
        if cliente["cpf"] == cpf and cliente["Senha"] == senha:
            valorPagamento = float(input("Digite o valor do pagamento: "))
            if valorPagamento > cliente["Saldo"]:
                print("Saldo insuficiente.")
                return
            codigoBoleto = input("Digite o código de barras do boleto: ")
            ExtratoUP[indice].append(f"Data: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            ExtratoUP[indice].append(f"Valor: - {valorPagamento}")
            ExtratoUP[indice].append(f"Tarifa: 0.0")
            cliente["Saldo"] -= valorPagamento
            saldo = cliente["Saldo"]
            ExtratoUP[indice].append(f"Saldo: R$ {saldo}")

            print(f"Pagamento de R$ {valorPagamento:.2f} para o boleto {codigoBoleto} realizado com sucesso!")
            Exts()
            Subs()
            return
    print("CPF ou senha inválida.")





# Laço infinito para rodar durante todo o código...
while(True):
    entrada = int(input("Selecione Uma Opção Acima: "))
    if(entrada == 1):
        OpenExtr()
        opeen()
        opcao1()
        # função para Sair do While.
        sair = input("Deseja sair? (\033[32mS\033[0m or \033[31mN\033[0m)")
        if(sair == "S" or sair == 's'):
            break
        else:
            Options()
 

    elif(entrada == 2):
        OpenExtr()
        opeen()
        opcao2()
        # função para Sair do While.
        sair = input("Deseja sair? (\033[32mS\033[0m or \033[31mN\033[0m)")
        if(sair == "S" or sair == 's'):
            break
        else:
            Options()


    elif(entrada == 3):
        OpenExtr()
        opeen()
        opcao3()
        # função para Sair do While.
        sair = input("Deseja sair? (\033[32mS\033[0m or \033[31mN\033[0m)")
        if(sair == "S" or sair == 's'):
            break
        else:
            Options()


    elif(entrada == 4):
        OpenExtr()
        opeen()
        opcao4()
        sair = input("Deseja sair? (\033[32mS\033[0m or \033[31mN\033[0m)")
        if(sair == "S" or sair == 's'):
            break
        else:
            Options()


    elif(entrada == 5):
        OpenExtr()
        opeen()
        opcao5()
        # função para Sair do While.
        sair = input("Deseja sair? (\033[32mS\033[0m or \033[31mN\033[0m)")
        if(sair == "S" or sair == 's'):
            break
        else:
            Options()   
    elif(entrada == 6):
        OpenExtr()
        opeen()
        opcao6()
        # função para Sair do While.
        sair = input("Deseja sair? (\033[32mS\033[0m or \033[31mN\033[0m)")
        if(sair == "S" or sair == 's'):
            break
        else:
            Options() 
    elif(entrada == 7):
        OpenExtr()
        opeen()
        opcao7()
        # função para Sair do While.
        sair = input("Deseja sair? (\033[32mS\033[0m or \033[31mN\033[0m)")
        if(sair == "S" or sair == 's'):
            break
        else:
            Options()   
    elif(entrada == 8):
        OpenExtr()
        opeen()
        opcao8()
        # função para Sair do While.
        sair = input("Deseja sair? (\033[32mS\033[0m or \033[31mN\033[0m)")
        if(sair == "S" or sair == 's'):
            break
        else:
            Options() 
    elif(entrada == 9):
        print('Obrigado')
        break
# --------------------------------------------------------------------------------------------------------------   