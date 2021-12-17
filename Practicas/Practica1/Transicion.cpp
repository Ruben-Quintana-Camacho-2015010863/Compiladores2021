#include <iostream>
#include <cstring>
#include "Transicion.h"
using namespace std;

//Constructor, segun yo cuenta como seter tambien :L
Transicion::Transicion(int ini, int fin, char sim){
    this -> inicio = ini;
    this -> final = fin;
    this -> simbolo = sim;//Transicion epsilon
}

int Transicion::getInicio(){
    return inicio;
}

int Transicion::getFin(){
    return final;
}

char Transicion::getSimbolo(){
    return simbolo;
}

bool Transicion::equals(Transicion tr){
    int in = tr.getInicio();
    int fn = tr.getFin();
    char c = tr.getSimbolo();
    if( (inicio == in) && (final == fn) && (simbolo == c) ){
        return true;
    }else{
        return false;
    }
}
