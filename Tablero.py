from Ficha import *

class Tablero:
    #Defina aquí los atributos de Tablero
    NCasillas = 0
    Ficha1 = 0
    Ficha2 = 0
    Ficha3 = 0
    Ficha4 = 0

    #también va a necesitar una lista de Fichas (puede asumir un número de Fichas fijo si le parece más fácil), 
    #y un mecanismo para saber quién sigue en el turno


    #agregue parámetros necesarios después de self
    #para iniciar los valores de sus atributos
    def __init__(self, NCasillas):
        self.NCasillas = NCasillas
        self.Ficha1 = Ficha("rojo")
        self.Ficha2 = Ficha("azul")
        self.Ficha3 = Ficha("verde")
        self.Ficha4 = Ficha("amarillo")
        #inicialice aquí todos los atributos
        #no olvide usar self.atributo para acceder el atributo de la clase

    def turno(self):
        i = 0
        while(i <= 20):
            print("\nSiguiente turno la ficha", self.Ficha1.color)
            self.Ficha1.avanzar()
            i = self.Ficha1.posicion
            print("\nSiguiente turno la ficha", self.Ficha2.color)
            self.Ficha2.avanzar()
            i = self.Ficha2.posicion
            print("\nSiguiente turno la ficha", self.Ficha3.color)
            self.Ficha3.avanzar()
            i = self.Ficha3.posicion
            print("\nSiguiente turno la ficha", self.Ficha4.color)
            self.Ficha4.avanzar()
            i = self.Ficha4.posicion
        print("\nSe acabo el juego, una ficha llego al final")
    #defina aquí los métodos de Tablero
    #recuerde que el primer parámetro de cada método es siempre self
