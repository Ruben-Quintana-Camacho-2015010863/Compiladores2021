#include <iostream>
#include <fstream>
#include <vector>
#include "Transicion.h"
using namespace std;

// Asi como el AFN, el AFD tiene la misma logica (eso creo)
// solo necesitamos cambiar ciertas cosas
class AFD{
    private:
        int incial;
        int finales[20];
        std::vector<Transicion> transiciones;
    public:
        AFD();
        void carga(string nombre);
        void cargaTransiciones(string nombre);
        void addTransicion(int inicio, int fin, const char *simbolo);
        void obtenerInicial(string nombre);
        void rmTransicion(int inicio, int fin, const char *simbolo); //Segun mi logica, hasta ahora solo debo hacer manejo de un indice
        void obtenerFinal(string nombre);
        void establecerFinal(int estado);
        bool esAFN();
        bool esAFD();
};