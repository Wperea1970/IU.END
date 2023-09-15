from tabulate import tabulate
import numpy as np

# Lista de estilos de aprendizaje
estilos_aprendizaje = [
    "\033[1m Cuando aprendo:\033[0m",
    "Prefiero valerme de mis\nsensaciones y sentimientos",
    "Prefiero mirar y atender",
    "Prefiero pensar en las ideas",
    "Prefiero hacer cosas",
    "\033[1m Aprendo mejor cuando:\033[0m",
    "Confío en mis\ncorazonadas\ny sentimientos",
    "Atiendo y\nobservo\ncuidadosamente",
    "Confío en mis\npensamientos\nlógicos",
    "Trabajo duramente\npara que las cosas\nqueden realizadas:",
    # ... Añade el resto de los estilos de aprendizaje aquí
]

# Crear una lista para almacenar las calificaciones
calificaciones = []

# Recopilar calificaciones para cada estilo de aprendizaje
for estilo in estilos_aprendizaje:
    puntuacion = int(input(f"Puntuación de 0 a 3 para el estilo de aprendizaje '{estilo}': "))
    
    while puntuacion < 0 or puntuacion > 3:
        print("La puntuación debe estar entre 0 y 3.")
        puntuacion = int(input(f"Puntuación de 0 a 3 para el estilo de aprendizaje '{estilo}': "))
    
    calificaciones.append([estilo, puntuacion])
   
# Imprimir la tabla con las calificaciones utilizando tabulate
headers = ["\033[1m Estilo de aprendizaje IU.END TEST KOLB\033[0m", "Puntuación"]
print(tabulate(calificaciones, headers, tablefmt="grid"))

# Calcular la suma total de las calificaciones
suma_total = sum(puntuacion for estilo, puntuacion in calificaciones)
print("\nSuma total de las calificaciones:", suma_total)

# Aquí puedes realizar análisis o tomar decisiones basadas en las calificaciones.
