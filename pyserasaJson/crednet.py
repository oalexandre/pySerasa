# -*- coding: utf-8 -*-
from pyserasaJson.erros import BlocoInexistenteError
from pyserasaJson.blocosDados import pendenciasInternas
from pyserasaJson.blocosDados import pendenciasFinanceiras
from pyserasaJson.blocosDados import protestosEstados
from pyserasaJson.blocosDados import chequesSemFundos
from pyserasaJson.blocosDados import covemDevedores
from pyserasaJson.blocosDados import grafias



class Crednet(object):
    def __init__(self):
        self.blocos = []
        self.blocos.append(pendenciasInternas())
        self.blocos.append(pendenciasFinanceiras())
        self.blocos.append(protestosEstados())
        self.blocos.append(chequesSemFundos())
        self.blocos.append(covemDevedores()) 
        self.blocos.append(grafias())
        # self.blocos.append(blocoN500_subtipo00())

    def __getattr__(self, name):
        bloco = ([c for c in self.blocos if c.nome == name] or [None])[0]
        if not bloco:
            print (BlocoInexistenteError().exibirErro(name))
        else:
            if bloco.nome == 'pendenciasInternas':
                print (bloco.nome + "\n")
                for registro in bloco.blocos:
                    for campos in registro.campos.campos:
                        print (campos._nome),
                        print (": "),
                        print (campos._valor)

                    print (" ")
            if bloco.nome == 'pendenciasFinanceiras':
                print (bloco.nome + "\n")
                for registro in bloco.blocos:
                    for campos in registro.campos.campos:
                        print (campos._nome),
                        print (": "),
                        print (campos._valor)

                    print (" ")
            if bloco.nome == 'protestosEstados':
                print (bloco.nome + "\n")
                for registro in bloco.blocos:
                    for campos in registro.campos.campos:
                        print (campos._nome),
                        print (": "),
                        print (campos._valor)

                    print (" ")
            if bloco.nome == 'chequesSemFundos':
                print (bloco.nome + "\n")
                for registro in bloco.blocos:
                    for campos in registro.campos.campos:
                        print (campos._nome),
                        print (": "),
                        print (campos._valor)

                    print (" ")
            else:
                return bloco

    def get_string(self, bloco=None):
        string_retorno = ""
        if bloco is None:
            for bloco in self.blocos:
                if bloco.nome == 'pendenciasInternas':
                    print ("---------> "+ bloco.nome)
                    string_retorno += "Pendencias Internas\n" + "------------" \
                             "-----------------------------------------------\n"
                    for registro in bloco.blocos:
                        for campos in registro.campos.campos:
                            string_retorno += campos._nome + ": " + str(
                                campos._valor) + "\n"
                elif bloco.nome == 'pendenciasFinanceiras':
                    string_retorno += "Pendencias Financeiras\n" + "---------" \
                          "--------------------------------------------------\n"
                    for registro in bloco.blocos:
                        for campos in registro.campos.campos:
                            string_retorno += campos._nome + ": " + str(
                                campos._valor) + "\n"
                elif bloco.nome == 'protestosEstados':
                    string_retorno += "Protestos dos Estados\n" + "---------" \
                          "--------------------------------------------------\n"
                    for registro in bloco.blocos:
                        for campos in registro.campos.campos:
                            string_retorno += campos._nome + ": " + str(
                                campos._valor) + "\n"
                elif bloco.nome == 'chequesSemFundos':
                    string_retorno += "Cheques sem Fundos\n" + "-------------" \
                              "----------------------------------------------\n"
                    for registro in bloco.blocos:
                        for campos in registro.campos.campos:
                            string_retorno += campos._nome + ": " + str(
                                campos._valor) + "\n"
                else:
                    string_retorno += str(bloco.nome_bloco) + "-------------------" \
                                    "----------------------------------------\n"
                    for campo in bloco.campos.campos:
                        string_retorno += campo._nome + ": " + str(
                            campo._valor) + "\n"
        else:
            if bloco.nome == 'pendenciasInternas':
                string_retorno += "Pendencias Internas\n" + "------------" \
                            "-----------------------------------------------\n"
                for registro in bloco.blocos:
                    for campos in registro.campos.campos:
                        string_retorno += campos._nome + ": " + str(
                            campos._valor) + "\n"
                    string_retorno += "\n"
            elif bloco.nome == 'pendenciasFinanceiras':
                string_retorno += "Pendencias Financeiras\n" + "---------" \
                        "--------------------------------------------------\n"
                for registro in bloco.blocos:
                    for campos in registro.campos.campos:
                        string_retorno += campos._nome + ": " + str(
                            campos._valor) + "\n"
                    string_retorno += "\n"
            elif bloco.nome == 'protestosEstados':
                string_retorno += "\nProtestos dos Estados\n" + "--------" \
                        "---------------------------------------------------\n"
                for registro in bloco.blocos:
                    for campos in registro.campos.campos:
                        string_retorno += campos._nome + ": " + str(
                            campos._valor) + "\n"
                string_retorno += "\n"
            elif bloco.nome == 'chequesSemFundos':
                string_retorno += "\nCheques sem Fundos\n" + "-----------" \
                        "------------------------------------------------\n"
                for registro in bloco.blocos:
                    for campos in registro.campos.campos:
                        string_retorno += campos._nome + ": " + str(
                            campos._valor) + "\n"
                string_retorno += "\n"
            # elif bloco is not None:
            #     string_retorno += "\n" + str(bloco.nome_bloco) + "\n----------" \
            #             "-------------------------------------------------\n"
            #     for campo in bloco.campos.campos:
            #         string_retorno += campo._nome + ": " + str(
            #             campo._valor) + "\n"
            #     string_retorno += "\n"
        return string_retorno

    def get_bloco_de_registros(self, nome):

        for bloco in self.blocos:
            if bloco.nome == nome:
                return bloco

        return None
