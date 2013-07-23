#coding: utf-8
from cadastrarTecla import cadastrarTecla

def apresentacao(porta):
        listaTeclas = ['KEY_DOWN', 'KEY_UP','KEY_F5', 'KEY_ESC']
        print ("Vamos cadastrar as teclas.")
        print ("Em caso de repetição o sistema irá pedir para que se cadastre uma nova tecla.")
        listaComando = []
        listaComando.append(cadastrarTecla("Passar", porta,listaComando))
        listaComando.append(cadastrarTecla("Voltar", porta,listaComando))
        listaComando.append(cadastrarTecla("Iniciar apresentação", porta,listaComando))
        listaComando.append(cadastrarTecla("Finalizar apresentação", porta,listaComando))
        listaTuplas = {}
        for i in range(len(listaTeclas)):
                listaTuplas.update({listaComando[i*2]:listaTeclas[i]})
        return listaTuplas