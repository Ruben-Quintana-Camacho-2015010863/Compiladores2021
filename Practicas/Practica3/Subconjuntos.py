import AFN

if __name__ == "__main__":
    autn = AFN.AFN()
    autn.carga("afn.afn")
    autn.cargaTransiciones()
    autn.obtenerInicial()
    autn.obtenerFinal()
    autn.obtenerAlfabeto()

    #Ahora solo falta definir el algoritmo, con ayuda de stackoverflow xd