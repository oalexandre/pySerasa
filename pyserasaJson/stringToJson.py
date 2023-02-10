from .parserStringDados import ParserStringDados
from .crednet import Crednet
import datetime
from .stringParser import parseNomeCompleto, parseDataNascimento, parseNomeDaMae, parseScore, parseProtestos, parsePendenciasInternas, parsePendenciasFinanceiras, parseChequesSemFundo

def stringToJson(cpf, estado, usuario, senha, producao):

    json = {
        'nomeCompleto':'',
        'dataNascimento':'',
        'nomeMae':'',
        'pendenciasInternas':'',
        'pendenciasFinanceiras':'',
        'protestos':'',
        'chequesSemFundo':'',
        'score':'',

    }

    a = ParserStringDados()
    crednet = Crednet()

    #gera URL de consulta
    dados = a.gerar_string_envio(cpf, estado, usuario, senha, producao)
    
    #realzia consulta na URL do SERASA
    response = a.realizar_busca_serasa(dados)
    
    json['nomeCompleto'] = parseNomeCompleto(response)
    json['dataNascimento'] = parseDataNascimento(response)
    json['nomeMae'] = parseNomeDaMae(response)
    json['score'] = parseScore(response)
    
    #constroi o objeto com os dados retornados conm base na crasse Crednet
    parseString = a.parser_string_dados_retorno(response, crednet)
    todosBlocos = ''
    for i in parseString.blocos:
        stringRetorno = parseString.get_string(i)
        if stringRetorno != "":
            todosBlocos = todosBlocos + '\n' + stringRetorno
    
    json['protestos'] = parseProtestos(todosBlocos)
    json['pendenciasFinanceiras'] = parsePendenciasFinanceiras(todosBlocos)
    json['pendenciasInternas'] = parsePendenciasInternas(todosBlocos)
    json['chequesSemFundo'] = parseChequesSemFundo(todosBlocos)

    return json