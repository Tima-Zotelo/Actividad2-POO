import os
from claseViajero import viajFrec

def menu (nv, listaViajero):
    os.system('cls')
    op = int( input ('''
    --------> Menu de Viajero <--------
    
    Elija su opcion:
    1. Consultar cantidad de millas acumuladas
    2. Acumular Millas
    3. Canjear Millas
    Su opcion: '''))
    if op == 1:
        opc1(listaViajero)
    elif op == 2:
        opc2(listaViajero)
    elif op == 3:
        opc3(listaViajero)
    else:
        salir(op)

def opc1 (listaViajero):
    nViaj = int (input('Ingrese numero de viajero'))
    viajFrec.buscarViajero (listaViajero, nViaj)
    

def opc2 (listaViajero):
    return

def opc3 (listaViajero):
    return

    

