from vpython import *
from random import uniform
import unicodedata
import math
import os

# ----teste ------
def remove_control_characters(s):
	return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")


tragetoria_bola = open("./trajetoria.txt", "r")
# tragetoria_bola = open("./Ora_bolas-trajetoria _bola_oficial.txt", "r")
dados = tragetoria_bola.readlines()
tragetoria_bola.close()

# -------------------------------Formatação de dados da bola-------------------
dados_formatados = []
for linha in dados:
	linha = remove_control_characters(linha)
	if linha == "":
		continue
	dados_formatados.append(linha)
dados_formatados.pop(0)

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
# ---------------------
Yr = -1
print("Digite os pontos iniciais do robo:")
Xr = float(input("Escolha o ponto X: "))
Yr = float(input("Escolha o ponto Y: "))

# Adequação ao padrão canvas
Xr = Xr * 10
Yr = Yr * 10

positionInitialBall = vector(X_bola[0] * 10, Y_bola[0] * 10, 0)

campo = box(pos=vector(45, 30, 0), size=vector(90, 60, 0), color=color.green)
ball = sphere(pos=positionInitialBall, radius=2, color=color.cyan, make_trail=True, retain=1000)
robo = box(pos=vector(Xr, Yr, 0), size=vector(10, 10, 10), color=color.red, make_trail=True, retain=1000)
pointer = arrow(pos=vector(1, 2, 0), axis=vector(50, 0, 0), shaftwidth=1, color=color.yellow)
delimiter = ring(pos=positionInitialBall, axis=vector(0, 0, 1), radius=10, thickness=0.1)

# ----------Calculo do ponto de encontro--------------------
# ----------Movimentação da bola--------------------
# ----------Movimentação do Robô--------------------
for i in range(len(X_bola)):
	X_bola_teste = X_bola[i] * 10
	Y_bola_teste = Y_bola[i] * 10

	sleep(0.02)
	ball.pos.x = X_bola[i] * 10
	ball.pos.y = Y_bola[i] * 10

	dist_robo_bola = math.sqrt((X_bola_teste - Xr) ** 2 + (Y_bola_teste - Yr) ** 2)

	velocidade_robo = 280 / 10
	if dist_robo_bola >= (140 / 10):
		Tr = ((dist_robo_bola - (140 / 10)) / velocidade_robo) + 1
	else:
		Tr = math.sqrt(dist_robo_bola * 2 / velocidade_robo)

	if T_bola[i] >= Tr:
		robo.pos.x += 1
		robo.pos.y += 1
		Xfinal = X_bola_teste
		Yfinal = Y_bola_teste
		Tfinal = T_bola[i]
		finalizar = 2
		robo.pos.x = Xfinal
		robo.pos.y = Yfinal
		break

	if i == 100:
		print("Ponto de encontro inexistente!")
