import os.path
def escolherPorta():
        lista = []
        for i in range(30):
                nameFile = '/dev/ttyACM'+str(i)
                if (os.path.exists(nameFile)):
                        lista.append(nameFile)
        portaFinal = -1
        if(len(lista) == 0):
                print ("Erro!!\nVerifique se o Arduino encontra-se conectado ao PC.")
        else:
                while (portaFinal < 0 or portaFinal >= (len(lista))):
                        print("Escolha uma porta:")
                        for i in range(len(lista)):
                                print (str(i)+"-> "+ lista[i])
                        portaFinal = int(raw_input())
                return lista[portaFinal]