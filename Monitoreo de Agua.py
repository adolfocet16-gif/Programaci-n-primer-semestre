"""
Sistema de Red de Monitoreo de Calidad del Agua en Acueductos.
Cumple con: Vectores, Matrices, Sets/Dicts, Búsquedas (Lineal/Binaria),
Persistencia de Archivos y manejo de Excepciones.
"""

def main():
    print("--- INICIANDO SISTEMA DE MONITOREO DE AGUA ---")

    # 1. Estructuras Estáticas (Vectores y Matrices) - 4%
    # Vector: Almacena mediciones secuenciales de pH de una estación en el tiempo.
    vector_mediciones_ph = [7.1, 7.2, 7.5, 6.8, 8.1, 7.4, 6.5]
    print(f"Mediciones de pH (Vector): {vector_mediciones_ph}")

    # Matriz: Modela la ubicación geográfica de los sensores en la ciudad (cuadrícula 3x3).
    # Cada celda contiene el ID del sensor.
    matriz_sensores = [
        ["S01", "S02", "S03"],
        ["S04", "S05", "S06"],
        ["S07", "S08", "S09"]
    ]
    print(f"Ubicación de sensores (Matriz): Fila 1: {matriz_sensores[0]}")

    # 2. Colecciones Dinámicas (Sets y Diccionarios) - 4%
    # Conjuntos (Sets): Filtran IDs de nodos defectuosos para no tomarlos en cuenta.
    todos_los_nodos = {"S01", "S02", "S03", "S04", "S05"}
    nodos_defectuosos = {"S02", "S04"}
    
    # Operación de conjuntos para obtener los nodos activos y sanos
    nodos_activos = todos_los_nodos.difference(nodos_defectuosos)
    print(f"Nodos defectuosos (Set): {nodos_defectuosos}")
    print(f"Nodos activos filtrados: {nodos_activos}")

    # Diccionario: Guarda información detallada de una anomalía
    alerta = {"sensor": "S03", "tipo": "turbidez_alta", "valor": 9.5}

    # 3. Algoritmos (Búsqueda Lineal y Binaria) - 4%
    anomalias_quimicas = [8.1, 9.2, 6.1, 5.5, 10.4] # Lista desordenada
    
    # Búsqueda Lineal: Buscar el valor 6.1 en la lista desordenada
    valor_a_buscar_lineal = 6.1
    encontrado_lineal = False
    for valor in anomalias_quimicas:
        if valor == valor_a_buscar_lineal:
            encontrado_lineal = True
            break
    print(f"Búsqueda Lineal: ¿Anomalía {valor_a_buscar_lineal} detectada? {encontrado_lineal}")

    # Búsqueda Binaria: Requiere una lista ordenada
    anomalias_ordenadas = sorted(anomalias_quimicas) # [5.5, 6.1, 8.1, 9.2, 10.4]
    valor_a_buscar_binaria = 9.2
    
    inicio = 0
    fin = len(anomalias_ordenadas) - 1
    encontrado_binaria = False

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if anomalias_ordenadas[medio] == valor_a_buscar_binaria:
            encontrado_binaria = True
            break
        elif anomalias_ordenadas[medio] < valor_a_buscar_binaria:
            inicio = medio + 1
        else:
            fin = medio - 1
            
    print(f"Búsqueda Binaria: ¿Anomalía {valor_a_buscar_binaria} detectada en {anomalias_ordenadas}? {encontrado_binaria}")

    # 4. Persistencia (Archivos y Excepciones I/O) - 4%
    # Guardamos una bitácora de las alertas críticas en un archivo de texto
    guardar_bitacora("S06", "pH peligrosamente bajo (6.1)")


def guardar_bitacora(sensor, mensaje):
    """Guarda una alerta en un archivo de texto manejando excepciones."""
    nombre_archivo = "bitacora_alertas.txt"
    try:
        # Modo 'a' (append) para no borrar alertas anteriores
        with open(nombre_archivo, "a") as archivo:
            archivo.write(f"ALERTA CRÍTICA - Sensor {sensor}: {mensaje}\n")
        print(f"Persistencia: Alerta guardada exitosamente en '{nombre_archivo}'.")
    except IOError as e:
        print(f"Error de I/O al intentar guardar la bitácora: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado al guardar el archivo: {e}")

# Punto de entrada estándar en Python (Buenas Prácticas PEP 8)
if __name__ == "__main__":
    main()