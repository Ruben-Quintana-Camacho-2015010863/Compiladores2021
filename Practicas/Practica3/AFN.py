import re
import os       #Para el manejo de archivos
import Transiciones

class AFN(object):
    def __init__(self):
        self.inicial = 0
        self.finales = []
        self.transiciones = []
        self.alfabeto = []
        self.linea = ""

    def carga(self,fname):  #abrimos/creamos el archivo
        f = open(fname, encoding='utf-8')
        self.linea = f.read()    #Leemos el archivo y guardamos en linea
        f.close()

    def obtenerAlfabeto(self):
        simbolos = []
        for line in self.linea.splitlines():
            simbolo = ""
            if re.match(r"(\d+)->(\d+),([a-zE])", line):   #intentamos hacer match
                res = re.match(r"(\d+)->(\d+), ([a-zE])", line)
                simbolo = res.group(3)
                simbolos.append(simbolo)
        simbolos = list(dict.fromkeys(simbolos))
        simbolos.remove('E')
        self.alfabeto = simbolos

    def listString(self,s):
        str1 = ""
        for ele in s:   #element xd
            str1 = str1 + " " + str(ele)
        return str1
    
    def guardar(self,fname):
        self.linea = "inicial:{}\nfinales:{}".format(self.inicial, self.listString(self.finales))
        #necesito las transiciones
        for tr in self.transiciones:
            atr = tr.obtenerAtributos()
            self.linea += "\n{}->{},{}".format(atr[0], atr[1], atr[2])
        f = open(fname + ".afn", 'w', encoding='utf-8')
        f.write(self.linea)
        f.close()

    def cargaTransiciones(self):
        for line in self.linea.splitlines():
            inicio = 0
            fin = 0
            simbolo = ""
            if re.match(r"(\d+)->(\d+),([a-zE])", line):
                res = re.match(r"(\d+)->(\d+),([a-ZE])", line)
                inicio = int(res.group(1))
                fin = int(res.group(2))
                simbolo= res.group(3)
                tr = Transiciones.Transicion(inicio, fin, simbolo)
                self.transiciones.append(tr)
    
    def addTransicion(self, inicio, fin, simbolo):  #Agregar transicion
        tr = Transiciones.Transicion(inicio, fin, simbolo)
        self.transiciones.append(tr)

    def rmTransicion(self, inicio, fin, simbolo):   #Eliminar transicionn
        tr = Transiciones.Transicion(inicio, fin, simbolo)
        indice = 0
        for transicion in self.transiciones:
            if transicion.igual(tr):
                self.transiciones.pop(indice)
                return
            indice = indice + 1

    def obtenerInicial(self):
        lineas = self.linea.splitlines()
        ini_str = re.match(r"([a-zA-z]+):(\d+)", lineas[0])
        self.inicial = int(ini_str.group(2))

    def obtenerFinal(self):
        lineas = self.linea.splitlines()
        ini_str = re.match(r"([a-zA-z]+):(\s*\d+)+", lineas[1])
        finales = ini_str.group(2).split(" ")
        for final in finales:
            self.finales.append(int(final))

    def establecerInicial(self, inicial):
        self.inicial = inicial

    def establecerFinal(self, final):
        self.finales.append(final)

    #Metodos de evaluacion
    def esAFN(self):
        for transicion in self.transiciones:
            if transicion.obtenerAtributos()[2] == 'E':
                return True
        return False

    def esAFD(self):
        for transicion in self.transiciones:
            if transicion.obtenerAtributos()[2] == 'E':
                return False
        return True

'''
Pruebas 

if __name__ == "__main__":
    autn = AFN()
    autn.cargar("afn.afn")
    autn.cargaTransiciones()
    autn.addTransicion(2,3,'E')
    autn.rmTransicion(11,11,'b')
    autn.obtenerInicial()
    autn.obtenerFinal()
    autn.establecerInicial(4)
    autn.establecerFinal(8)
    autn.guardar("afn2")
    
'''