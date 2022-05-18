import tornado
from vpython import *
from random import uniform
import unicodedata
import math
import os

def remove_control_characters(s):
	return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")

trajetoria_bola = open("./trajetoria.txt", "r")
dados_bola = trajetoria_bola.readlines()
trajetoria_bola.close()

trajetoria_robo = open("./trajetoria_robo.txt", "r")
dados_robo = trajetoria_robo.readlines()
trajetoria_robo.close()
traj_robo = []

# -------------------------------Formatação de dados da bola-------------------
dados_formatados = []
for linha in dados_bola:
	linha = remove_control_characters(linha)
	if linha == "":
		continue
	dados_formatados.append(linha)
dados_formatados.pop(0)

for linha in dados_robo:
	linha = linha.strip()
	traj_robo.append(linha)
traj_robo.pop(0)

# Separar os dados da bola em listas
T_bola = []
X_bola = []
Y_bola = []
for linha in dados_formatados:
	counter = 0
	tipo = 0
	dado = ""
	for char in linha:
		if counter > 0:
			dado += char
			if counter == 2 and tipo == 0:
				T_bola.append(float(dado))
				tipo = 1
				dado = ""
				counter = 0
			elif counter == 3 and tipo == 1:
				X_bola.append(float(dado))
				tipo = 2
				dado = ""
				counter = 0
			elif counter == 3 and tipo == 2:
				Y_bola.append(float(dado))
				tipo = 0
				dado = ""
				counter = 0
			if counter > 0:
				counter += 1
		elif char == ",":
			dado += "."
			counter = 1
		else:
			dado += char

finalizar = 0

T_robo = []
X_robo = []
Y_robo = []
teste = []
for linha in traj_robo:
  linha = linha.split(" ")
  T_robo.append(float(linha[0]))
  X_robo.append(float(linha[1]))
  Y_robo.append(float(linha[2]))
  teste.append(linha)

positionInitialBall = vector(X_bola[0] * 10, Y_bola[0] * 10, 2)

campo = box(pos=vector(45, 30, 0), size=vector(90, 60, 0), color=color.green)
ball = sphere(pos=positionInitialBall, radius=2, color=color.cyan, make_trail=True, retain=1000)
robo = box(pos=vector(X_robo[0] * 10, Y_robo[0] * 10, 2.6), size=vector(5, 5, 5), color=color.red, make_trail=True, retain=1000)
delimiter = ring(pos=positionInitialBall, axis=vector(0, 0, 1), radius=10, thickness=0.1)

# ----------Movimentação da bola--------------------
# ----------Movimentação do Robô--------------------
for i in range(len(X_bola)):
	sleep(0.02)
	ball.pos.x = X_bola[i] * 10
	ball.pos.y = Y_bola[i] * 10

	robo.pos.x = X_robo[i] * 10
	robo.pos.y = Y_robo[i] * 10

	print(f'T_bola[i]: {T_bola[i]} \nT_robo[-1]: {T_robo[i]}')
	if T_bola[i] >= T_robo[i]:
		print(f'T_bola[i]: {T_bola[i]} \nT_robo[-1]: {T_robo[i]}')
		robo.pos.x = X_bola[i] * 10
		robo.pos.y = Y_bola[i] * 10
		break

	if i == 100:
		print("Ponto de encontro inexistente!")