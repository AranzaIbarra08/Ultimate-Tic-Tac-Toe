"""
Este es el proyecto para la clase de Inteligencia Artificial del Equipo 2. 

Este equipo está integrado por: 
  *Aranza Ibarra Camarena
  *Brauilio Lozano Cuevas
  * Mingyar Romero Medellín 
  *Carlos Montejano León
"""

"""
Manual de usuario: 
  Este manual es simplemente para poder entender qué hace cada función, 
  qué es lo que recibe, qué es lo que regresa, cómo se conecta y cómo debería jugarse. 
  
  Todo lo que sea parte del manual de usuario se va a encontrar dentro de "" 
  mientras que todo lo que sea un solo comentario (a partir de este momento) será
  especificado con #. 

"""

#Estas simplemente son las librerías necesarias que utilizamos para poder 
#programar lo que necesitabamos. 

from math import inf
from collections import Counter
import itertools          
from time import time

"""
Gracias a que decidimos que en la terminal se imprimiera la cuadrícula del gato de gatos. 
Lo que sucedió fue que para que se pudiera imprimir de manera 'linda' utilizamos indices. 

Entonces, el movimiento Aa sería indicado por el índice (1,1). 

Aquí debo un tablero indicando cada coordenada. 
(1,1) (1,2) (1,3)| (1,4) (1,5) (1,6) | (1,7) (1,8) (1,9)
(2,1) (2,2) (2,3)| (2,4) (2,5) (2,6) | (2,7) (2,8) (2,9)
(3,1) (3,2) (3,3)| (3,4) (3,5) (3,6) | (3,7) (3,8) (3,9)
--------------------------------------------------------
(4,1) (4,2) (4,3)| (4,4) (4,5) (4,6) | (4,7) (4,8) (4,9)
(5,1) (5,2) (5,3)| (5,4) (5,5) (5,6) | (5,7) (5,8) (5,9)
(6,1) (6,2) (6,3)| (6,4) (6,5) (6,6) | (6,7) (6,8) (6,9)
--------------------------------------------------------
(7,1) (7,2) (7,3)| (7,4) (7,5) (7,6) | (7,7) (7,8) (7,9)
(8,1) (8,2) (8,3)| (8,4) (8,5) (8,6) | (8,7) (8,8) (8,9)
(9,1) (9,2) (9,3)| (9,4) (9,5) (9,6) | (9,7) (9,8) (9,9)

Sin embargo, cuando se hace un movimeinto SI indica a qué 'cuadro' del Tablero
grande irse para hacer su movimiento. Las indicaciones son: 
  
  A|B|C
  ----
  D|E|F
  -----
  G|H|I
  
  Para poder recibir las coordenadas que queremos utilizar primero checa si el primer
  movimiento de todo el juego por parte del humano y así le permite tirar 
  sin restricción alguna.

  La primera función indica solo cómo obtenemos los índices
  Aquí debo un tablero indicando cada coordenada. 
"""

"""
Solicita al jugador decidir quién inicia la partida en el juego Ultimate Tic Tac Toe.

Esta función interactiva pide al jugador seleccionar si desea iniciar el juego o si prefiere que la máquina comience. 
El usuario debe responder con 'u' para sí mismo o 'm' para que la máquina inicie. Cualquier entrada diferente 
provoca una solicitud repetida hasta recibir una respuesta válida. Esta decisión inicial es crucial para definir 
la estrategia de juego desde el comienzo.

Devuelve:
- True si el jugador decide comenzar el juego.
- False si el jugador elige que la máquina comience.
"""


def choose_starter():
    while True:  # Este bucle continuará hasta que se rompa explícitamente.
        choice = input("Who should start? (u/m): ").strip().lower()  # Solicita la entrada del usuario y la normaliza.
        if choice == "u":
            return True  # Si la elección es 'u', retorna True.
        elif choice == "m":
            return False  # Si la elección es 'm', retorna False.
        else:
            print("Invalid response. Please enter 'u' for you or 'm' for the machine.")  # Mensaje de error.

"""
Solicita al jugador realizar un movimiento en el juego Ultimate Tic Tac Toe, validando la entrada.

Dependiendo del estado actual del juego y del último movimiento realizado, esta función guía al jugador sobre dónde 
puede colocar su siguiente 'X'. Si es libre de elegir cualquier cuadrante (al inicio del juego o si el cuadrante 
dirigido está lleno), se le informa que puede colocar 'X' en cualquier lugar. De lo contrario, se indica específicamente 
en qué cuadrante debe jugar, basándose en la última jugada de la máquina. La función valida que la elección del jugador 
esté dentro de los límites permitidos y que la celda seleccionada esté vacía, garantizando así que el movimiento es válido.

Parámetros:
- state: El estado actual del tablero, representado como una cadena de caracteres.
- bm: El índice del último movimiento realizado en el juego, utilizado para determinar las restricciones de movimiento.

Devuelve:
- Una tupla (x, y) con la fila y columna seleccionadas por el jugador para su próximo movimiento, validando que 
  la selección sea legal de acuerdo con las reglas del juego y el estado actual del tablero.
"""

def take_input(state, bm):
    # Inicializa una bandera para determinar si el jugador puede colocar 'X' en cualquier lugar
    free_placement = False

    # Verifica si es el primer movimiento o si el último movimiento permite jugar en cualquier cuadrante
    if bm == -1 or len(check_move_with_last(bm)) > 9:
        free_placement = True

    # Si el jugador puede colocar 'X' en cualquier lugar, imprime un mensaje indicándolo
    if free_placement:
        print("Place X wherever you want.")
    else:
        # Diccionario para mapear los índices de los cuadrantes a letras para una mejor comprensión
        box_dict = {0: "A", 1: "B", 2: "C",
                    3: "D", 4: "E", 5: "F",
                    6: "G", 7: "H", 8: "I"}
        # Indica al jugador en qué cuadrante debe jugar, basado en el último movimiento
        print(f"Where do you want to place X in the {box_dict[bm % 9]} square?")

    # Solicita al jugador que ingrese el número de fila y valida la entrada
    x = int(input("Row = "))

    # Solicita al jugador que ingrese el número de columna y valida la entrada
    y = int(input("Column = "))
    print()  # Imprime una línea en blanco para mejorar la legibilidad

    # Verifica si el movimiento está permitido en el cuadrante específico, según las reglas del juego
    if bm != -1 and index(x, y) not in check_move_with_last(bm):
        raise ValueError("Invalid move: Not allowed in this square based on the last move.")

    # Verifica si el movimiento es válido (la casilla está libre y el movimiento es dentro de los límites del tablero)
    if not valid_input(state, (x, y)):
        raise ValueError("Invalid move: The cell is not available or out of bounds.")

    # Devuelve la posición elegida por el jugador como una tupla (fila, columna)
    return (x, y)


"""
Visualiza el tablero actual de Ultimate Tic Tac Toe, mostrando las posiciones de 'X' y 'O'.

Esta función imprime el estado actual del tablero de Ultimate Tic Tac Toe, diseñado como una cuadrícula de 9x9 que representa
9 'gatos pequeños'. Cada celda puede contener una 'X', una 'O' o estar vacía, indicando el progreso actual del juego. La visualización
incluye separadores para distinguir claramente cada uno de los 9 subtableros y facilitar la elección de movimientos por parte del jugador.

La impresión comienza con una cabecera que numera las columnas del 1 al 9, ayudando a los jugadores a identificar fácilmente las coordenadas
para sus movimientos. Luego, se itera a través de cada fila y columna del tablero, imprimiendo el contenido de cada celda junto con separadores
verticales y horizontales que organizan visualmente el tablero en sus 9 subtableros. Esta estructura clara y fácil de leer es esencial para
que los jugadores planifiquen sus estrategias y determinen sus próximos movimientos en el juego.

Parámetros:
- state: El estado actual del tablero, representado como una cadena de 81 caracteres. Cada carácter representa una celda en el tablero,
               que puede ser 'X', 'O' o un espacio en blanco para celdas vacías.

No devuelve nada, pero imprime directamente el estado del tablero en la consola para que el jugador lo vea.
"""


def output_tic_tac(state):
    # Imprime la cabecera del tablero para facilitar la identificación de las columnas.
    # Esto ayuda a los jugadores a visualizar mejor cómo referirse a cada posición del tablero.
    print(" 1  2  3  4  5  6  7  8  9 ")  # Guía de columnas para el usuario.

    # Itera sobre cada fila del tablero para construir y mostrar su estado actual.
    for row in range(1, 10):
        # Inicializa la cadena de la fila actual, empezando con el número de fila y un separador.
        row_str = [str(row) + "|"]

        # Itera sobre cada columna en la fila actual para agregar el estado de cada celda (X, O o vacío).
        for col in range(1, 10):
            # Añade el estado de la celda actual a la cadena de la fila.
            row_str += [state[index(row, col)]]

            # Añade un separador vertical después de cada grupo de tres columnas para visualizar los subtableros.
            if col % 3 == 0:
                row_str += ["|"]

        # Imprime una línea divisoria horizontal antes de cada nuevo grupo de tres filas para separar los subtableros.
        if (row - 1) % 3 == 0:
            print("-" * (len(row_str) * 2 - 1))

        # Imprime el estado actual de la fila, incluyendo los contenidos de las celdas y los separadores.
        print(" ".join(row_str))

    # Imprime una línea divisoria final al final del tablero para mantener una apariencia consistente.
    print("-" * (len(row_str) * 2 - 1))
    
"""
Actualiza el estado del tablero de juego con el nuevo movimiento realizado por un jugador.

Esta función modifica el estado actual del tablero, insertando el símbolo del jugador ('X' o 'O')
en la posición especificada por el movimiento. Se asegura de que el estado del tablero refleje
correctamente todos los movimientos realizados hasta el momento.

Parámetros:
- state : Cadena que representa el estado actual del tablero de juego. Cada carácter puede ser
               un espacio vacío (indicando una celda vacía), 'X' o 'O'.
- move : Si el movimiento es una tupla, representa las coordenadas (fila, columna)
                      del movimiento a realizar. Si es un entero, representa el índice directo
                      en la cadena del estado del tablero.
- player : El símbolo del jugador actual ('X' o 'O') que está realizando el movimiento.

Devuelve:
- str: La cadena actualizada que representa el nuevo estado del tablero después de realizar el movimiento.

Nota: Si 'move' es una tupla, se convierte a un índice entero utilizando la función 'index' para
      determinar la posición exacta dentro de la cadena de estado. Esto permite una actualización
      directa y eficiente del tablero.
"""

def actualice_play(state, move, player):
    # Convierte el movimiento a un índice entero si viene en formato de tupla (fila, columna).
    if not isinstance(move, int):
        move = index(move[0], move[1])
    
    # Actualiza el estado del tablero insertando el símbolo del jugador en la posición indicada.
    return state[:move] + player + state[move + 1:]

    """
    Actualiza el estado de los 'gatos pequeños' para reflejar si alguno ha sido ganado.

    Esta función revisa cada 'gato pequeño' en el juego de Ultimate Tic Tac Toe para determinar si
    existe un ganador para cada uno. Un 'gato pequeño' corresponde a uno de los 9 subtableros en
    el tablero de juego. Si un jugador ha ganado en uno de estos subtableros, su símbolo ('X' o 'O')
    se registra en el estado general de los 'gatos pequeños'.

    Parámetros:
    - state (str): Cadena que representa el estado completo del tablero de juego, incluyendo todos
                   los 'gatos pequeños'. Cada carácter puede ser un espacio vacío (indicando una
                   celda vacía), 'X' o 'O'.

    Devuelve:
    - list: Una lista de 9 elementos que representa el estado de ganancia de cada 'gato pequeño'.
            Cada elemento puede ser un espacio vacío (indicando que el 'gato pequeño' aún no ha sido
            ganado), 'X' (indicando que el jugador 'X' ha ganado ese 'gato pequeño'), o 'O' (indicando
            que el jugador 'O' ha ganado ese 'gato pequeño').

    La función se basa en 'small_board_check' para evaluar si un jugador ha completado una línea en
    algún 'gato pequeño', lo cual es crucial para determinar la estrategia de juego, ya que ganar
    subtableros específicos puede abrir oportunidades para realizar movimientos en otras partes del
    tablero principal.
    """
    
def Update_small_to_big(state):

    # Inicializa una lista para almacenar el estado de ganancia de cada 'gato pequeño'.
    temp_box_win = [" "] * 9

    # Itera sobre cada 'gato pequeño' para revisar su estado.
    for b in range(9):
        # Genera los índices que corresponden al 'gato pequeño' actual en la cadena de estado.
        i_b = list(range(b * 9, b * 9 + 9))
        # Extrae la subcadena que representa el 'gato pequeño' actual.
        box_str = state[i_b[0]: i_b[-1] + 1]
        # Actualiza el estado de ganancia del 'gato pequeño' actual usando 'small_board_check'.
        temp_box_win[b] = small_board_check(box_str)
    
    # Devuelve la lista actualizada que representa el estado de ganancia de todos los 'gatos pequeños'.
    return temp_box_win

    """
    Calcula el índice lineal correspondiente a las coordenadas bidimensionales en el tablero de Ultimate Tic Tac Toe.

    En Ultimate Tic Tac Toe, el tablero es una cuadrícula de 9x9 que contiene 9 subtableros de 3x3. Esta función
    transforma las coordenadas bidimensionales (x, y), donde x e y van de 1 a 9, en un índice lineal que va de 0 a 80.
    Este índice lineal representa la posición en una cadena que modela el estado completo del tablero de juego.

    Parámetros:
    - x : El número de fila en el tablero, en el rango de 1 a 9.
    - y : El número de columna en el tablero, en el rango de 1 a 9.

    Devuelve:
    - int: El índice lineal correspondiente a la posición (x, y) en el tablero, utilizado para acceder o modificar
           el estado del tablero representado como una cadena.

    El cálculo del índice se realiza teniendo en cuenta la estructura dividida del tablero en subtableros, asegurando
    que cada coordenada se mapee correctamente a su posición lineal en la representación de cadena del estado del juego.
    """

def index(x, y):

    # Calcula el índice lineal basado en las coordenadas (x, y)
    return (((x - 1) // 3) * 27) + (((x - 1) % 3) * 3) + (((y - 1) // 3) * 9) + ((y - 1) % 3)
    



"""
Determina si un 'gato pequeño' (subtablero) ha sido ganado y por quién.

Esta función evalúa el estado de un 'gato pequeño' en el juego de Ultimate Tic Tac Toe, identificando si un jugador
ha logrado alinear tres de sus símbolos, sea horizontal, vertical o diagonalmente. Se llama desde la función 
'Update_small_to_big' para actualizar el estado de victoria de cada 'gato pequeño'. La implementación sigue la 
estrategia recomendada en clase de dividir el problema en funciones más simples para facilitar el manejo y la 
comprensión del código.

Parámetros:
- box_str (str): Cadena de caracteres que representa el estado del 'gato pequeño' siendo evaluado. Cada carácter
                 puede ser un espacio vacío (indicando una celda no ocupada), 'X' o 'O'.

Devuelve:
- str: El símbolo del jugador que ha ganado el 'gato pequeño' ('X' o 'O'). Si el 'gato pequeño' no ha sido ganado,
       devuelve un espacio vacío (' ').

Nota:
- 'pos_go' es una variable global que contiene las combinaciones de índices que representan todas las posibles líneas
  ganadoras en un 'gato pequeño'.
"""

def small_board_check(box_str):
    global pos_go  # Usa la variable global 'pos_go' que contiene todas las posibles líneas ganadoras.

    # Itera sobre cada conjunto de índices de líneas ganadoras.
    for idxs in pos_go:
        (x, y, z) = idxs  # Desempaqueta el conjunto de índices a variables individuales.
        
        # Verifica si los tres espacios correspondientes en el 'gato pequeño' son iguales y no están vacíos.
        if (box_str[x] == box_str[y] == box_str[z]) and box_str[x] != " ":
            return box_str[x]  # Retorna el símbolo del jugador que ha ganado este 'gato pequeño'.

    return " "  # Retorna un espacio vacío si no hay un ganador en este 'gato pequeño'.


"""
Determina los índices válidos para el próximo movimiento basándose en el último movimiento realizado.
  
  A|B|C
  ----
  D|E|F
  -----
  G|H|I
  
Esta función es crucial para implementar la regla que dicta que el próximo movimiento de un jugador debe realizarse
en el 'gato pequeño' correspondiente a la posición del último movimiento del oponente en su propio 'gato pequeño'.
Por ejemplo, si el último movimiento fue en la parte superior izquierda de un 'gato pequeño', el próximo movimiento
debe ser en el 'gato pequeño' superior izquierdo del tablero grande, a menos que este ya haya sido ganado.

Si el 'gato pequeño' relevante ya ha sido ganado (o está completamente ocupado), el jugador puede elegir cualquier
'gato pequeño' no ganado para su próximo movimiento. Esto introduce una capa adicional de estrategia al juego.

Parámetros:
- last_move: Puede ser un entero que representa el índice lineal del último movimiento realizado, o una tupla
             (fila, columna) si el movimiento se está especificando en términos de coordenadas del tablero grande.

Devuelve:
- Una lista de índices que representan posiciones válidas para el próximo movimiento en el tablero grande. Si el juego
  permite un movimiento en cualquier 'gato pequeño' no ganado, la lista incluirá índices de todas las celdas válidas
  en esos 'gatos pequeños'. Si el movimiento está restringido a un 'gato pequeño' específico, solo incluirá índices
  dentro de ese subtablero.

Uso de variables globales:
- box_won: Una lista que mantiene el estado de cada 'gato pequeño', indicando si ha sido ganado (y por quién) o si
           aún está en juego.
"""

def check_move_with_last(last_move):
    global box_won  # Utiliza la variable global 'box_won' para acceder al estado actual de los 'gatos pequeños'.

    # Convierte 'last_move' a índice lineal si es necesario.
    if not isinstance(last_move, int):
        last_move = index(last_move[0], last_move[1])

    # Calcula a qué 'gato pequeño' corresponde el último movimiento.
    box_to_play = last_move % 9

    # Genera los índices para el 'gato pequeño' objetivo.
    idxs = list(range(box_to_play * 9, box_to_play * 9 + 9))

    # Si el 'gato pequeño' ya ha sido ganado, permite el movimiento en cualquier 'gato pequeño' no ganado.
    if box_won[box_to_play] != " ":
        # Lista de índices de todos los 'gatos pequeños' no ganados.
        pi_2d = [list(range(b * 9, b * 9 + 9)) for b in range(9) if box_won[b] == " "]
        pos_indic = list(itertools.chain.from_iterable(pi_2d))
    else:
        # Restringe el movimiento al 'gato pequeño' objetivo si no ha sido ganado.
        pos_indic = idxs

    return pos_indic

"""
Genera todos los movimientos válidos siguientes basados en el estado actual del tablero, el jugador actual y el último movimiento realizado.

Esta función es fundamental para determinar las posibles opciones de movimiento que tiene un jugador en su turno. Utiliza la función
'check_move_with_last' para obtener una lista de índices donde el jugador actual puede realizar su movimiento. Luego, para cada índice
válido, simula el movimiento actualizando el estado del tablero con el símbolo del jugador en la posición correspondiente. Este proceso
ayuda a visualizar los posibles estados futuros del tablero como resultado de los movimientos válidos del jugador actual.

Parámetros:
- state (str): El estado actual del tablero representado como una cadena de caracteres, donde cada carácter puede ser 'X', 'O', o un espacio
               en blanco, indicando una casilla vacía.
- player (str): El símbolo del jugador actual ('X' o 'O').
- last_move: El último movimiento realizado en el juego, que puede ser un índice lineal o una tupla de coordenadas, utilizado para determinar
             las restricciones de movimiento basadas en las reglas del Ultimate Tic Tac Toe.

Devuelve:
- Un objeto zip que contiene pares de estados de tablero sucesores y los índices correspondientes de esos movimientos. Cada estado sucesor
  es una cadena que representa cómo se vería el tablero si el jugador actual realizara un movimiento en el índice correspondiente.
"""

def check_for_moves(state, player, last_move):
    succ = []  # Lista para almacenar los estados sucesores del tablero.
    moves_idx = []  # Lista para almacenar los índices de los movimientos válidos.

    # Obtiene los índices de los movimientos válidos basados en el último movimiento.
    pos_index = check_move_with_last(last_move)

    # Itera sobre cada índice de movimiento válido.
    for idx in pos_index:
        # Verifica si la posición está vacía (es decir, es un movimiento válido).
        if state[idx] == " ":
            moves_idx.append(idx)  # Añade el índice a la lista de movimientos válidos.
            # Actualiza el estado del tablero con el movimiento actual y lo añade a la lista de estados sucesores.
            succ.append(actualice_play(state, idx, player))

    # Devuelve pares de estados de tablero sucesores y los índices de los movimientos correspondientes.
    return zip(succ, moves_idx)


"""
Imprime el tablero para cada movimiento válido que el jugador puede realizar en su turno.

Esta función es útil para visualizar las consecuencias de cada posible movimiento que el jugador actual tiene a su disposición,
basándose en el estado actual del tablero y el último movimiento realizado. Utiliza la función 'check_for_moves' para generar
todos los posibles movimientos válidos y sus correspondientes estados de tablero sucesores. Luego, para cada estado sucesor,
utiliza 'output_tic_tac' para imprimir el tablero, permitiendo una visualización clara de cómo se vería el tablero si se
realizara ese movimiento.

Parámetros:
- state (str): El estado actual del tablero, representado como una cadena de caracteres. Cada carácter puede ser 'X', 'O', o un espacio
               en blanco, indicando una casilla vacía.
- player (str): El símbolo del jugador actual ('X' o 'O').
- last_move: El último movimiento realizado en el juego, que puede ser un índice lineal o una tupla de coordenadas. Este parámetro es
             utilizado para determinar las restricciones de movimiento basadas en las reglas del Ultimate Tic Tac Toe.
"""

def print_check_for_moves(state, player, last_move):
    # Utiliza la función 'check_for_moves' para obtener todos los posibles movimientos válidos y sus estados sucesores.
    for st in check_for_moves(state, player, last_move):
        # Para cada estado sucesor obtenido, imprime el tablero utilizando 'output_tic_tac'.
        output_tic_tac(st[0])  # st[0] contiene el estado sucesor del tablero.


"""
Alterna el símbolo del jugador entre 'X' y 'O'.

Esta función simple intercambia los símbolos de los jugadores en el juego de Tic Tac Toe. Si el símbolo actual es 'X',
devuelve 'O', y viceversa. Esto es útil para cambiar de turno entre los jugadores, asegurando que cada jugador use el símbolo
correcto en su turno.

Parámetro:
- p (str): El símbolo del jugador actual ('X' o 'O').

Devuelve:
- str: El símbolo del jugador para el próximo turno. Si el símbolo actual es 'X', devuelve 'O'; si es 'O', devuelve 'X'.
"""

def Play_X_or_O(p):
    # Devuelve 'O' si el jugador actual es 'X', de lo contrario devuelve 'X'.
    return "O" if p == "X" else "X"


"""
Aquí es donde verdaderamente comienza la heurística. Se asignan los valores a los lugares del tablero 'pequeño'
Gracias a lo que pudimos hacer practicando (jugando) nos dimos cuenta que tirar en las 'no esquinas no centro' era una buena forma de jugar. 
Lamentablmente, al apostar tanto a eso hace que nosotros estemos teniendo esos movimientos. 

Esta función asigna valores heurísticos a las posiciones ocupadas en un 'gato pequeño' del juego Ultimate Tic Tac Toe,
considerando tanto las jugadas del jugador actual como las de su oponente. La heurística se basa en la cantidad de símbolos
consecutivos (líneas de 'X' o 'O') que el jugador o su oponente tienen en el 'gato pequeño', otorgando puntajes más altos
por líneas más largas. Esta evaluación ayuda a determinar la mejor jugada posible, prefiriendo movimientos que bloqueen al
oponente o que avancen hacia la victoria en el subtablero.

Parámetros:
- box_str (str): Cadena que representa el estado del 'gato pequeño' siendo evaluado.
- player (str): El símbolo del jugador actual ('X' o 'O').

Devuelve:
- int: El puntaje heurístico del 'gato pequeño' para el jugador actual, considerando tanto las posiciones ocupadas por él
       como las de su oponente.
"""

def evaluate_smalls(box_str, player):
    global pos_go  # Accede a las combinaciones ganadoras definidas globalmente.
    score = 0  # Inicializa el puntaje heurístico.

    # Define contadores para las líneas completas, casi completas y simples del jugador.
    three = Counter(player * 3)
    two = Counter(player * 2 + " ")
    one = Counter(player * 1 + " " * 2)

    # Define contadores para las líneas completas, casi completas y simples del oponente.
    three_opponent = Counter(Play_X_or_O(player) * 3)
    two_opponent = Counter(Play_X_or_O(player) * 2 + " ")
    one_opponent = Counter(Play_X_or_O(player) * 1 + " " * 2)

    # Evalúa cada combinación ganadora posible en el 'gato pequeño'.
    for idxs in pos_go:
        (x, y, z) = idxs
        current = Counter([box_str[x], box_str[y], box_str[z]])

        # Asigna puntajes basados en la cantidad de símbolos consecutivos del jugador y su oponente.
        if current == three:
            score += 100  # Línea completa del jugador.
        elif current == two:
            score += 10  # Dos en línea del jugador con una casilla libre.
        elif current == one:
            score += 1  # Una posición ocupada por el jugador.
        elif current == three_opponent:
            score -= 100  # Línea completa del oponente.
            return score
        elif current == two_opponent:
            score -= 10  # Dos en línea del oponente con una casilla libre.
        elif current == one_opponent:
            score -= 1  # Una posición ocupada por el oponente.

    return score  # Devuelve el puntaje total heurístico para el 'gato pequeño'.

"""
Evalúa el estado general del tablero en Ultimate Tic Tac Toe para determinar un puntaje heurístico global.

Esta función calcula un puntaje heurístico para el tablero completo considerando tanto el estado de los 'gatos pequeños'
como el tablero grande en su conjunto. Utiliza 'evaluate_smalls' para calcular el puntaje de cada 'gato pequeño' individualmente,
así como el estado general de victoria en los 'gatos pequeños'. Multiplica el puntaje de los 'gatos pequeños' ganados por un factor
para enfatizar su importancia en la estrategia general del juego. Este enfoque permite identificar las mejores jugadas posibles
basándose en el estado actual del juego y los movimientos previos.

Parámetros:
- state (str): El estado actual del tablero, representado como una cadena de 81 caracteres que incluyen 'X', 'O' o espacios en blanco.
- last_move: El último movimiento realizado, necesario para evaluar las restricciones de movimiento actuales.
- player (str): El símbolo del jugador actual ('X' o 'O').

Devuelve:
- int: El puntaje heurístico total para el estado actual del tablero desde la perspectiva del jugador actual.
"""

def evaluate_all(state, last_move, player):
    global box_won  # Utiliza la variable global 'box_won' para acceder al estado de los 'gatos pequeños' ganados.

    score = 0  # Inicializa el puntaje total.

    # Calcula el puntaje basado en los 'gatos pequeños' ganados.
    score += evaluate_smalls(box_won, player) * 200  # Multiplica por 200 para dar mayor peso a los 'gatos pequeños' ganados.

    # Itera sobre cada 'gato pequeño' para evaluar y sumar su puntaje individual.
    for b in range(9):
        # Genera índices para el 'gato pequeño' actual.
        idxs = list(range(b * 9, b * 9 + 9))
        # Extrae la cadena que representa el estado del 'gato pequeño' actual.
        box_str = state[idxs[0]: idxs[-1] + 1]
        # Suma el puntaje evaluado del 'gato pequeño' al puntaje total.
        score += evaluate_smalls(box_str, player)

    return score  # Devuelve el puntaje total heurístico para el estado actual del tablero.


"""
Implementa el algoritmo Minimax con poda Alfa-Beta para el juego Ultimate Tic Tac Toe.

El algoritmo Minimax se utiliza para determinar el mejor movimiento posible para un jugador, considerando que el oponente
también jugará óptimamente. La poda Alfa-Beta mejora la eficiencia del Minimax tradicional al eliminar ramas del árbol de juego
que no necesitan ser exploradas porque no afectarán al resultado final.

La función 'minimax' es la función principal que inicia el algoritmo, alternando entre maximizar el puntaje para el jugador actual
y minimizar el puntaje para el oponente mediante las funciones 'max_turn' y 'min_turn', respectivamente.
"""




def minimax(state, last_move, player, depth, s_time):
    # Genera todos los movimientos válidos y sus estados sucesores.
    succ = check_for_moves(state, player, last_move)
    best_move = (-inf, None)  # Inicializa el mejor movimiento y su valor.
   
    # Evalúa cada movimiento sucesor utilizando el turno del oponente (min_turn).
    for s in succ:
        val = min_turn(s[0], s[1], Play_X_or_O(player), depth - 1, s_time, -inf, inf)
        if val > best_move[0]:  # Actualiza el mejor movimiento si se encuentra un valor mayor.
            best_move = (val, s)
    return best_move[1]  # Devuelve el índice del mejor movimiento.

def min_turn(state, last_move, player, depth, s_time, alpha, beta):
    # Comprueba la condición de terminación del algoritmo.
    if depth <= 0 or small_board_check(box_won) != " ":
        return evaluate_all(state, last_move, Play_X_or_O(player))
    
    # Genera todos los movimientos válidos y sus estados sucesores.
    succ = check_for_moves(state, player, last_move)
    for s in succ:
        val = max_turn(s[0], s[1], Play_X_or_O(player), depth - 1, s_time, alpha, beta)
        if val < beta:  # Actualiza beta si se encuentra un valor menor, para minimizar.
            beta = val
        if alpha >= beta:  # Poda Alfa-Beta.
            break
    return beta  # Devuelve el valor mínimo encontrado.

def max_turn(state, last_move, player, depth, s_time, alpha, beta):
    # Comprueba la condición de terminación del algoritmo.
    if depth <= 0 or small_board_check(box_won) != " ":
        return evaluate_all(state, last_move, player)
    
    # Genera todos los movimientos válidos y sus estados sucesores.
    succ = check_for_moves(state, player, last_move)
    for s in succ:
        val = min_turn(s[0], s[1], Play_X_or_O(player), depth - 1, s_time, alpha, beta)
        if alpha < val:  # Actualiza alpha si se encuentra un valor mayor, para maximizar.
            alpha = val
        if alpha >= beta:  # Poda Alfa-Beta.
            break
    return alpha  # Devuelve el valor máximo encontrado.


"""
Verifica si un movimiento es válido dentro del juego Ultimate Tic Tac Toe.

Esta función asegura que el movimiento propuesto por un jugador cumple con varios criterios de validez:
1. Está dentro de los límites del tablero, que van de 1 a 9 tanto para filas como para columnas.
2. El 'gato pequeño' correspondiente al movimiento no ha sido ganado previamente (indicado por 'box_won').
3. La celda específica dentro del tablero está vacía y lista para ser ocupada.

Al cumplir con estos criterios, se garantiza que el movimiento es legal según las reglas del juego y las restricciones
del estado actual del tablero.

Parámetros:
- state (str): El estado actual del tablero, representado como una cadena de 81 caracteres que incluyen 'X', 'O', o espacios en blanco.
- move (tuple): Una tupla de dos enteros que representan la fila y la columna del movimiento propuesto.

Devuelve:
- bool: True si el movimiento es válido; False en caso contrario.
"""

def valid_input(state, move):
    global box_won  # Accede a la variable global que indica el estado de victoria de cada 'gato pequeño'.

    # Verifica que el movimiento esté dentro de los límites del tablero (1 a 9 para filas y columnas).
    if not (0 < move[0] < 10 and 0 < move[1] < 10):
        return False  # El movimiento está fuera de los límites.

    # Calcula el índice del 'gato pequeño' afectado y verifica si ya ha sido ganado.
    if box_won[index(move[0], move[1]) // 9] != " ":
        return False  # El 'gato pequeño' correspondiente ya ha sido ganado.

    # Verifica si la celda específica dentro del tablero está vacía.
    if state[index(move[0], move[1])] != " ":
        return False  # La celda ya está ocupada.

    return True  # El movimiento cumple con todos los criterios y es válido.


"""
Inicia y ejecuta el flujo completo del juego Ultimate Tic Tac Toe.

Esta función controla el flujo del juego, alternando turnos entre el usuario y la máquina, y utilizando
las funciones previamente definidas para gestionar la lógica del juego. Incluye la inicialización del
tablero, la determinación de quién inicia el juego, la realización de movimientos válidos, la evaluación
del estado del juego para determinar un ganador, y la terminación del juego con un mensaje apropiado.

Parámetros:
- state (str): Estado inicial del tablero, representado como una cadena de 81 espacios en blanco por defecto.
- depth (int): Profundidad máxima de búsqueda para el algoritmo Minimax, con un valor predeterminado de 20.

Devuelve:
- str: El estado final del tablero al concluir el juego.
"""
def game(state=" " * 81, depth=20):
    global box_won, pos_go  # Variables globales para el estado de los 'gatos pequeños' y las combinaciones ganadoras.
    
    # Define las combinaciones ganadoras para los 'gatos pequeños'.
    pos_go = [(0, 4, 8), (2, 4, 6), (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8)]
    
    # Actualiza el estado de los 'gatos pequeños' basado en el estado inicial del tablero.
    box_won = Update_small_to_big(state)
    output_tic_tac(state)  # Muestra el tablero inicial.

    # Determina quién comienza el juego, usuario o máquina.
    is_user_turn = choose_starter()
    bm = -1  # Índice del último movimiento, inicialmente inválido.

    while True:
        if is_user_turn:  # Turno del usuario.
            try:
                # Solicita y procesa el movimiento del usuario.
                user_move = take_input(state, bm)
                user_state = actualice_play(state, user_move, "X")
                bm = user_move
            except ValueError:
                # Maneja errores en la entrada del usuario y repite el turno.
                print("Error!")
                output_tic_tac(state)
                continue
            output_tic_tac(user_state)
            state = user_state
        else:  # Turno de la máquina.
            print("Bot is spinning gears...")
            s_time = time()
            bot_state, bm = minimax(state, bm, "O", depth, s_time)
            print(f"Bot placed O at position {bm}")
            output_tic_tac(bot_state)
            state = bot_state

        # Comprueba el estado del juego para determinar si hay un ganador.
        box_won = Update_small_to_big(state)
        game_won = small_board_check(box_won)
        if game_won != " ":
            break  # Termina el bucle si hay un ganador.

        # Cambia de turno.
        is_user_turn = not is_user_turn

    # Anuncia el resultado del juego.
    if game_won == "X":
        print("You win")
    elif game_won == "O":
        print("Bot wins")
    else:
        print("It's a draw")
    return state  # Devuelve el estado final del tablero.

# Se invoca la función para iniciar el juego.
game(" " * 81, depth=6)

"""

Este es el código que utilizamos para comparar la eficiencia entre profundidades IA vs IA


def game_ai_vs_ai(state=" " * 81, initial_depth_1=7, initial_depth_2=6):
    global box_won, pos_go
    pos_go = [
        (0, 4, 8), (2, 4, 6),
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8)
    ]

    box_won = Update_small_to_big(state)
    output_tic_tac(state)
    depth_1 = initial_depth_1
    depth_2 = initial_depth_2
    move_count_1 = 0  # Contador de movimientos para la IA 1
    move_count_2 = 0  # Contador de movimientos para la IA 2
    bm = -1  # Último movimiento inicialmente inválido

    while True:
        # Turno de IA 1
        print("Jugador 1 (IA) está pensando...")
        s_time = time()
        state, bm = minimax(state, bm, "X", depth_1, s_time)
        print(f"Jugador 1 (IA) coloca en la posición {bm}")
        output_tic_tac(state)
        move_count_1 += 1

        # Aumenta la profundidad de la IA 1 cada 15 movimientos
        if move_count_1 % 15 == 0:
            depth_1 += 1
            print(f"Profundidad de búsqueda de Jugador 1 (IA) aumentada a {depth_1}.")

        box_won = Update_small_to_big(state)
        game_won = small_board_check(box_won)
        if game_won != " ":
            break

        # Turno de IA 2
        print("Jugador 2 (IA) está pensando...")
        s_time = time()
        state, bm = minimax(state, bm, "O", depth_2, s_time)
        print(f"Jugador 2 (IA) coloca en la posición {bm}")
        output_tic_tac(state)
        move_count_2 += 1

        # Aumenta la profundidad de la IA 2 cada 20 movimientos
        if move_count_2 % 20 == 0:
            depth_2 += 1
            print(f"Profundidad de búsqueda de Jugador 2 (IA) aumentada a {depth_2}.")

        box_won = Update_small_to_big(state)
        game_won = small_board_check(box_won)
        if game_won != " ":
            break

    # Anuncia el resultado del juego
    if game_won == "X":
        print("Jugador 1 (IA) gana")
    elif game_won == "O":
        print("Jugador 2 (IA) gana")
    else:
        print("Es un empate")

    return state

# Ajusta las profundidades iniciales y ejecuta el juego
game_ai_vs_ai(" " * 81, initial_depth_1=7, initial_depth_2=6)

Por último, pero no menos importante, aquí están todas las fuentes que buscamos para poder realizar este proyecto:

1) https://www.cs.us.es/~fsancho/Blog/posts/Minimax.md
2) https://keepcoding.io/blog/que-es-pygame/
3) https://youtu.be/zzOQoE9Gh80?si=jB5Xs0G_sQvXlhh-
4) https://youtu.be/xqXyEpEbUj8?si=r7zg4W31qC2igz_j
5) https://youtu.be/CcwC8tTe_QE?si=fFRGna8mUImzQ_ww
6) https://youtu.be/yE4imG5aqpU?si=EgAvNcpFhdaJh8r-
7) https://youtu.be/ZjC5PDPXnbI?si=RAMHOcjOKWYOjAZt
8) https://youtu.be/FtO_FyoR_5w?si=j01P_oEzcQ7tdpq7
9) https://youtu.be/uO5VCLwqqfw?si=MRTHbzFHHCKDS14B
10) https://www.youtube.com/watch?v=I0y-TGehf-4                                                                                             

YouTube. Recuperado el 24 de febrero de 2024, de https://youtu.be/zzOQoE9Gh80?si=jB5Xs0G_sQvXlhh-
YouTube. Recuperado el 24 de febrero de 2024, de https://youtu.be/xqXyEpEbUj8?si=r7zg4W31qC2igz_j
YouTube. Recuperado el 24 de febrero de 2024,  de https://youtu.be/CcwC8tTe_QE?si=fFRGna8mUImzQ_ww
YouTube. Recuperado el 24 de febrero de 2024, de https://youtu.be/yE4imG5aqpU?si=EgAvNcpFhdaJh8r-
YouTube. Recuperado el 25 de febrero de 2024, de https://youtu.be/ZjC5PDPXnbI?si=RAMHOcjOKWYOjAZt
YouTube. Recuperado el 25 de febrero de 2024, de https://youtu.be/FtO_FyoR_5w?si=j01P_oEzcQ7tdpq7
YouTube. Recuperado el 25 de febrero de 2024, de https://youtu.be/uO5VCLwqqfw?si=MRTHbzFHHCKDS14B
YouTube. Recuperado el 25 de febrero de 2024, de https://youtu.be/4ik99V-eXgE?si=4cDWhikBaCoaBjB9
YouTube. Recuperado el  26  de febrero de 2024 de https://youtu.be/BfmivoVFins?si=2uHx3pA6TcTOJGmy
YouTube. Recuperado el 26 de febrero de 2024, de https://youtu.be/weC1pAeh2Do?si=wFlGYHfbEx_daSHu

"""

