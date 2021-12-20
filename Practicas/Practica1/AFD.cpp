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
    try{
        string linea;

        file.open(nombre.c_str());
        if(file.fail()){
            std::cout << "No se pudo abrir el archivo\n";
            exit(1);
        }
        getline(file, linea);
        std::regex expresion("([a-zA-z]+)(\\d+)");
        std::cmatch expresionMatch;
        std::regex_search(linea, expresionMatch, expresion);
        this -> incial = stoi(expresionMatch[2]);
        file.close();
    }catch(const std::exception& e){

    }
}

void AFD::obtenerFinal(string nombre){
    try{
        string linea;
        int indice = 0;
        string aux[20];
        int nums[20];

        file.open(nombre.c_str());
        if(file.fail()){
            std::cout << "No se pudo abrir el archivo\n";
            exit(1);
        }
        //getline(file, linea);
        std::regex expresion("([a-zA-z]+):(.\\s*\\d+)+)");
        std::cmatch expresionMatch;
        for(int i = 0; i <= 1; i++){
            getline(file,linea);
            if(i == 1){ //Arreglo de funciones para simular el proceso en Java.
                std::regex_search(linea, expresionMatch, expresion);
                this -> finales = std::accumulate(begin(expresionMatch), end(expresionMatch),2, [](const AFD &c){
                    return expresionMatch[2];
                });
            }
        }
        file.close();
    }catch(const std::exception& e){
        
    }   
}

void AFD::establecerFinal(int estado){
    int aux[10];
    for(int i = 0; i <= sizeof(finales+1); i++){
        aux[i] = finales[i];
    }
    aux[sizeof(aux)-1]= estado;
    this->finales = aux;
}

bool AFD::esAFN(){
    for(Transicion transicion : this->transiciones){
        if(transicion.getSimbolo() == 'E'){
            return true;
        }
    }
    return false;
}

bool AFD::esAFD(){
    for(Transicion transicion : this->transiciones){
        if(transicion.getSimbolo() == 'E'){
            return false;
        }
    }
    return true;
}