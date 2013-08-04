#coding: utf8
########
from cadastrarTecla import cadastrarTecla

def amarok(porta):
        listaTeclas = ['KEY_PLAYPAUSE',
        'KEY_NEXTSONG',
        'KEY_PREVIOUSSONG',
        'KEY_MUTE',
        'KEY_VOLUMEDOWN',
        'KEY_VOLUMEUP']
        print ("Vamos cadastrar as teclas.")
        print ("Em caso de repetição o sistema irá pedir para que se cadastre uma nova tecla.")
        listaComando = []
        listaComando.append(cadastrarTecla("Play/Pause", porta,listaComando))
        listaComando.append(cadastrarTecla("Next",porta,listaComando))
        listaComando.append(cadastrarTecla("Previous",porta,listaComando))
        listaComando.append(cadastrarTecla("Mute",porta,listaComando))
        listaComando.append(cadastrarTecla("Diminui Som",porta,listaComando))
        listaComando.append(cadastrarTecla("Aumenta Som",porta,listaComando))
        listaTuplas = {}
        for i in range(len(listaTeclas)):
                listaTuplas.update({listaComando[i*2]:listaTeclas[i]})
        return listaTuplas