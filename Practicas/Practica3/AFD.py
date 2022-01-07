import re
import Transiciones

class AFD(object):
    def __init__(self):
        self.inicial = ""
        self.finales = []
        self.transiciones = []
        self.linea = ""
        
    def cargar(self, fname):
        f = open(fname, encoding='utf-8')
        self.linea = f.read()
        f.close()

    def list_str(self, s):
        str1 = ""
        for ele in s:
            str1 = str1 + " " + str(ele)
        return str1
    
    def guardar(self, fname):    #Escribimos el resultado en el archivo
        self.linea = "Inicial:{}\nfinales:{}".format(self.inicial, self.list_str(self.finales))
        for tr in self.transiciones:
            atr = tr.obtenerAtributos()
            self.linea += "\n{}->{},{}".format(atr[0], atr[1], atr[2])
        f = open(fname + ".afd", 'w', encoding='utf-8')
        f.write(self.linea)
        f.close()

    def obtenerLenguaje(self):
        simbolos = []
        for line in self.linea.splitlines():
            simbolo = ""
            if re.match(r"(\d+)->(\d+),([a-zE])", line):
                res = re.match(r"(\d+)->(\d+),([a-zE])", line)
                simbolo = res.group(3)
                simbolos.append(simbolo)
        simbolos = list(dict.fromkeys(simbolos)) #{}
        print(simbolos)

    def cargarTransiciones(self):
        for line in self.linea.splitlines():
            inicio = 0
            fin = 0
            simbolo = ""
            if re.match(r"([A-Z]?)->([A-Z]?),([a-z])", line):
                res = re.match(r"([A-Z]?)->([A-Z]?),([a-z])", line)
                inicio = res.group(1)
                fin = res.group(2)
                simbolo = res.group(3)
                tr = Transiciones.Transicion(inicio, fin, simbolo)
                self.transiciones.append(tr)
            
    def addTransicion(self, inicio, fin, simbolo):
        tr = Transiciones.Transicion(inicio, fin, simbolo)
        self.transiciones.append(tr)

    def rmTransicion(self, inicio, fin, simbolo):
        tr = Transiciones.Transicion(inicio, fin, simbolo)
        indice = 0
        for transicion in self.transiciones:
            if(transicion.igual(tr)):
                self.transiciones.pop(indice)
                return
            indice = indice + 1

    
