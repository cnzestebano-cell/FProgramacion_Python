# =========================
# MATRIZ DE SESIONES
# Formato:
# [ID Cliente, Duración(segundos), Eventos Clics]
# =========================

sesiones = [
    [101, 250, 12],
    [102, 45, 2],
    [103, 120, 5],
    [104, 300, 10],
    [105, 80, 1]
]

# =========================
# MÓDULO / FUNCIÓN
# Calcula la clasificación
# =========================

def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


# =========================
# GENERAR INFORME
# =========================

print("=== INFORME DE COMPROMISO ===\n")

for sesion in sesiones:
    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    print(f"Cliente {id_cliente}: {clasificacion}")