def classifica_idade():
    pass
    idade = int(input('Digite sua idade: '))

    lista = [idade]

    crianca = []
    adolecente = []
    adulto = []

    for idade in lista:
        if idade >= 0 and idade <= 12:
            crianca.append(idade)
        elif idade >= 13 and idade <= 18:
            adolecente.append(idade)
        else:
            adulto.append(idade)
        
    print('criança: ', crianca)
    print('adolecente: ', adolecente)
    print('Adulto: ', adulto)
            
    return crianca, adolecente, adulto

classifica_idade()

