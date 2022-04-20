import numpy as np
import RPi.GPIO as GPIO 
import time 
#Establecemos que vamos a trabjar en modo BCM 
GPIO.setmode(GPIO.BCM)

#Funcion de movimiento de motor 1
def movimiento(paso1,paso2,paso3,paso4,delay,i):
  #configuramos el pin GPIO como entrada y salida
  GPIO.setup(paso1, GPIO.OUT)
  GPIO.setup(paso2, GPIO.OUT)
  GPIO.setup(paso3, GPIO.OUT)
  GPIO.setup(paso4, GPIO.OUT)

  #Ingresamos a un lazo infinito
  while i<500:
  # -------- LAZO INFINITO -------- 
    GPIO.output(paso1, GPIO.HIGH)
    GPIO.output(paso2, 0)
    GPIO.output(paso3, 0)
    GPIO.output(paso4, 0)

    time.sleep(delay)

    GPIO.output(paso1, 0)
    GPIO.output(paso2, GPIO.HIGH)
    GPIO.output(paso3, 0)
    GPIO.output(paso4, 0)

    time.sleep(delay)

    GPIO.output(paso1, 0)
    GPIO.output(paso2, 0)
    GPIO.output(paso3, GPIO.HIGH)
    GPIO.output(paso4, 0)

    time.sleep(delay)

    GPIO.output(paso1, 0)
    GPIO.output(paso2, 0)
    GPIO.output(paso3, 0)
    GPIO.output(paso4, GPIO.HIGH)

    time.sleep(delay)

    #contador
    i=i+1
"""""
giros=0
while giros<2:
  #Utilizo la funcion movimiento para mover el motor Y hacia abajo
  movimiento(14,15,18,23,0.002,0)
  #Utilizo la funcion movimiento para mover el motor X hacia la derecha
  movimiento(2,3,4,17,0.002,500)
  #Utilizo la funcion movimiento para mover el motor hacia arriba
  movimiento(23,18,15,14,0.002,0)
  #Utilizo la funcion movimiento para mover el motor X hacia la derecha
  movimiento(2,3,4,17,0.002,500)
  giros=giros+1
"""
matriz = [
  [1,0,0],
  [0,1,0],
  [1,0,0]]
print (matriz)

def busqueda(col):
  ult_paso=0
  pos_anterior=0
  if((matriz[0][col])==1):
    mov=1
    pos_anterior=1
    pasos=0
    while pasos<mov:
      movimiento(14,15,18,23,0.002,0)#abajo
      pasos=pasos+1
    print(mov)
    time.sleep(2)
    ult_paso=1
  else:
    print('0')

  if((matriz[1][col])==1):
    mov=2-pos_anterior
    pasos=0
    while pasos<mov:
      movimiento(14,15,18,23,0.002,0)#abajo
      pasos=pasos+1
    print(mov)
    pos_anterior=2
    time.sleep(2)
    ult_paso=2
  else:
    print('0')

  if((matriz[2][col])==1):
    mov=3-pos_anterior
    pasos=0
    while pasos<mov:
      movimiento(14,15,18,23,0.002,0)#abajo
      pasos=pasos+1
    print(mov)
    time.sleep(2)
    ult_paso=3
  else:
    print('0')
  
  j=0
  print("")
  print(ult_paso)
  while j<ult_paso:
    j=j+1
    movimiento(23,18,15,14,0.002,0)#arriba

busqueda(0)
movimiento(2,3,4,17,0.002,0)#derecha
print("Derecha")
busqueda(1)
movimiento(2,3,4,17,0.002,0)#derecha
print("Derecha")
busqueda(2)
movimiento(17,4,3,2,0.002,0)#izquierda
movimiento(17,4,3,2,0.002,0)#izquierda