listaPecas = [] #lista de peças criadas
idPeca = 0 #id das peças criadas

print("--------------------------------------------------------------------------------")
print("Bem vindo ao Controle de estoque da Bicicletaria do RENAN")
print("--------------------------------------------------------------------------------")

while True:
    #MENU DE OPÇÕES
    print("--------------------------------------------------------------------------")
    print("1 - Cadastrar Peça")
    print("2 - Consultar Peça")
    print("3 - Remover Peça")
    print("4 - Sair")
    print("--------------------------------------------------------------------------")
    op = input("Selecione a opção desejada: ")
    print("--------------------------------------------------------------------------")
    
    if(op == "1"): #caso selecionado 1, digite
        idPeca = idPeca+1
        peca = []
        peca.append(idPeca)
        peca.append(input("Por favor entre com o NOME da peça: "))
        peca.append(input("Por favor entre com o FABRICANTE da peça: "))
        peca.append(float(input("Por favor entre com o VALOR da peça: ")))
        
        listaPecas.append(peca)

    elif(op == "2"): #caso selecionado 2, digite

        print("1 - Consultar TODAS as peças")
        print("2 - Consultar peças por CÓDIGO")
        print("3 - Consultar peças por FABRICANTE")
        print("4 - Sair\n")
        opcao = input("Escolha a opção desejada: ")

        if(opcao =="1"): #caso selecionado 1, busque a lista toda

            for peca in listaPecas:
                print("--------------------------------------")
                print("Código: {0}".format(peca[0]))
                print("Nome: {0}".format(peca[1]))
                print("Fabricante: {0}".format(peca[2]))
                print("Valor: {0}".format(peca[3]))
                print("--------------------------------------")
           
        if(opcao =="2"): #caso selecionado 2, busque pelo cogigo
            codigoPeca =  int(input("Digite o CÓDIGO da peça: "))

            for peca in listaPecas:
                if peca[0] == codigoPeca:
                    print("--------------------------------------")
                    print("Código: {0}".format(peca[0]))
                    print("Nome: {0}".format(peca[1]))
                    print("Fabricante: {0}".format(peca[2]))
                    print("Valor: {0}".format(peca[3]))
                    print("--------------------------------------")


        if(opcao == "3"): #caso selecionado 3, busque pelo fabricante
            fabricantePeca =  input("Digite o FABRICANTE da peça: ")

            for peca in listaPecas:
                if peca[2] == fabricantePeca:
                    print("--------------------------------------")
                    print("Código: {0}".format(peca[0]))
                    print("Nome: {0}".format(peca[1]))
                    print("Fabricante: {0}".format(peca[2]))
                    print("Valor: {0}".format(peca[3]))
                    print("--------------------------------------")

        if (opcao == "4"): #caso selecionado 4, continue o programa
            continue

    elif(op == "3"): #caso selecionado 3, remova a peça pelo codigo
        print("Você selecionou a opção de remover peças")
        codigoDelete = input("Digite o Codigo da Peça a Ser removida: ")

        for peca in listaPecas:
            if peca[0] == codigoPeca:
                listaPecas.remove(peca)

    elif(op == "4"): #caso selecionado 1, pare o programa
        break

    else:
        print("Operação Invalida") #caso selecionado qualquer coisa diferente de 1 a 4, operação invalida