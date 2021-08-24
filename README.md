# Lexico
El funcionamiento de lexico es bastante sencillo, lo que hice fue introducir una fuente que es lo que tendré que analizar
Le agrego un espacio al final para que me reconozca el últimos símbolo
Inicializo un diccionario donde guardo todos los simbolos que se detectaron, este guarda los datos de la siguientes manera "Simbolo:Tipo"
Tambien inicializo en el estado 0 de mi automata y creo una variable donde se va guardando cada caracter que forma el simbolo
Lo siguiente es un ciclo donde empieza mi automata que se ejecutará por cada caracter en la fuente
El estado 0 te pasa al 1 si es un caracter, al 2 si es un digito, si hay un espacio entiendo que hubo un error de dedo y sólo ignoro el caracter, si hay algo más lo mando al estado 404 que es un error
El estado 1 es para los caracteres y de momento sólo busca si es un identificador, para aceptarlo el siguiente caracter debe de ser un espacio vacio (Por eso agrego un espacio al final de la cadena)
Si no es ni caracter o digito es un error y se va al estado 404
El estado 2 es por si encontramos un numero real aunque mientras escribo esto, con la lógica que llevo ya podría identificar si es un entero
En cuanto obtiene un punto es enviado al estado 3
En el estado 3 no puede tener otro punto o te enviara al estado 404 y al igual que el estado 1, se acepta hasta que haya un espacio en blanco
El estado 404 es mi forma de identificar los errores sólo los mantengo dentro de ese estado hasta llegar a un espacio en blanco y se agregan al diccionario como errores
Al final solo imprimo todo el diccionario
