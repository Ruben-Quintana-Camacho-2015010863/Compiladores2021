#include <iostream>
#include <fstream>  //Manejo de archivos
#include <string>
#include <vector>   //Libreria para hacer uso de algo parecido a un ArrayList
#include <regex>
#include "AFN.h"
using namespace std;

AFN::AFN(){

}

void AFN::carga(string nombre){
    ofstream file; //Puede que sirva :L
    file.open(nombre, ios::out);  //Cargamos l archivo, si no existe se crea un archivo
}

void AFN::cargaTransiciones(){
    try{
        string linea;   //Almacenamos la cadena que se escribe en el archivo
        int inicio, fin;
        const char *c;
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
    }catch(exception e){

    }
}

void AFN::addTransicion(int inicio, int fin, const char *simbolo){
    //Transicion transicion = new Transicion(inicio, fin, simbolo);   //new??
}