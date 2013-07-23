#coding: utf8
from lerComando import lerComando
from time import sleep
def cadastrarTecla(tecla, porta,listaComando):
        valores = ["v1","v2"]
        while valores[0] != valores [1]: #Cadastrar tecla play/pause
                print ("Pressione o botao do controle que servira como " + tecla)
                valores[0] = lerComando(porta)
                print ("Aguarde")
                sleep(1)
                print ("Pressione novamente")
                valores[1] = lerComando(porta)
                print ("Aguarde")
                sleep(1)
                if valores[0] != valores[1]:
                        print("Leitura errada, cadastre novamente.")
                elif valores[0] in listaComando:#evita o cadastro de mesma tecla pra diferentes funcoes
                        print("Botao ja cadastrado, favor escolha outro botao!")
                        valores[0] = ["v1"]
                        valores[1] = ["v2"]
                else:
                        listaComando.append(valores[0])
        return valores[0]