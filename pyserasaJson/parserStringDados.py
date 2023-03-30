# -*- coding: utf-8 -*-
import re
import requests
from pyserasaJson.blocosDados import *
import importlib


class ParserStringDados(object):
    def gerar_string_envio(self, cpf, uf_cliente, login, senha, producao):
        dados =""
        url=""
        if producao:
            url = 'https://sitenet43-2.serasa.com.br/Prod/consultahttps?p='
        else:
            url = 'https://mqlinuxext-2.serasa.com.br/Homologa/consultahttps?p='

        dados = url + login+senha+'        B49C      '+cpf+'FC     FI0001000000000000000N99SINIAN                                            N                       S                                                                                                                                                                                                                                                                             P002RE02                     REHMHSPN                                                                              N00100PPX21P 0                                                                                                     N00300                     '+uf_cliente+'                                                                                      T999'

        return dados

    def realizar_busca_serasa(self, dados):
        request = requests.post(dados, verify=True)

        return request.text

    def montar_bloco(self, bloco, arquivo):
        nome = bloco[0:4]
        nome_classe = "bloco"+nome
        if bloco[0:4] != u'B49C' and bloco[0:4] != u'T999' \
                and bloco[0:4] != u'P002' and bloco[0:4] != u'N001' \
                and bloco[0:4] != u'N003' and bloco[0:4] != u'A900' \
                and bloco[0:4] != u'I105':
            nome_classe = nome_classe + "_subtipo" + bloco[4:6]
        # mod_serializer = __import__('pyserasa.blocosDados', globals(), locals())
        # if(nome_classe == 'blocoB49C'):
        #     bloco_montado = blocoB49C(nome, bloco)
        # func = getattr(mod_serializer, nome_classe)
        # if nome_classe == 'blocoP001_subtipo01' or nome_classe == 'blocoI001_subtipo07' or nome_classe == 'blocoI002_subtipo95' or nome_classe == 'blocoI003_subtipo53' or nome_classe == 'blocoB901_subtipo10' or nome_classe == 'blocoI002_subtipo92' or nome_classe == "blocoB916_subtipo20"  or nome_classe == "blocoI060_subtipo00": 
        #     return arquivo
        
        try:
            func = eval(nome_classe)
            bloco_montado = func(nome, bloco)
            
            if nome == 'N230':
                arquivo.blocos[0].blocos.append(bloco_montado)
            elif nome in ['N240', 'I140', 'I220']:
                arquivo.blocos[1].blocos.append(bloco_montado)
            elif nome in ['N250', 'I110']:
                arquivo.blocos[2].blocos.append(bloco_montado)
            elif nome == 'N270':
                arquivo.blocos[3].blocos.append(bloco_montado)
            elif nome == 'I230':
                arquivo.blocos[4].blocos.append(bloco_montado)
            elif nome == 'I105':
                arquivo.blocos[5].blocos.append(bloco_montado)
            else:
                arquivo.blocos.append(bloco_montado)

            return arquivo
        except:
            return arquivo


        

    def parser_string_dados_retorno(self, string_dados_retorno, arquivo):
        string_dados_retorno = string_dados_retorno[
                               0:len(string_dados_retorno)-2] + 'T999'
        vetor_string_dados = re.findall(
            "([B,P,N,I,A]\d{2}.*?)(?=(?!I000)(?!P000)[B,P,N,I][0-9][0-9][0-9]|A900|T999)", string_dados_retorno)

        arquivo_crednet = self.montar_objeto_crednet(
            vetor_string_dados, arquivo)

        return arquivo_crednet

    def montar_objeto_crednet(self, vetor_string_dados, arquivo):

        for bloco in vetor_string_dados:
            arquivo = self.montar_bloco(bloco, arquivo)

        return arquivo
