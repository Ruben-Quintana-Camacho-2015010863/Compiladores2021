#include <iostream>
#include "Transicion.h"
using namespace std;

//Constructor, segun yo cuenta como seter tambien :L
Transicion::Transicion(int inicio, int fin, char simbolo){
    inicio = 0;
    fin = 0;
    simbolo = 'E';//Transicion epsilon
}

int Transicion::getInicio(){
    return inicio;
}

int Transicion::getFin(){
    return fin;
}

char Transicion::getSimbolo(){
    return simbolo;
}

bool Transicion::equals(Transicion tr){
    int in = tr.getInicio();
    int fn = tr.getFin();
    char c = tr.getSimbolo();
    if( (inicio == in) && (fin == fn) && (simbolo == c) ){
        return true;
    }else{
        return false;
    }
}
