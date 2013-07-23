#coding: utf8
import serial
baud_rate = 9600
def lerComando(porta):
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