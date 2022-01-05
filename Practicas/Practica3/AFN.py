import re
import os

class AFN(object):
    def __init__(self):
        self.inicial = 0
        self.finales = []
        self.alfabeto = []
        self.linea = ""

    def carga(self,fname):  #abrimos/creamos el archivo
        f = open(fname, encoding='utf-8')
        self.linea= f.read()    #Leemos el archivo y guardamos en linea
        f.close()

    def obtenerAlfabeto(self):
        simbolos = []
        for linea in self.linea.splitlines():
            simbolo = ""
            if re.match(r"(\d+)->(\d+),([a-zE])", linea):   #intentamos hacer match
                res = re.match(r"(\d+)->(\d+), ([a-zE])", linea)
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