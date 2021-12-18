#include <iostream>
#include <fstream>
#include <regex>
#include <vector>
#include <string>
#include <functional>
#include "AFD.h"    // :L
#include "Transicion.h"
#include <numeric>
using namespace std;
fstream file;

AFD::AFD(){

}

void AFD::carga(string nombre){
    file.open(nombre, ios::out);  // ios::out => si no existe se crea un archivo
    if(file.fail()){
        std::cout << "No se pudo abrir el archivo\n";
        exit(1);
    }
    file.close();
}

void AFD::cargaTransiciones(string nombre){
    try{
        string linea;   //Almacenamos la cadena que se escribe en el archivo
        int inicio, fin;
        const char *c;

        file.open(nombre.c_str());
        if(file.fail()){
            std::cout << "No se pudo abrir el archivo\n";
            exit(1);
        }
        getline(file, linea);
        std::regex expresion("(\\d+)->(\\d+),([a-zE])");    //Declaramos expresion
        std::cmatch expresionMatch;
        while(!(linea.empty())){
            if(std::regex_search(linea, expresionMatch, expresion)){
                inicio = stoi(expresionMatch[1]);
                fin = stoi(expresionMatch[2]);
                c = expresionMatch[3].first;
                addTransicion(inicio, fin, c);  //Agremos una transicion al archivo
            }
        }
        file.close();
    }catch(const std::exception& e){

    }
}

void AFD::addTransicion(int inicio, int fin, const char *simbolo){
    Transicion transicion(inicio, fin, *simbolo);
    transiciones.push_back(transicion);
}

void AFD::rmTransicion(int inicio, int fin, const char *simbolo){
    Transicion trans(inicio, fin, *simbolo);
    int indice = 0;     //Contador inidice para indicar nuestra posicion
    for(Transicion transicion : this -> transiciones){
        if(transicion.equals(trans)){
            transiciones.erase(transicion);
        }
        indice++;
    }
}

void AFD::obtenerInicial(string nombre){

}