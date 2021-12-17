using namespace std;

class Transicion {
    private:
        int inicio = 0, final = 0;    //Marccamos el inicio y final del automata
        char simbolo = 'E';   //Simbolo de transicion
    public:
        Transicion(int, int, char);
        int getInicio();
        int getFin();
        char getSimbolo();
        bool equals(Transicion tr);
};