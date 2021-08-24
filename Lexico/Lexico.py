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
            simbolos[simbolo] = "Real"
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

    elif estado==404:
        if caracter == " ": #Termina el simbolo
            estado=0
            simbolos[simbolo] = "Error"
            simbolo= ""
        else:
            simbolo+=caracter

print(simbolos)
