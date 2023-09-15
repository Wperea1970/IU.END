from tabulate import tabulate
import numpy as np


# Lista de estilos de aprendizaje

print("\033[1m IU. Escuela Nacional del Deporte \033[0m" )

print(" " )

print ("\033[1m Facultad de Ciencias de la Educación y  del Deporte \033[0m")

print(" ")

print ("\033[1m Programa Deporte \033[0m")

print(" ")

print ("\033[1m Curso Fundamentos Bioquímocos del Deporte \033[0m")

print(" ")

print("\033[1m  Consentimiento Informado: \033[0m")

print (" ")

print("Dado el cumplimiento de la ley 1581 del 2012 nivel nacional “por lo cual se dicta disposiciones generales para la protección de datos personales” En calidad de mis plenas facultades legales autorizo, por medio del presente documento, la utilización de mis datos en el proceso de investigación descrito en este documento. Así mismo, certifico que he sido informado de los propósitos del estudio y los fines con los que será utilizada la información recolectada mediante la encuesta planteados por el investigador. Reconozco que la información que yo provea en el curso de esta investigación es estrictamente confidencial y no será usada para ningún otro propósito fuera de los de este estudio sin mi consentimiento.")

print ("   ")

print(f"Deberás asignar un puntuación de 1 a 3, en los casilleros a cada una de las situaciones de una fila determinada, respondiendo a la pregunta del encabezamiento. Coloca 3 puntos a la situación que te reporte más beneficios cuando aprendes, y asigna los puntajes“3”, “2” y “0” a las restantes situaciones expuestas en la fila, en función de la efectividad quetienen éstas en tu forma de aprender. No se puede repetir un puntaje dentro de una fila.")

print (" ")


Nombres = ("Digite nombres y apellidos: ")
Nombres= input("\033[1m Digite nombres y apellidos: ")
print(" ")

Género = ("\033[1m Digite el genero:\033[0m")
Género = input("\033[1m Digite el genero: \033[0m")
print(" ")

Edad = ("\033[1mDigite la edad:\033[0m")
Edad= input("\033[1m Digite la edad: \033[0m")
print(" ")

Grupo= ("Digite el grupo: ")
Grupo = input("\033[1m Digite el grupo: \033[0m")
print(" ")


estilos_aprendizaje = [

    ["\033[1m Cuando aprendo:\033[0m"],

    ["Prefiero valerme de mis\nsensaciones y sentimientos"],
    ["Prefiero mirar y atender"],
    ["Prefiero pensar en las ideas"],
    ["Prefiero hacer cosas"],
    
 ["\033[1m Aprendo mejor cuando:\033[0m",
    "Confío en mis\ncorazonadas\ny sentimientos",
    "Atiendo y\nobservo\ncuidadosamente",
    "Confío en mis\npensamientos\nlógicos",
    "Trabajo duramente\npara que las cosas\nqueden realizadas:"],

 [ "\033[1m Cuando estoy aprendiendo:\033[0m"],
   [ "Tengo sentimientos\ny reacciones\nfuertes"],
    ["Soy reservado\n y tranquilo"],
    ["Busco razonar\n sobre las cosas\n que están\n sucediendo"],
   [ "Me siento\nresponsable\nde las cosas"],
  
 [ "\033[1m Aprendo a trevés de:\033[0m"],
    ["Sentimientos"],
    ["Observaciones"],
    ["Razonamientos"],
    ["Acciones"], 

 [
 "\033[1m Cuando aprendo:\033[0m"],
["Estoy abierto\na nuevas\nexperiencias"],
 ["Tomo en cuenta\ntodos los\naspectos\nrelacionados"],
 ["Prefiero analizar\nlas cosas\ndividiéndolas\nen sus partes\ncomponentes"],
 ["Prefiero hacer\nlas cosas\ndirectamente"],



 ["\033[1m Cuando estoy aprendiendo:\033[0m"],
 ["Soy una persona\nintuitiva"],
 ["Soy una persona\nobservadora"],
 ["Soy una persona\nlógica"],
 [" Soy una persona\nactiva"],



 ["\033[1m Aprendo mejor a través de:\033[0m"],
 ["Las relaciones\ncon mis\ncompañeros"],
 ["La observación","Teorías racionales"],
[ "La práctica\nde los temas\ntratados"],


[ "\033[1m Cuando aprendo:\033[0m"],
 ["Me siento\ninvolucrado en los\ntemas tratados"],
 ["Me tomo mi tiempo\nantes de actuar"],
 ["Prefiero las teorías\ny las ideas"],
 ["Prefiero ver los\nresultados a través de\nmi propio trabajo"],


["\033[1m Aprendo mejor cuando:\033[0m"],
 ["Me baso en mis\n intuiciones y\n sentimientos"],
 ["Me baso en\nobservaciones\npersonales"],
 ["Tomo en cuenta\nmis propias ideas\nsobre el tema"],
 ["Pruebo\npersonalmente\nla tarea"],


["\033[1m Cuando estoy aprendiendo:\033[0m "],
 ["Soy una persona\nabierta"],
 ["Soy una persona\nreservada"],
 ["Soy una persona\nracional"],
 ["Soy una persona\nresponsable"],
 

[
 "\033[1m Cunado aprendo:\033[0m"],
 ["Me involucro"],
 ["Prefiero observar"],
 ["Prefiero evaluar\n las cosas:"],
 ["Prefiero asumir\nuna actitud activa"],

[
 "\033[1m Aprendo cuando:\033[0m"],
 ["Soy receptivo\ny de mente\nabierta:"],
 ["Soy cuidadoso","Analizo las ideas:"],
 ["Soy práctico:"],
 
]

# Crear una lista para almacenar las calificaciones
calificaciones = []

# Recopilar calificaciones para cada estilo de aprendizaje
for estilo in estilos_aprendizaje:

    puntuacion = int(input(f"Puntuación de 0 a 3 para el estilo de aprendizaje '{estilo}': "))
    
    while puntuacion < 0 or puntuacion > 3:

        print("0 a 3.")
        puntuacion = int(input(f"Puntuación de 0 a 3 para el estilo de aprendizaje '{estilo}': "))
    
    calificaciones.append([estilo, puntuacion])
   
# Imprimir la tabla con las calificaciones utilizando tabulate

headers = ["\033[1m Estilo de aprendizaje IU.END TEST KOLB\033[0m", "Puntuación"]
print(np.array(calificaciones).shape)
print(tabulate(calificaciones, headers, tablefmt="grid"))

suma_total = sum(puntuacion for estilo, puntuacion in calificaciones)
print("\033[1m \nSuma total de las calificaciones: \033[1m", suma_total)