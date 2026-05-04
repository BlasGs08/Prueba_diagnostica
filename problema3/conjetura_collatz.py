import random

def calcular_collatz(numero_actual):
    secuencia_numeros = [str(numero_actual)]
    pico_maximo = numero_actual
    total_pasos = 0
    
    while numero_actual != 1:
        if numero_actual % 2 == 0:
            numero_actual = numero_actual // 2
        else:
            numero_actual = 3 * numero_actual + 1
        
        if numero_actual > pico_maximo:
            pico_maximo = numero_actual
            
        secuencia_numeros.append(str(numero_actual))
        total_pasos += 1
    
    return " -> ".join(secuencia_numeros), total_pasos, pico_maximo

def evaluar_intervalo(limite_inferior, limite_superior):
    if limite_superior < 100 * limite_inferior:
        print("Error: No se cumple la regla limite_superior >= 100 * limite_inferior.")
        return

    numero_mas_pasos = 0
    maxima_cantidad_pasos = 0
    numero_mayor_pico = 0
    valor_mayor_pico = 0

    for numero_evaluado in range(limite_inferior, limite_superior + 1):
        texto_secuencia, pasos_tomados, pico_alcanzado = calcular_collatz(numero_evaluado)
        
        if pasos_tomados > maxima_cantidad_pasos:
            maxima_cantidad_pasos = pasos_tomados
            numero_mas_pasos = numero_evaluado
            
        if pico_alcanzado > valor_mayor_pico:
            valor_mayor_pico = pico_alcanzado
            numero_mayor_pico = numero_evaluado
            
        print(f"Valor={numero_evaluado}:\n{texto_secuencia}\n")
        
    print(f"Numero con secuencia mas larga: {numero_mas_pasos} ({maxima_cantidad_pasos} pasos)")
    print(f"Numero con el pico mas alto: {numero_mayor_pico} (Pico de {valor_mayor_pico})")
    print("Demostrado...\n")

inicio_aleatorio = random.randint(1, 5)
fin_aleatorio = random.randint(100 * inicio_aleatorio, (100 * inicio_aleatorio) + 50)

evaluar_intervalo(inicio_aleatorio, fin_aleatorio)