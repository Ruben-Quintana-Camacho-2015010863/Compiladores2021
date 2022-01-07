from re import U    #matcheo con unicode
import AFN
import Transiciones
import AFD

class Subconjuntos(object):
    def __init__(self, afn):
        self.afn = afn
        self.Destados = {}

    def e_cerradura(self, estados):     #cerradura epsilon
        Tr = self.afn.trancisiones
        cerradura = []
        cerradura.append(estados)   #almacenamos los estados del automara para su analisis
        pila = []
        pila.append(estados)    #una estructura auxiliar
        while len(pila) != 0:
            estado = pila.pop()
            #---------
            for transicion in Tr:
                if transicion.inicio == estado and transicion.simbolo == 'E':
                    if transicion.fin not in cerradura:
                        cerradura.append(transicion.fin)
                        pila.append(transicion.fin)
        return cerradura

    def mover(self, estados, simbolo):   #Trnaisicion
        Tr = self.afn.transiciones
        m = []
        for estado in estados:
            for transicion in Tr:
                if estado == transicion.inicio and transicion.simbolo == simbolo:
                    m.append(transicion.fin)
        return m
    
    def construirSubconjunto(self):
        etiqueta = 65
        seEncuentra = False     #No se me ocurre otro nombre de variable XD
        self.Destados[str(chr(etiqueta))] = (self.e_cerradura(self.afn.inicial))
        self.Destados[str(chr(etiqueta))].sort()
        self.Destados[str(chr(etiqueta))].append(False)
        while not self.analizarMarcados():
            self.Destados[str(chr(etiqueta))][-1] = True    #-1 es de der a izq
            for simbolo in self.afn.alfabeto:
                U = self.e_cerradura(self.mover(self.Destados[str(chr(etiqueta))][:-1], simbolo))
                U.sort()    #u es una var
                for key, val in self.Destados.items():
                    if all(item in U for item in val):
                        seEncuentra = True
                    if not seEncuentra:
                        etiqueta = etiqueta + 1
                        self.Destados[str(chr(etiqueta))] = U
                        self.Destados[str(chr(etiqueta))].append(True)
                        #necesito declarar el afd
                        self.afd.addTransicion(chr(etiqueta-1), chr(etiqueta), simbolo)

        for key, val in self.Destados.items():
            if self.afn.inicial in val[:-1]:
                self.afd.establecerInicial(key)
            for item in self.afn.finales:
                if item in val[:-1]:
                    self.afd.establecerFinal(key)
    
    def analizarMarcados(self):
        marcados = True
        for key, val in self.Destados.items():
            if val[-1] == False:
                marcados = False
        return marcados

    def obtenerAFD(self):
        return self.afd

if __name__ == "__main__":
    autn = AFN.AFN()
    autn.carga("afn.afn")
    autn.cargaTransiciones()
    autn.obtenerInicial()
    autn.obtenerFinal()
    autn.obtenerAlfabeto()
    subconjuntos = Subconjuntos(autn)   #Realizamos el algoritmo dado un AFN
    subconjuntos.construirSubconjunto()
    autd = AFD.AFD()
    autd = subconjuntos.obtenerAFD()
    autd.guardar("afd")


    #Ahora solo falta definir el algoritmo, con ayuda de stackoverflow xd