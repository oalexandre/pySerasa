from pyserasa.parserStringDados import ParserStringDados
from pyserasa.crednet import Crednet

#massa de dados para teste de CNPJ
#importante, cnpj tem que ser passado com 15 caracteres, sendo o primeiro 0 e o restante com a sequência normal
cnpjs =[
"000063960000109",
"069207850000161",
"016854896000106",
"000000202000133",
"000000273000136",
"000000802000100",
"000000998000124",
"016695068000172",
"000000167000152",
"000004559000190",
"000008572000117",
"000019703000161",
"000044222000106",
"000000112000142",
"000008420000114",
"000077144000146",
"000012346000100",
"000033241000137",
"000087181000135",
"000000380000164"
]
#massa de dados para teste de CPF
#importante, CPF tem que ser passado com 15 caracteres, sendo 4 primeiros 0 e o restante com a sequência normal
cpfs =[
"000056017278053",
"000035894162890",
"000000449448100",
"000060656760710",
"000000902900706",
"000000000028363",
"000000000028525",
"000000000093181",
"000000000699900",
"000000000081094",
"000000145491820",
"000033037426004",
"000009544798900",
"000029284074304",
"000000239941268",
"000003670532846",
"000007392095153",
"000001636227872",
"000001109899963",
"000001851519734"
]

#para testes troque a massa de dados no for de CPFs para CNPJs e altere o tipo de pessoa abaixo.
for doc in cnpjs:
    a = ParserStringDados()
    crednet = Crednet()

    #F para fisica e J para juridica
    tipo_pessoa = 'J'
    #estado
    estado = 'SP'
    #usuario com 8 caracteres
    usuario = ''
    #senha com 8 caracteres
    senha = ''
    #cnpj do consultante com 14 caracteres
    cnpj_consultante = '06217362000180'
    #True para produção, False para homologação
    producao = False

    #gera URL de consulta
    dados = a.gerar_string_envio(doc, tipo_pessoa, cnpj_consultante, estado, usuario, senha, producao)
    
    #realzia consulta na URL do SERASA
    response = a.realizar_busca_serasa(dados)
    #constroi o objeto com os dados retornados conm base na crasse Crednet
    parseString = a.parser_string_dados_retorno(response, crednet)

    #imprime em tela os resultados, em c
    # aso de implantação em sistemas pode-se salvad os dados retornados em variáveis para uso em regras de negócio.
    print ('###### Documento consultado ' + tipo_pessoa + ': '+doc+'       ###### \n')

    for i in parseString.blocos:
        stringRetorno = parseString.get_string(i)
        if stringRetorno != "":
            print (stringRetorno)

    print ('######                FIM DA CONSULTA                ###### \n')
    print ('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ \n')
