# 1- Leer de un archivo separado por comas los datos para crear instancias de la clase ViajeroFrecuente, y almacenarlas en una lista.
# 2- Lea por teclado un número de viajero frecuente y presente un menú con las siguientes opciones:
# a- Consultar Cantidad de Millas.
# b- Acumular Millas.
# c- Canjear Millas.
# 3- Represente el almacenamiento en memoria para la lista cargada con 4 viajeros.

from claseViajero import viajFrec as vf
from manejadorViajero import menu as menuViajero
import csv 
import os


def opc1 (listaViaj):
    total = 0
    path = './viajFrec.csv'
    archivo = open(path, "r")
    reader = csv.reader(archivo, delimiter=',')
    for fila in reader:
        numViaj = fila [0]
        dni = fila [1]
        nom = fila [2]
        ape = fila [3]
        millAcum = fila [4]
        viajero = vf (numViaj, dni, nom, ape, millAcum)
        listaViaj.append(viajero)
        total = total + 1
    archivo.close()
    if total > 0:
        print ('lista cargada correctamente')
    os.system('pause')
    return listaViaj
    

    
def opc2 (listaViajero):
    nViaj = int (input ('ingrese numero del Viajero: '))
    menuViajero(nViaj, listaViajero)
    

def opc3 ():
    print ('opc 3')

def salir():
    print ('saliendo...')
    os.system ('pause')
    os.system('exit')

def menu(listaViajero):
    os.system('cls')
    op = int (input ('''
    -------->Menu<--------
    Seleccione una opcion:
    1. Item 1: Leer archivo y crear lista
    2. Item 2: Ingresar numero de viajero y canjear millas
    3. Item 3: 
    0. Salir

    Su opcion: '''))

    if op == 1:
        listaViajero = opc1(listaViaj)
        menu(listaViajero)
    elif op == 2:
        opc2(listaViaj)
    elif op == 3:
        opc3()
    else:
        salir()

if __name__ == '__main__':
    listaViaj = []
    menu (listaViaj)


    
