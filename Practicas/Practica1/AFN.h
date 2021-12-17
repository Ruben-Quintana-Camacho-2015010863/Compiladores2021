#include <iostream>
#include <fstream>
#include <vector>
#include "Transicion.h"
using namespace std;

class AFN{
    private:
        int incial;
        int finales[20];
        std::vector<Transicion> transiciones;
        //Archivo txt para anotacion de las transiciones
        //ofstream file;
    public:
        AFN();
        void carga(string nom);   //archivo
        void cargaTransiciones();
        void addTransicion(int ini, int fin, const char *sim);
        void rmTransicion(int ini, int fin, const char *sim);    //Eliminar una transicion
        void obtenerInicial();
        
};