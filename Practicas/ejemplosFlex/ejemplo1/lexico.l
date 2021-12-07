%{
    /*
    Lenguaje LEX se usaba para lex
    Lex es un programa de UNIX
    Flex es la version libre de lex

    Un analizador lexico se define o se 
    especifica usando expresiones regulares.

    Una expresion regular es una notacion simplificada
    para lenguajes regulares.

    - Lenguajes regulares: conjunto finitos + operaciones
    - Operaciones: Union, concatenacion y cerradura.
    */

    /*Codigo C*/
    #include<stdio.h>

%}
digito  [0-9]
letra   [a-zA-Z]
palabras    "int"|"char"|"float"
%%
{palabras}                          { printf("-PR-\n"); }
({letra}|_)({letra}|{digito}|_)*    { printf("-ID-\n"); }
"{"|"}"|"("|")"|";"                 { printf("-SEP-\n"); }
[1-9]{digito}*|"0"                  { printf("-CTE-\n"); }
"="|"+"|"-"                         { printf("-OP-\n"); }
%%