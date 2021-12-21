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
        
        #Por ultimo validamos cadena
        automataFinal.append(self.obtenerCerraduraEstrella(cadena))#Evaluamos la cerradura *

    def obtenerCerraduraEstrella(self, cadena):
        automata = []
        expresionNormal = []
        expresionParentesis = []
        listaCompleta = []
        expresionNormal = re.findall("\w\*", cadena)
        expresionParentesis = re.findall("\(\w+\)\*", cadena)
        listaCompleta = listaCompleta + expresionNormal
        listaCompleta = listaCompleta + expresionParentesis
        automata.append(self.plantillaEstrella(listaCompleta))
        return automata

    def plantillaEstrella(self, Lista):
        automatas = []
        for item in Lista:
            item = item.replace("*", "")
            cont1 = 1
            cont2 = 2
            if len(item) == 1:
                nuevaLista = [] #Otra lista como aux XD
                # Agregamos las tranciciones que ocurren de un estado a otro, imprimiendo el trazado
                nuevaLista.append("Estado" + str(cont1) + " -> Estado" + str(cont2) + " ,E")
                nuevaLista.append("Estado" + str(cont1) + " -> Estado" + str(cont2+2) + " ,E")
                nuevaLista.append("Estado" + str(cont1+1) + " -> Estado" + str(cont2+1) + " ," + item)
                nuevaLista.append("Estado" + str(cont1+2) + " -> Estado" + str(cont2) + " ,E")
                nuevaLista.append("Estado" + str(cont1+2) + " -> Estado" + str(cont2+2) + " ,E")
                automatas.append(nuevaLista)
            if len(item) > 1:
                nuevaLista = []
                item = item.replace("(", "")
                item = item.replace(")", "")
                nuevaLista.append("Estado" + str(cont1) + " -> Estado" + str(cont2) + " ,E")
                nuevaLista.append("Estado" + str(cont1) + " -> Estado" + str(cont2 + 1 + len(item)) + " ,E")
                n = 1
                for letra in item:
                    nuevaLista.append("Estado" + str(cont1 + n) +  " -> Estado" + str(cont2 + n) + " ," + letra)
                    n = n + 1
                nuevaLista.append("Estado" + str(cont1 + 1 + len(item)) + " -> Estado" + str(cont2) + " ,E")
                nuevaLista.append("Estado" + str(cont1 + 1 + len(item)) + " -> Estado" + str(cont2 + 1 + len(item)) + " ,E")
                automatas.append(nuevaLista)
        return automatas

automata = Thompson()
automata.convertir("a*")