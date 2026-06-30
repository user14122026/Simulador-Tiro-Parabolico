# primero pedimos los datos
h0 = float(input("Introduce la altura inicial en metros: "))
v0 = float(input("Introduce la velocidad inicial en metros por segundo: "))
angulo = float(input("Introduce el grado de inclinación del lanzamiento: "))
# el float lo utilizamos para clambiar de texto a numero en python

# ahora vamos a cambiar el angulo a radianes (python trabaja con radianes)
import math    # esto es por lo del numero pi para el vocabulario de matematicas
angulo_rad = angulo*(math.pi/180)

# vamos a descomponer la v0
v0X = v0 * (math.cos(angulo_rad))
v0Y = v0 * (math.sin(angulo_rad))

# vamos a calcular el tiempo
t = 0
dt= 0.1

# aqui definimos la gravedad
planeta = input("Elige el planeta: Tierra, Luna, Marte, Sol: ")
if planeta == "Tierra":
 g = 9.8
if planeta == "Luna":
 g = 1.62
if planeta == "Marte":
 g = 3.72
if planeta == "Sol":
 g = 274

# creamos las listas para guardar la posicion
x = []
y = []

pos_x = 0
pos_y = h0

# ahora vamos a crear el bucle
while pos_y >= 0:
 pos_x = v0X * t
 pos_y = h0 + v0Y * t - 0.5 * g * t**2
 # ahora hacemos que la posicion en x,y se guarde en las listas creadas
 x.append(pos_x)
 y.append(pos_y)
 t = t + dt

# ahora vamos a representar la parabola
import matplotlib.pyplot as plt

plt.plot(x, y)
plt.xlabel("Distancia horizontal (m)")
plt.ylabel("Altura (m)")
plt.title("Simulación de tiro parabólico")
plt.grid(True)

# vamos a clacular la altura maxima
altura_max = max(y)
indice_max = y.index(altura_max)
alcance_max = x[-1]
inicio_x = x[0]
inicio_y = y[0]

# por ultimo marcamos los puntos clave dentro de la grafica
plt.scatter(inicio_x, inicio_y, color="green", label="Inicio")
plt.scatter(x[indice_max], altura_max, color="red", label="Altura máxima")
plt.scatter(alcance_max, 0, color="orange", label="Alcance máximo")
plt.text(inicio_x, inicio_y, f"Inicio ({inicio_x:.1f}, {inicio_y:.1f})", color="green", fontsize=9, ha="left", va="bottom")
plt.text(x[indice_max], altura_max, f"Altura máx = {altura_max:.1f} m", color="red", fontsize=9, ha="left", va="bottom")
plt.text(alcance_max, 0, f"Alcance máx = {alcance_max:.1f} m", color="orange", fontsize=9, ha="right", va="top")
plt.legend()

plt.show()