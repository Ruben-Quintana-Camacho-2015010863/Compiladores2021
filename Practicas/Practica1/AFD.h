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
        
};