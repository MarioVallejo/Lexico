fuente="avellana 3.3 3a 3..3 a3a"
fuente+=" "
simbolos={} #Para agregar simbolos["Simbolo"] = "tipo (0)"
estado=0
simbolo=""

for caracter in fuente:
    if estado==0:

        if caracter.isdigit()==True:
            simbolo+=caracter
            estado=2

        elif caracter.isalpha()==True:
            simbolo+=caracter
            estado=1

        elif caracter==" ":
            estado=0

        elif caracter=="+" or caracter=="-":
            simbolo+=caracter
            estado=4

        elif caracter=="*" or caracter=="/":
            simbolo+=caracter
            estado=5

        elif caracter=="<" or caracter==">":
            simbolo+=caracter
            estado=6
        
        elif caracter=="|":
            simbolo+=caracter
            estado=8

        elif caracter=="&":
            simbolo+=caracter
            estado=10

        elif caracter=="!":
            simbolo+=caracter
            estado=12

        elif caracter=="=":
            simbolo+=caracter
            estado=14

        elif caracter==";":
            simbolo+=caracter
            estado=15

        elif caracter==",":
            simbolo+=caracter
            estado=16

        elif caracter=="(":
            simbolo+=caracter
            estado=17

        elif caracter==")":
            simbolo+=caracter
            estado=18

        elif caracter=="{":
            simbolo+=caracter
            estado=19

        elif caracter=="}":
            simbolo+=caracter
            estado=20

        else: #Error
            simbolo+=caracter
            estado=404

    elif estado==1: 

        if caracter.isdigit()==True:
            simbolo+=caracter

        elif caracter.isalpha()==True:
            simbolo+=caracter

        elif caracter == " ": #Aceptacion
            estado=0
            if simbolo=="int" or simbolo=="float" or simbolo=="void":
                simbolos[simbolo] = "Tipo"

            elif simbolo=="if":
                simbolos[simbolo] = "if"

            elif simbolo=="while":
                simbolos[simbolo] = "while"

            elif simbolo=="return":
                simbolos[simbolo] = "return"

            else:
                simbolos[simbolo] = "Identificador"
                simbolo= ""
        
        else: #Error
            simbolo+=caracter
            estado=404

    elif estado==2:
        if caracter.isdigit()==True:
            simbolo+=caracter

        elif caracter == ".":
           simbolo+=caracter
           estado=3

        elif caracter == " ": #Aceptacion
            estado=0
            simbolos[simbolo] = "Entero"
            simbolo= ""

        else: #Error
            simbolo+=caracter
            estado=404

    elif estado==3:

        if caracter.isdigit()==True:
            simbolo+=caracter

        elif caracter == " ": #Aceptacion
            estado=0
            simbolos[simbolo] = "Real"
            simbolo= ""

        else: #Error
            simbolo+=caracter
            estado=404
    
    elif estado==4:

        if caracter == " ":
            estado=0
            simbolos[simbolo] = "OpSuma"
            simbolo= ""

        else: 
            simbolo+=caracter
            estado=404

    elif estado==5:

        if caracter == " ":
            estado=0
            simbolos[simbolo] = "OpMul"
            simbolo= ""

        else: 
            simbolo+=caracter
            estado=404
    
    elif estado==6:

        if caracter == " ":
            estado=0
            simbolos[simbolo] = "OpRelac"
            simbolo= ""
        
        elif caracter == "=":
            simbolo+=caracter
            estado=7

        else: 
            simbolo+=caracter
            estado=404

    elif estado==7:

        if caracter == " ":
            estado=0
            simbolos=[simbolo] = "OpRelac"
            simbolo= ""
        
        else:
            simbolo+=caracter
            estado=404
    
    elif estado==8:

        if caracter=="|":
            estado=9
            simbolo+=caracter

        else:
            simbolo+=caracter
            estado=404

    elif estado==9:

        if caracter==" ":
            estado=0
            simbolos[simbolo] = "OpOr"
            simbolo= ""

        else:
            simbolo+=caracter
            estado=404

    elif estado==10:

        if caracter=="&":
            estado=11
            simbolo+=caracter

        else:
            simbolo+=caracter
            estado=404

    elif estado==11:

        if caracter==" ":
            estado=0
            simbolos[simbolo] = "OpAnd"
            simbolo= ""

        else:
            simbolo+=caracter
            estado=404
    
    elif estado==12:

        if caracter==" ":
            estado=0
            simbolos[simbolo]="OpNot"
            simbolo= ""
        
        elif caracter=="=":
            estado=13
            simbolo+=caracter

        else:
            simbolo+=caracter
            estado=404

    elif estado==13:

        if caracter==" ":
            estado=0
            simbolos[simbolo]="OpIgualdad"
            simbolo=""

        else:
            simbolo+=caracter
            estado=404

    elif estado==14:

        if caracter==" ":
            estado=0
            simbolos[simbolo]="="
            simbolo=""

        elif caracter=="=":
            estado=13
            simbolo+=caracter
        
        else:
            simbolo+=caracter
            estado=404
    
    elif estado==15:

        if caracter==" ":
            estado=0
            simbolos[simbolo]=";"
            simbolo=""

        else:
            simbolo+=caracter
            estado=404

    elif estado==16:

        if caracter==" ":
            estado=0
            simbolos[simbolo]=","
            simbolo=""

        else:
            simbolo+=caracter
            estado=404
    
    elif estado==17:

        if caracter==" ":
            estado=0
            simbolos[simbolo]="("
            simbolo=""

        else:
            simbolo+=caracter
            estado=404            

    elif estado==18:

        if caracter==" ":
            estado=0
            simbolos[simbolo]=")"
            simbolo=""

        else:
            simbolo+=caracter
            estado=404

    elif estado==19:

        if caracter==" ":
            estado=0
            simbolos[simbolo]="{"
            simbolo=""

        else:
            simbolo+=caracter
            estado=404

    elif estado==20:

        if caracter==" ":
            estado=0
            simbolos[simbolo]="}"
            simbolo=""

        else:
            simbolo+=caracter
            estado=404

    elif estado==404:
        if caracter == " ": #Termina el simbolo
            estado=0
            simbolos[simbolo] = "Error"
            simbolo= ""
        else:
            simbolo+=caracter

print(simbolos)
