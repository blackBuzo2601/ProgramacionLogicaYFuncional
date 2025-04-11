#20760257
#BUZO ZAMORA ELIAN
#11/04/2025
#PROGRAMACIÓN LÓGICA Y FUNCIONAL
#ALGORITMO DE LAS N REINAS MIGRADO A PYTHON
N = 4
#Creamos la matriz de 4 x 4
board = [[0 for _ in range(N)] for _ in range(N)]
#Arreglo para imprimir las n reinas
queens = [[-1, -1] for _ in range(N)]

def valid_state(row, col, current_queen):
    for q in range(current_queen):
        q_row, q_col = queens[q]  #desestructuramos ese arreglo, obtenemos los valores
        if row == q_row or col == q_col or abs(q_row - row) == abs(q_col - col):
            return False
    return True

def n_queens(current_queen, current_col):
    print(f"\n==> Iteración: Reina {current_queen}, Columna {current_col}")
    print("-" * 60)

    if current_queen >= N:
        print("Todas las reinas se colocaron correctamente.")
        return True

    found = False
    row = 0
    
    while row < N and not found: #negamos found !found
        print(f"Intentando colocar la reina {current_queen} en renglón {row}, columna {current_col}...")
        
        if valid_state(row, current_col, current_queen):
            # Guardar la posición de la reina
            queens[current_queen][0] = row
            queens[current_queen][1] = current_col
            board[row][current_col] = 1  # Marcar en el tablero
            
            # Mostrar tablero temporal
            print_board()

            ##llamada recursiva y guardar resultado en found (True o false)
            found = n_queens(current_queen + 1, current_col + 1)
            if not found: #Si nos devolvió false hacer backtracking
                # Backtracking: deshacer la jugada
                board[row][current_col] = 0
                queens[current_queen] = [-1, -1]
                print(f" Retrocediendo desde reina {current_queen} en renglón {row}, columna {current_col}")
        else:
            print(f" No se puede colocar en ({row}, {current_col})")
        row += 1

    return found

def print_board():
    for fila in board:
        print(" ".join(str(celda) for celda in fila))
    print()

print(f"Resolviendo el problema de las {N} Reinas...\n")
n_queens(0, 0)
print("\nTablero final con las reinas colocadas (1 = reina):")
print_board()

