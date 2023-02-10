from pyserasaJson.stringToJson import stringToJson

#importante, CPF tem que ser passado com 15 caracteres, sendo 4 primeiros 0 e o restante com a sequência normal
cpfs =[
    '000000000001678',
    # "000000000000604",
    # "000000000001244",
    # "000000000002054",
    # "000000000002569",
    # "000000000003379",
    # "000000000004340",
    # "000000000005070",
    # "000000000005665",
    # "000000000007447",
    # "000000000009571",
    # "000000000010901",
    # "000000000013501",
    # "000000000014494",
    # "000000000015970",
    # "000000000017590",
    # "000056017278053",
    # "000035894162890",
    # "000000449448100",
    # "000060656760710",
    # "000000902900706",
    # "000000000028363",
    # "000000000028525",
    # "000000000093181",
    # "000000000699900",
    # "000000000081094",
    # "000000145491820",
    # "000033037426004",
    # "000009544798900",
    # "000029284074304",
    # "000000239941268",
    # "000003670532846",
    # "000007392095153",
    # "000001636227872",
    # "000001109899963",
    # "000001851519734"
]

estado = 'SP'
usuario = '59992836'
senha = 'Pavei@12'
producao = False

#para testes troque a massa de dados no for de CPFs para CNPJs e altere o tipo de pessoa abaixo.
for cpf in cpfs:
    json = stringToJson(cpf, estado, usuario, senha, producao)
    print(json)
    