import datetime as dt
import time
import os

fecha = dt.date.today()
print(f"Fecha actual: {fecha}")

cant = int(input("¿Cuántas notas? "))

suma = 0
for i in range(cant):
    nota = int(input(f"Ingresa la calificación {i+1}: "))
    suma += nota

promedio = suma / cant

os.system("cls||clear")
pasos = 10
for cont in range(1, pasos + 1):
    puntos = "." * cont  # 
    porcentaje = cont * 10
    print(f"Calculando promedio{puntos} {porcentaje}%")
    time.sleep(0.5)


print("Cálculo finalizado.")
time.sleep(1)
print(f"El promedio es: {promedio:.2f}")