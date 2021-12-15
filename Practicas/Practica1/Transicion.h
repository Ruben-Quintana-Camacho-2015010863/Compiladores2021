using namespace std;

class Transicion {
    private:
        int inicio, fin;
        char simbolo;
    public:
        Transicion(int, int, char);
        int getInicio();
        int getFin();
        char getSimbolo();
        bool equals();
};