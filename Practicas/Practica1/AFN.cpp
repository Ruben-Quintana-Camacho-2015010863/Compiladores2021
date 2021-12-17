#include <iostream>
#include <fstream>  //Manejo de archivos
#include <string>
#include <vector>   //Libreria para hacer uso de algo parecido a un ArrayList
#include <regex>
#include "AFN.h"
#include "Transicion.h"
using namespace std;
fstream file;

AFN::AFN(){

}

void AFN::carga(string nombre){
    //ofstream file; //Puede que sirva :L
    file.open(nombre, ios::out);  //Cargamos l archivo, si no existe se crea un archivo
    if(file.fail()){
        std::cout << "No se pudo abrir el archivo\n";
        exit(1);
    }
    file.close();
}

void AFN::cargaTransiciones(string nombre){
    try{
        string linea;   //Almacenamos la cadena que se escribe en el archivo
        int inicio, fin;
        const char *c;

        file.open(nombre.c_str());
        if(file.fail()){
            std::cout << "No se pudo abrir el archivo\n";
            exit(1);
        }
        //linea = file.getline();
        getline(file, linea);
        std::regex expresion("(\\d+)->(\\d+),([a-zE])");    //Declaramos expresion
        std::cmatch expresionMatch;
        while(!(linea.empty())){
            if(std::regex_search(linea, expresionMatch, expresion)){ //Creo que puede ir mejor en un if :L
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

void AFN::addTransicion(int inicio, int fin, const char *simbolo){
    //Transicion *transicion = new Transicion(inicio, fin, simbolo);   //new??
    Transicion transicion(inicio, fin, *simbolo);
    transiciones.push_back(transicion);
}

void AFN::rmTransicion(int inicio, int fin, const char *simbolo){
    Transicion trans(inicio, fin, *simbolo);
    for(Transicion transicion : this -> transiciones){
        if(transicion.equals(trans)){
            //transiciones.pop_back(transicion);
            transiciones.erase(transicion);
        }
    }
}

void AFN::obtenerInicial(){
    try{
        /* code */
    }catch(const std::exception& e){

    }
       
}