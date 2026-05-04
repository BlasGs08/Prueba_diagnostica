import random

def analizar_expresion(expr):
    i = 0
    n = len(expr)
    balance_parentesis = 0
    resultado = []

    while i < n:
        c = expr[i]

        # Ignorar espacios
        if c.isspace():
            i += 1
            continue

        # Identificar NUMERO (enteros o reales con '.')
        if c.isdigit():
            token = c
            i += 1
            while i < n and (expr[i].isdigit() or expr[i] == '.'):
                token += expr[i]
                i += 1
            resultado.append(f"NUMERO {token}")
            continue

        # Identificar OPERANDO (letras seguidas de letras o números)
        if c.isalpha():
            token = c
            i += 1
            while i < n and expr[i].isalnum():
                token += expr[i]
                i += 1
            resultado.append(f"OPERANDO {token}")
            continue

        # Identificar OPERADOR, PAREN_IZQ, PAREN_DER
        if c in "+-*/":
            resultado.append(f"OPERADOR {c}")
        elif c == '(':
            resultado.append(f"PAREN_IZQ {c}")
            balance_parentesis += 1
        elif c == ')':
            resultado.append(f"PAREN_DER {c}")
            balance_parentesis -= 1
        else:
            resultado.append(f"ERROR {c}")
        
        i += 1

    # Imprimir resultado en una sola línea
    print(" ".join(resultado), end=" ")
    
    # Validar balance de paréntesis
    if balance_parentesis == 0:
        print("PARÉNTESIS BALANCEADOS.")
    else:
        print("ERROR_PARÉNTESIS_NO_BALANCEADOS.")


def generar_expresion_aleatoria():
    """Construye una cadena de expresión matemática de forma aleatoria."""
    variables = ["VALOR", "A", "B", "CONT", "X"]
    operadores = ["+", "-", "*", "/"]
    
    # Decidir cuántos términos tendrá la expresión (entre 2 y 5)
    cantidad_terminos = random.randint(2, 5)
    expr = ""
    parentesis_abiertos = 0

    for i in range(cantidad_terminos):
        # 30% de probabilidad de abrir un paréntesis
        if i < cantidad_terminos - 1 and random.random() < 0.3:
            expr += "("
            parentesis_abiertos += 1
        
        # 50% probabilidad de que sea un NUMERO, 50% de que sea un OPERANDO
        if random.choice([True, False]):
            numero = str(random.randint(1, 50))
            # 50% de que el número sea decimal
            if random.choice([True, False]):
                numero += "." + str(random.randint(1, 99))
            expr += numero
        else:
            expr += random.choice(variables)
        
        # Si hay paréntesis abiertos, 40% de probabilidad de cerrarlo aquí
        if parentesis_abiertos > 0 and random.random() < 0.4:
            expr += ")"
            parentesis_abiertos -= 1

        if i < cantidad_terminos - 1:
            expr += random.choice(operadores)

    while parentesis_abiertos > 0:
        if random.choice([True, False]):
            expr += ")"
            parentesis_abiertos -= 1
        else:
            break

    return expr

print("=== INICIANDO PRUEBAS ALEATORIAS DEL ANALIZADOR LÉXICO ===")

# probamos 3 expresiones completamente distintas
for intento in range(1, 4):
    expresion_random = generar_expresion_aleatoria()
    print(f'\nPrueba #{intento} - Analizando: "{expresion_random}"')
    analizar_expresion(expresion_random)