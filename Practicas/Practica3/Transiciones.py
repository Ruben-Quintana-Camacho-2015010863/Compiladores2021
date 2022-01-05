class Transicion(object):
    def __init__(self, inicio, fin, simbolo):
        self.inicio = inicio    #Marcamos el inicio y final del automata
        self.fin = fin          
        self.simbolo = simbolo  #Simbolo de transicion

    def obtenerAtributos(self):
        return self.inicio, self.fin, self.simbolo
    
    def igual(self, tr):    #Metodo equal en la practica1
        return True if (self.inicio == tr.inicio and self.fin == tr.fin and self.simbolo == tr.simbolo) else False
    
    def __repr__(self):
        return self.inicio, self.fin, self.simbolo