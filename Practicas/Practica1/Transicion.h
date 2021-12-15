using namespace std;

class Transicion {
    private:
        int inicio, fin;    //Marccamos el inicio y final del automata
        char simbolo;   //Simbolo de transicion
    public:
        Transicion(int, int, char);
        int getInicio();
        int getFin();
        char getSimbolo();
        bool equals(Transicion tr);
};