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
        automataFinal.append(self.cerraduraEstrella(cadena)) #Evaluamos la cerradura *
        automataFinal.append(self.cerraduraPositiva(cadena)) #Evaluamos la cerradura +
        print(automataFinal)    #Por ultimo mandamos a imprimir las tranciciones de las plantillas, por lo que finaliza el programa

    def cerraduraEstrella(self, cadena):
        automata = []
        expresionNormal = []
        expresionParentesis = []
        listaCompleta = []
        expresionNormal = re.findall("\w\*", cadena)    #Hacemos match con *
        expresionParentesis = re.findall("\(\w+\)\*", cadena)
        listaCompleta = listaCompleta + expresionNormal
        listaCompleta = listaCompleta + expresionParentesis
        automata.append(self.plantillaEstrella(listaCompleta))
        return automata

    def plantillaEstrella(self, Lista): #Plantilla porque es el formato 
        automatas = []
        for item in Lista:
            item = item.replace("*", "")
            cont1 = 1
            cont2 = 2
            if len(item) == 1:
                nuevaLista = [] #Otra lista como aux XD
                # Agregamos las tranciciones que ocurren de un estado a otro, imprimiendo el trazado
                nuevaLista.append("Estado" + str(cont1) + " -> Estado" + str(cont2) + ",E")
                nuevaLista.append("Estado" + str(cont1) + " -> Estado" + str(cont2+2) + ",E")
                nuevaLista.append("Estado" + str(cont1+1) + " -> Estado" + str(cont2+1) + "," + item)
                nuevaLista.append("Estado" + str(cont1+2) + " -> Estado" + str(cont2) + ",E")
                nuevaLista.append("Estado" + str(cont1+2) + " -> Estado" + str(cont2+2) + ",E")
                automatas.append(nuevaLista)
            if len(item) > 1:
                nuevaLista = []
                item = item.replace("(", "")
                item = item.replace(")", "")
                nuevaLista.append("Estado" + str(cont1) + " -> Estado" + str(cont2) + ",E")
                nuevaLista.append("Estado" + str(cont1) + " -> Estado" + str(cont2 + 1 + len(item)) + ",E")
                n = 1
                for letra in item:
                    nuevaLista.append("Estado" + str(cont1 + n) +  " -> Estado" + str(cont2 + n) + "," + letra)
                    n = n + 1
                nuevaLista.append("Estado" + str(cont1 + 1 + len(item)) + " -> Estado" + str(cont2) + ",E")
                nuevaLista.append("Estado" + str(cont1 + 1 + len(item)) + " -> Estado" + str(cont2 + 1 + len(item)) + ",E")
                automatas.append(nuevaLista)
        return automatas

    def cerraduraPositiva(self, cadena):
        automata = []
        listaCompleta = []
        expresionNormal = []
        expresionParentesis = []
        expresionNormal = re.findall("\w\+", cadena)    #Hacemos match con +
        expresionParentesis = re.findall("\(\w+\)\+", cadena)
        listaCompleta = listaCompleta + expresionNormal
        listaCompleta = listaCompleta + expresionParentesis
        automata.append(self.plantillaPositiva(listaCompleta))
        return automata

    def plantillaPositiva(self, Lista):
        automatas = []
        for item in Lista:
            item = item.replace("+", "")
            cont1 = 1
            cont2 = 2
            if len(item) == 1:
                nuevaLista = []     #Otra lista como aux para este bloque xd
                nuevaLista.append("Estado" + str(cont1) + " -> Estado" + str(cont2) + "," + item)
                nuevaLista.append("Estado" + str(cont1 + 1) + " -> Estado" + str(cont2 + 1) + ",E")
                nuevaLista.append("Estado" + str(cont1 + 1) + " -> Estado" + str(cont2 + 3) + ",E")
                nuevaLista.append("Estado" + str(cont1 + 2) + " -> Estado" + str(cont2 + 2) + "," + item)
                nuevaLista.append("Estado" + str(cont1 + 3) + " -> Estado" + str(cont2 + 1) + ",E")
                nuevaLista.append("Estado" + str(cont1 + 3) + " -> Estado" + str(cont2 + 1) + ",E")
                automatas.append(nuevaLista)
            if len(item) > 1:
                nuevaLista = []
                item = item.replace("(", "")
                item = item.replace(")", "")
                n = 1
                cont1 = 1 + len(item)
                cont2 = 2 + len(item)
                for letra in item:
                    nuevaLista.append("Estado" + str(n) + " -> Estado" + str(n + 1) + "," + letra)
                    n = n +1
                nuevaLista.append("Estado" + str(cont1) + " -> Estado" + str(cont2) + ",E")
                nuevaLista.append("Estado" + str(cont1) + " -> Estado" + str(cont2 + 1 + len(item)) + ",E")
                for letra in item:
                    nuevaLista.append("Estado" + str(n + 1) + " -> Estado" + str(n + 2) + "," + item)
                    n = n + 1
                nuevaLista.append("Estado" + str(cont1 + len(item) + 1) + " -> Estado" + str(cont2 + len(item) + 1) + ",E")
                nuevaLista.append("Estado" + str(cont1 + len(item) + 1) + " -> Estado" + str(cont2 + len(item) - 4) + ",E")
                automatas.append(nuevaLista)
        return automatas


automata = Thompson()
automata.convertir("a+b+c*")