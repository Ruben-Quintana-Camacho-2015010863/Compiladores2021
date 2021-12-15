#include <iostream>
#include "Transicion.h"
using namespace std;

//Constructor
Transicion::Transicion(int inicio, int fin, char simbolo){
    inicio = 0;
    fin = 0;
    simbolo = 'E';//Transicion epsilon
}
