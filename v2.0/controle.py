#! /usr/bin/env python
#coding: utf-8
import os.path
from evdev import UInput, ecodes as e
from time import sleep
from escolherPorta import escolherPorta
from lerComando import lerComando
#Módulos de programas
from amarok import amarok
from vlc import vlc
from apresentacao import apresentacao
 
#porta = '/dev/ttyACM1'

baud_rate = 9600
 
def executaAcao(tecla):
        ui = UInput()
        print tecla
        ui.write(e.EV_KEY, e.ecodes[tecla], 1) #key down
        ui.write(e.EV_KEY, e.ecodes[tecla], 0) #key up
        ui.syn()
        ui.close()

def criaDicionarioArquivo(tipo):
        arq = open(tipo+".con", "r")
        conf = arq.readlines()
        dic = {}
        i = 0
        while i < len(conf):
                dic.update({conf[i]:conf[i+1]})
                i+=2
                print i
        return dic

def escolherPrograma(porta):
        continuar = True
        opcao = ""
        listaComando = []
        listaTeclas = []
        tipo = ""
        cadastrou = False
        while (opcao != "1" and opcao != "2" and opcao != "3"):
                opcao = str(raw_input ("Digite 1 para Amarok\nDigite 2 para VLC\nDigite 3 para Apresentação:\n"))
                opcaoPlayer = 0;
                dic = {}
                if opcao == "1":
                        print ("\nAmarok\n")
                        tipo = "Amarok"
                        if (os.path.exists(tipo+".con")) and (raw_input("Já existe configuração pra esse sistema\nSe desejar utilizá-la digite sim:\n") == "sim"):
                                dic = criaDicionarioArquivo(tipo)
                        else:
                                dic = amarok(porta) 
                                cadastrou = True          
                elif opcao == "2":
                        tipo = "VLC"
                        print ("\nVLC\n")
                        if (os.path.exists(tipo+".con")) and (raw_input("Já existe configuração pra esse sistema\nSe desejar utilizá-la digite sim:\n") == "sim"):
                                dic = criaDicionarioArquivo(tipo)
                        else:
                                dic = vlc(porta)
                                cadastrou = True
                elif opcao == "3":
                        tipo = "Apresentacao"
                        print ("\nApresentação\n")
                        if (os.path.exists(tipo+".con")) and (raw_input("Já existe configuração pra esse sistema\nSe desejar utilizá-la digite sim:\n") == "sim"):
                                dic = criaDicionarioArquivo(tipo)
                        else:
                                dic = apresentacao(porta)
                                cadastrou = True
                else:
                        print("Opcao invalida\n")       
        return dic, tipo, cadastrou
 
def salvaConfiguracao(dic,tipo):
        arq = open((tipo + ".con"),"w")
        for con in dic.keys(): 
                parte_dic = str(con) + str(dic[con]) + "\n"
                print parte_dic
                arq.write(parte_dic)
        arq.close()

if __name__ == "__main__":
        print("\n\n####################__Controlando PC via IR e Arduino__####################\n\n")
        print("Programa desenvolvido por João Luiz D. H. Valença")
        print("Estudante da Universidade Federal de Pernambuco(UFPE)")
        print("Licenca GPL v2\n")
        sleep(2)
        porta = escolherPorta()
        if(porta != None):
                dic, tipo, cadastrou = escolherPrograma(porta)
                if(cadastrou):
                        opcao = int(raw_input("Deseja guardar essas configurações:\n0 Sim\n1 Não\n"))
                        while opcao != 1 and opcao != 0:
                                opcao = raw_input("Escolha :\n0 Sim\n1 Não\n")
                        if(opcao == 0):
                                salvaConfiguracao(dic, tipo)
                print("\n\n#################### Sistema iniciado ####################\n\n");
                while True:
                        comando = lerComando(porta)
                        try:
                                executaAcao(dic[comando].split('\r')[0].split('\n')[0])
                        except:
                                print("Botão inválido")