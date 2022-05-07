# Métodos:
# a- El constructor.
# b- “cantidadTotaldeMillas”, retorna la cantidad de millas acumuladas.
# c- “acumularMillas”, recibe como parámetro la cantidad de millas recorridas, las suma en el atributo correspondiente y retorna el valor del atributo actualizado.
# d- “canjearMillas”, recibe como parámetro la cantidad de millas a canjear. Para utilizar las millas debe verificarse que la cantidad a canjear sea menor o igual a la cantidad de millas acumuladas, caso contrario mostrar un mensaje de error en la operación. Retorna el valor de la cantidad de millas acumuladas.


class viajFrec:
    __numViaj = str,
    __dni = int,
    __nom = str,
    __ape = str,
    __millAcum = int

    def __init__(self, numViaj=None, dni=None, nom=None, ape=None, millAcum=None):
        self.__numViaj = numViaj
        self.__dni = dni
        self.__nom = nom
        self.__ape = ape
        self.__millAcum = millAcum

    def cantTotalMillas (self):
        return self.__millAcum
    
    def acumularMillas(self, xMillas):
        self.__millAcum += xMillas
        return self.__millAcum
    
    def canjearMillas (self, millasCanjear):
        if millasCanjear <= self.__millAcum:
            self.__millAcum -= millasCanjear
            return self.__millAcum
        else:
            print ('Error en la operación, cantidad de millas insuficientes')

    def buscarViajero (listaViajero, xNum):
        return