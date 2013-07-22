#! /usr/bin/env python
from evdev import UInput, ecodes as e
import serial
from time import sleep
 
 
porta = '/dev/ttyACM1'
#porta = '/dev/tty.usbserial'
baud_rate = 9600
 
def lerComando():
        try:
                arduino = serial.Serial(porta, baud_rate)
                valor = ""
                while (valor == ""):
                        valor = arduino.readline()
                arduino.close()
                return valor
        except serial.SerialException:
                print("Erro!!\nVerifique se o Arduino encontra-se conectado ao PC.")
                return ""
 
def executaAcao(tecla):
        ui = UInput()
        ui.write(e.EV_KEY, e.ecodes[tecla], 1)  # KEY_A down
        #print("olha a teclaa: "+tecla)
        ui.write(e.EV_KEY, e.ecodes[tecla], 0)
        ui.syn()
       
        ui.close()
 
def cadastrarTeclas():
        continuar = True
        opcao = ""
        listaComando = []
        listaTeclas = []
        while (opcao != "1" and opcao != "2"):
                opcao = str(raw_input ("Digite 1 para player Amarok\nDigite 2 para apresentacao\n"))
                opcaoPlayer = 0;
               
                #Futuramente da suporte a mais players
                #while (opcaoPlayer <= 0 or opcaoPlayer > 1):
                #       opcaoPlayer = str(raw_input ("Digite 1 para Amarok\nDigite 2 para \n"))
               
                if opcao == "1":
                        listaTeclas.append('KEY_PLAYPAUSE')
                        listaTeclas.append('KEY_NEXTSONG')
                        listaTeclas.append('KEY_PREVIOUSSONG')
                        listaTeclas.append('KEY_MUTE')
                        listaTeclas.append('KEY_VOLUMEDOWN')
                        listaTeclas.append('KEY_VOLUMEUP')
                       
                                               
                        print ("Vamos cadastrar as teclas para player/pause.\nEm caso de repeticao o sistema ira pedir para que se cadastre uma nova tecla!")
                        #cadastro da tecla player/pause
                        valor1 = ""
                        valor2 = " "
                        while valor1 != valor2:
                                print ("Pressione o botao do controle que servira como play >/||")
                                valor1 = lerComando()
                                sleep(1)
                                print ("Pressione novamente")
                                valor2 = lerComando()
                                sleep(1)
                                if valor1 != valor2:
                                        print("Leitura errada, cadastre novamente.")
                                elif valor1 in listaComando:
                                        print("Botao ja cadastrado, favor escolha outro botao!")
                                        valor1 = ""
                                        valor2 = " "
                                else:
                                        listaComando.append(valor1)
                                        print("Tecla play/pause cadastrada")
                       
                        #cadastro da tecla next
                        valor1 = ""
                        valor2 = " "
                        while valor1 != valor2:
                                print ("Pressione o botao do controle que servira como next >>|")
                                valor1 = lerComando()
                                sleep(1)
                                print ("Pressione novamente")
                                valor2 = lerComando()
                                sleep(1)
                                if valor1 != valor2:
                                        print("Leitura errada, cadastre novamente.")
                                elif valor1 in listaComando:
                                        print("Botao ja cadastrado, favor escolha outro botao!")
                                        valor1 = ""
                                        valor2 = " "
                                else:
                                        listaComando.append(valor1)
                                        print("Tecla next cadastrada")
                        #cadastro da tecla PREVIOUS
                        valor1 = ""
                        valor2 = " "
                        while valor1 != valor2:
                                print ("Pressione o botao do controle que servira como previous |<<")
                                valor1 = lerComando()
                                sleep(1)
                                print ("Pressione novamente")
                                valor2 = lerComando()
                                sleep(1)
                                if valor1 != valor2:
                                        print("Leitura errada, cadastre novamente.")
                                elif valor1 in listaComando:
                                        print("Botao ja cadastrado, favor escolha outro botao!")
                                        valor1 = ""
                                        valor2 = " "
                                else:
                                        listaComando.append(valor1)
                                        print("Tecla previous cadastrada")
                       
                        #cadastro da tecla mute
                        valor1 = ""
                        valor2 = " "
                        while valor1 != valor2:
                                print ("Pressione o botao do controle que servira como mute")
                                valor1 = lerComando()
                                sleep(1)
                                print ("Pressione novamente")
                                valor2 = lerComando()
                                sleep(1)
                                if valor1 != valor2:
                                        print("Leitura errada, cadastre novamente.")
                                elif valor1 in listaComando:
                                        print("Botao ja cadastrado, favor escolha outro botao!")
                                        valor1 = ""
                                        valor2 = " "
                                else:
                                        listaComando.append(valor1)
                                        print("Tecla mute cadastrada")
                       
                        #cadastro da tecla diminui som
                        valor1 = ""
                        valor2 = " "
                        while valor1 != valor2:
                                print ("Pressione o botao do controle que servira como diminui som")
                                valor1 = lerComando()
                                sleep(1)
                                print ("Pressione novamente")
                                valor2 = lerComando()
                                sleep(1)
                                if valor1 != valor2:
                                        print("Leitura errada, cadastre novamente.")
                                elif valor1 in listaComando:
                                        print("Botao ja cadastrado, favor escolha outro botao!")
                                        valor1 = ""
                                        valor2 = " "
                                else:
                                        listaComando.append(valor1)
                                        print("Tecla diminui som cadastrada")  
                       
                       
                        #cadastro da tecla aumenta som
                        valor1 = ""
                        valor2 = " "
                        while valor1 != valor2:
                                print ("Pressione o botao do controle que servira como aumenta som")
                                valor1 = lerComando()
                                sleep(1)
                                print ("Pressione novamente")
                                valor2 = lerComando()
                                sleep(1)
                                if valor1 != valor2:
                                        print("Leitura errada, cadastre novamente.")
                                elif valor1 in listaComando:
                                        print("Botao ja cadastrado, favor escolha outro botao!")
                                        valor1 = ""
                                        valor2 = " "
                                else:
                                        listaComando.append(valor1)
                                        print("Tecla aumenta som cadastrada")                  
                       
                elif opcao == "2":
                        valor1 = ""
                        valor2 = " "
                        listaTeclas.append('KEY_ENTER')
                        listaTeclas.append('KEY_BACKSPACE')
                        print ("Vamos cadastrar as teclas para apresentacao.\nEm caso de repeticao o sistema de cadastro ira reiniciar!")
                        #cadastro da tecla avancar slide
                        while valor1 != valor2:
                                print ("Pressione o botao do controle que servira como avancar slide")
                                valor1 = lerComando()
                                sleep(1)
                                print ("Pressione novamente")
                                valor2 = lerComando()
                                sleep(1)
                                if valor1 != valor2:
                                        print("Leitura errada, cadastre novamente.")
                                else:
                                        listaComando.append(valor1)
                                        print("Tecla avancar slide cadastrada")
                        #cadastro da tecla voltar slide
                        valor1 = ""
                        valor2 = " "
                        while valor1 != valor2:
                                print ("Pressione o botao do controle que servira como voltar slide")
                                valor1 = lerComando()
                                sleep(1)
                                print ("Pressione novamente")
                                valor2 = lerComando()
                                sleep(1)
                                if valor1 != valor2:
                                        print("Leitura errada, cadastre novamente.")
                                else:
                                        listaComando.append(valor1)
                                        print("Tecla voltar slide cadastrada")
                else:
                        print("Opcao invalida\n")
                       
        return listaComando, listaTeclas
 
 
if __name__ == "__main__":
        print("\n\n\n\n####################__Controlando PC via IR e Arduino__####################\n\n")
        print("Programa desenvolvido por Joao Luiz D. H. Valenca")
        print("Estudante da Universidade Federal de Pernambuco(UFPE)\n")
        sleep(5)
        botoes, teclas = cadastrarTeclas();
        print("\n\n#################### Sistema iniciado ####################\n\n");
        while True:
                comando = lerComando()
                try:
                        print(teclas[botoes.index(comando)])
                        executaAcao(teclas[botoes.index(comando)])
                except:
                        print("Botao invalido")