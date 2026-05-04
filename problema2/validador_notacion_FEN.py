import re
import random

def validar_fen(C):
    """
    Dado una cadena C, valida si se encuentra en notación FEN 
    (Forsyth-Edwards Notation).
    """
    # Expresión regular para validar el formato estándar FEN
    patron_fen = r"^([rnbqkpRNBQKP1-8]+\/){7}[rnbqkpRNBQKP1-8]+ [wb] (-|[KQkq]+) (-|[a-h][36]) \d+ \d+$"
    
    if re.match(patron_fen, C):
        return True
    return False

def realizar_pruebas_aleatorias():
    # Banco de cadenas FEN VÁLIDAS (posiciones reales de ajedrez)
    fens_validos = [
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", # Posición inicial
        "r1bqkbnr/pp1ppppp/2n5/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3", # Defensa Siciliana
        "8/8/8/4k3/8/8/4K3/8 w - - 0 1", # Final de Reyes
        "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1", # Con captura al paso
        "r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1" # Posición compleja
    ]

    # Banco de cadenas FEN INVÁLIDAS (errores comunes de sintaxis)
    fens_invalidos = [
        "esta no es una cadena fen", # Texto aleatorio
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -", # Faltan los contadores de turnos
        "rnbqkbnr/xxpppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", # Contiene piezas inválidas 'x'
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP w KQkq - 0 1", # Faltan filas (no hay 8 bloques)
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR z KQkq - 0 1", # Turno inválido 'z' (debe ser w o b)
    ]

    # Tomamos 2 cadenas válidas al azar y 2 inválidas al azar para la prueba
    casos_de_prueba = random.sample(fens_validos, 2) + random.sample(fens_invalidos, 2)
    
    # Mezclamos la lista para que el orden de evaluación también sea aleatorio
    random.shuffle(casos_de_prueba)

    print("="*60)
    print("   VALIDADOR DE NOTACIÓN FEN (Forsyth-Edwards Notation)")
    print("="*60)

    # Evaluamos cada cadena C
    for i, C in enumerate(casos_de_prueba, 1):
        es_valido = validar_fen(C)
        
        print(f"\n[Prueba {i}]")
        print(f"Cadena C  : {C}")
        
        if es_valido:
            print("Resultado : VÁLIDO (Cumple con el estándar FEN)")
        else:
            print("Resultado : INVÁLIDO (Sintaxis FEN incorrecta)")
            
    print("\n" + "="*60 + "\n")

realizar_pruebas_aleatorias()