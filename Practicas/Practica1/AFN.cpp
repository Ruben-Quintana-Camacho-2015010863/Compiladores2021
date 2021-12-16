#include <iostream>
#include <fstream>  //Manejo de archivos
#include <string>
#include <vector>   //Libreria para hacer uso de algo parecido a un ArrayList
#include <regex>
#include "AFN.h"
using namespace std;

AFN::AFN(){

}

void carga(string nombre){
    ofstream file; //Puede que sirva :L
    file.open(nombre, ios::out);  //Cargamos l archivo, si no existe se crea un archivo
}

void cargaTransiciones(){
    try{
        string linea;   //Almacenamos la cadena que se escribe en el archivo
        int inicio, fin;
        char c;
        std::regex expresion("(\\d+)->(\\d+),([a-zE])");    //Declaramos expresion
        std::smatch expresionMatch;
        while(!(linea.empty())){
            std::regex_search(linea, expresionMatch, expresion); //Creo que puede ir mejor en un if :L
            //if(std::regex_search(linea, expresionMatch, expresion))
        }
    }catch(exception e){

    }
}