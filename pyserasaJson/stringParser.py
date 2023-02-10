def parseNomeCompleto(data_string):
    #Nome Bloco + subtito "N20000"
    #Dado Original: inicia em 7, com 70 de comprimento
    #Dado após Spolit: inicia em 0 e termina em 69
    data_string = data_string.split('N20000')
    data_string = data_string[1][0:70]
    data_string = data_string.split(' ')
    nome = ''
    for i in data_string:
        if i != '':
            nome = nome + i + " "
    return nome

def parseDataNascimento(data_string):
    #Nome Bloco + subtito "N20000"
    #Dado Original: inicia em 77, com 8 de comprimento
    #Dado após Spolit: inicia em 70 e termina em 77
    data_string = data_string.split('N20000')
    data_string = data_string[1][70:78]
    return data_string[0:2] + "/" + data_string[2:4] + "/" + data_string[4:8]

def parseNomeDaMae(data_string):
    #Nome Bloco + subtito "N20001"
    #Dado Original: inicia em 7, com 40 de comprimento
    #Dado após Spolit: inicia em 0 e termina em 40
    data_string = data_string.split('N20001')
    data_string = data_string[1][0:40]
    data_string = data_string.split(' ')
    nome = ''
    for i in data_string:
        if i != '':
            nome = nome + i + " "
    return nome

def parseScore(data_string):
    #Nome Bloco + subtito "N50599"
    #Dado Original: inicia em 7, com 4 de comprimento
    #Dado após Spolit: inicia em 0 e termina em 6
    data_string = data_string.split('F900REHM')
    data_string = data_string[1][0:6].strip(' ')
    if data_string:
        return int(data_string)
    else:
        return 0

def parseProtestos(data_string):
    json = {
        'ocorrencias':0,
        'valorTotal':0,
        'descricao': ''

        }
    
    if len(data_string.split('tipoReg: N250\nsubtipo: 90')) > 1:
        totals_data = data_string.split('tipoReg: N250\nsubtipo: 90')
        totalOcorrencias = totals_data[1].split('totalOcorrencias: ')[1][0:5]
        if totalOcorrencias:
            json['ocorrencias'] = int(totalOcorrencias)
        else:
            json['ocorrencias'] = 0
        valorTotal = totals_data[1].split('valorTotal: ')[1].split('\n')[0]
        if valorTotal:
            json['valorTotal'] = float(valorTotal)
        else:
            json['valorTotal'] = 0
        
        entrys_data = totals_data[0].split('tipoReg: N250\nsubtipo: 00')[1:]
        for entry in entrys_data:
            json['descricao'] = json['descricao'] + entry
            
    return json

def parsePendenciasInternas(data_string):
    json = {
        'ocorrencias':0,
        'valorTotal':0,
        'descricao': ''

        }
    
    if len(data_string.split('tipoReg: N230\nsubtipo: 90')) > 1:
        totals_data = data_string.split('tipoReg: N230\nsubtipo: 90')
        totalOcorrencias = totals_data[1].split('totalOcorrencias: ')[1][0:5]
        if totalOcorrencias:
            json['ocorrencias'] = int(totalOcorrencias)
        else:
            json['ocorrencias'] = 0
        valorTotal = totals_data[1].split('valorTotal: ')[1].split('\n')[0]
        if valorTotal:
            json['valorTotal'] = float(valorTotal)
        else:
            json['valorTotal'] = 0
        
        entrys_data = totals_data[0].split('tipoReg: N230\nsubtipo: 00')[1:]
        for entry in entrys_data:
            json['descricao'] = json['descricao'] + entry
            
    return json

def parsePendenciasFinanceiras(data_string):
    json = {
        'ocorrencias':0,
        'valorTotal':0,
        'descricao': ''

        }
    
    if len(data_string.split('tipoReg: N240\nsubtipo: 90')) > 1:
        totals_data = data_string.split('tipoReg: N240\nsubtipo: 90')
        totalOcorrencias = totals_data[1].split('totalOcorrencias: ')[1][0:5]
        if totalOcorrencias:
            json['ocorrencias'] = int(totalOcorrencias)
        else:
            json['ocorrencias'] = 0
        valorTotal = totals_data[1].split('valorTotal: ')[1].split('\n')[0]
        if valorTotal:
            json['valorTotal'] = float(valorTotal)
        else:
            json['valorTotal'] = 0
        
        entrys_data = totals_data[0].split('tipoReg: N240\nsubtipo: 00')[1:]
        for entry in entrys_data:
            json['descricao'] = json['descricao'] + entry
            
    return json

def parseChequesSemFundo(data_string):
    json = {
        'ocorrencias':0,
        'valorTotal':0,
        'descricao': ''

        }
    
    if len(data_string.split('tipoReg: N270\nsubtipo: 90')) > 1:
        totals_data = data_string.split('tipoReg: N270\nsubtipo: 90')
        totalOcorrencias = totals_data[1].split('totalOcorrencias: ')[1][0:5]
        if totalOcorrencias:
            json['ocorrencias'] = int(totalOcorrencias)
        else:
            json['ocorrencias'] = 0
        valorTotal = totals_data[1].split('valorTotal: ')[1].split('\n')[0]
        if valorTotal:
            json['valorTotal'] = float(valorTotal)
        else:
            json['valorTotal'] = 0
        
        entrys_data = totals_data[0].split('tipoReg: N270\nsubtipo: 00')[1:]
        for entry in entrys_data:
            json['descricao'] = json['descricao'] + entry
            
    return json