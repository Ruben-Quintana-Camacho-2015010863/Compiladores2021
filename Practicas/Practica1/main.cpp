#include <iostream>
#include "Transicion.h"
#include "AFN.h"
using namespace std;

int main() {
    AFN autnd;  //Automata ND
    char simbolo = 'a';
    autnd.carga("..\\afn.afn");
    autnd.obtenerInicial("..\\afn.afn");
    autnd.obtenerFinal("..\\afn.afn");
    autnd.addTransicion(11,10, &simbolo);
    return 0;
}