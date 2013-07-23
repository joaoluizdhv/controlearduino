#! /usr/bin/env python
#coding: utf-8
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
        ui.write(e.EV_KEY, e.ecodes[tecla], 1) #key down
        ui.write(e.EV_KEY, e.ecodes[tecla], 0) #key up
        ui.syn()
        ui.close()

def cadastrarTeclas(porta):
        continuar = True
        opcao = ""
        listaComando = []
        listaTeclas = []
        while (opcao != "1" and opcao != "2" and opcao != "3"):
                opcao = str(raw_input ("Digite 1 para Amarok\nDigite 2 para VLC\nDigite 3 para Apresentação:\n"))
                opcaoPlayer = 0;
                dic = {}
                if opcao == "1":
                        print ("\nAmarok\n")
                        dic = amarok(porta)
                        print dic            
                elif opcao == "2":
                        print ("\nVLC\n")
                        dic = vlc(porta)
                elif opcao == "3":
                        print ("\nApresentação\n")
                        dic = apresentacao(porta)
                else:
                        print("Opcao invalida\n")       
        return dic
 
if __name__ == "__main__":
        print("\n\n####################__Controlando PC via IR e Arduino__####################\n\n")
        print("Programa desenvolvido por João Luiz D. H. Valença")
        print("Estudante da Universidade Federal de Pernambuco(UFPE)")
        print("Licenca GPL v2\n")
        sleep(2)
        porta = escolherPorta()
        if(porta != None):
                dic = cadastrarTeclas(porta)
                print("\n\n#################### Sistema iniciado ####################\n\n");
                while True:
                        comando = lerComando(porta)
                        try:
                                print(dic[comando].split('_')[1])
                                executaAcao(dic[comando])
                        except:
                                print("Botão inválido")