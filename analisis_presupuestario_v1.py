# Definición de Estructura de Datos (Lista de Diccionarios)
# Requisito: Utilizar estructuras de datos apropiadas (Listas, Diccionarios)

DATOS_PROYECTOS = [
    {
        "nombre": "Proyecto 1: Sistema de Gestión Municipal (Django)",
        "presupuesto_inicial": 40000000,  # Requisito: Tipos de datos (Enteros/Flotantes)
        "gasto_acumulado": 38000000,
        "estado": "En curso",
        "prioritario": True
    },
    {
        "nombre": "Proyecto 2: Dashboard interactivo de datos territoriales",
        "presupuesto_inicial": 20000000,
        "gasto_acumulado": 20000000,
        "estado": "Finalizado",
        "prioritario": False
    },
    {
        "nombre": "Programa Seguridad y Oportunidades",
        "presupuesto_inicial": 15402104,
        "gasto_acumulado": 11795942,
        "estado": "En curso",
        "prioritario": True
    }
]

# Requisito: Codificar un programa utilizando funciones
def calcular_metricas(proyectos: list) -> dict:
    # Requisito: Utilizar variables y operadores
    ppto_total = 0
    gasto_total = 0
    proyectos_activos = 0
    
    # Requisito: Utilizar sentencias iterativas (bucle for)
    for proyecto in proyectos:
        ppto_total = ppto_total + proyecto["presupuesto_inicial"]
        gasto_total = gasto_total + proyecto["gasto_acumulado"]
        
        # Requisito: Utilizar sentencias condicionales (if)
        if proyecto["estado"] == "En curso":
            proyectos_activos = proyectos_activos + 1

    saldo_disponible = ppto_total - gasto_total
    
    # Requisito: Distinguir tipos de datos (retorno de diccionario)
    return {
        "proyectos_totales": len(proyectos),
        "proyectos_activos": proyectos_activos,
        "ppto_total_clp": ppto_total,
        "gasto_acumulado_clp": gasto_total,
        "saldo_disponible_clp": saldo_disponible
    }

def mostrar_reporte(metricas: dict):
    # Requisito: Crear un programa que implemente variables y estructuras básicas
    
    # Simulación de información del usuario (Requisito: Formulario simple/Distinguir tipos de datos)
    usuario_nombre = "Patricia Vidal Uribe"
    usuario_rol = "Especialista en Análisis de Datos"
    print(f"--- Dashboard Básico de Gestión Municipal ---")
    print(f"Generado por: {usuario_nombre} ({usuario_rol})")
    print("---------------------------------------------")

    print(f"1. Proyectos Totales: {metricas['proyectos_totales']}")
    print(f"2. Proyectos Activos: {metricas['proyectos_activos']}")
    
    # Mostrar resultados del cálculo
    print("\n--- Resumen Presupuestario (en Pesos Chilenos) ---")
    print(f"Ppto. Inicial Total: ${metricas['ppto_total_clp']:,}")
    print(f"Gasto Acumulado Total: ${metricas['gasto_acumulado_clp']:,}")
    
    # Requisito: Utilizar sentencias condicionales (if/elif/else) para la toma de decisiones
    if metricas['saldo_disponible_clp'] < 0:
        print(f"¡ALERTA! Saldo Disponible: (${abs(metricas['saldo_disponible_clp']):,})")
        print("ESTADO: Se ha excedido el presupuesto total.")
    elif metricas['saldo_disponible_clp'] < metricas['ppto_total_clp'] * 0.1:
        print(f"ADVERTENCIA: Saldo Disponible: ${metricas['saldo_disponible_clp']:,}")
        print("ESTADO: Bajo saldo disponible (menos del 10% restante).")
    else:
        print(f"Saldo Disponible: ${metricas['saldo_disponible_clp']:,}")
        print("ESTADO: Saldo operativo normal.")

def generar_alerta_gasto(proyectos: list):
    print("\n--- Seguimiento de Gasto por Proyecto ---")
    # Requisito: Utilizar sentencias iterativas (bucle for)
    for proyecto in proyectos:
        # Requisito: Utilizar variables y operadores (Cálculo de porcentaje de gasto)
        gasto_ratio = (proyecto["gasto_acumulado"] / proyecto["presupuesto_inicial"]) * 100
        
        # Requisito: Utilizar sentencias condicionales (if/elif)
        if gasto_ratio >= 90:
            print(f"ALERTA GASTO: El proyecto '{proyecto['nombre']}' ha consumido el {gasto_ratio:.2f}% de su presupuesto inicial.")
        elif proyecto["prioritario"]:
            print(f"INFO Prioritario: '{proyecto['nombre']}' lleva un consumo del {gasto_ratio:.2f}%.")
        else:
            pass

# Punto de entrada del programa
if __name__ == "__main__":
    metricas = calcular_metricas(DATOS_PROYECTOS)
    mostrar_reporte(metricas)
    generar_alerta_gasto(DATOS_PROYECTOS)