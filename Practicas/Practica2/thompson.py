import string
import re   #Regular Expresion

class Thompson:
    def convertir(self, cadena):
        cadena = cadena     #Seteamos cadena
        automataFinal = []  #Array que almacenara los estados
        abecedario = string.ascii_lowercase     #Abecedario nos ayudara a matchear la cadena
        error = False       #Declaramos una variable bool
        lenguaje = []
        operaores = ["+", "|", "*"] #Operadores que acepta la construccion de thompson
        lenguaje = lenguaje + operaores
        for item in abecedario:
            lenguaje.append(item)   #Obtenemos el abecedario en minusculas porque es lo primero que evaluamos en la cadena
        #Validamos si la cadena ingresada es permitida por el lenguaje
        for item in cadena:
            if item not in lenguaje:
                error = True
            else:
                error = False
        if(error == True):
            print("Cadena invalida, ingresa otra cadena")

automata = Thompson()
automata.convertir("a")