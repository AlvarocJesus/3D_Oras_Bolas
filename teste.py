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
    if(counter > 0):
      dado+=char
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
    elif (char == ","):
      dado += "."
      counter = 1
    else:
      dado += char

finalizar = 0
# ---------------------
dist_centro = 101
Yr = -1
print("-------------------Opções-------------------")
print("1 - Obedecer limites")
print("2 - Ignorar limites")
print("--------------------------------------------")
regras = int(input(""))

positionInitialBall = vector(X_bola[0] * 10, Y_bola[0] * 10, 0)

campo = box(pos=vector(45, 30, 0), size=vector(90, 60, 0), color=color.green)
ball = sphere(
    pos=positionInitialBall, radius=2, color=color.cyan, make_trail=True, retain=1000
)
# robo = box(pos=vector(0, 3.8, 0), size=vector(9, 7.5, 9), color=color.red)
pointer = arrow(
    pos=vector(1, 2, 0), axis=vector(50, 0, 0), shaftwidth=1, color=color.yellow
)
delimiter = ring(
    pos=positionInitialBall, axis=vector(0, 0, 1), radius=10, thickness=0.1
)



# -------------------------------Movimentaçao Bola-------------------------------
""" for i in range(1, len(X_bola)):
    sleep(0.02)
    ball.pos.x = X_bola[i] * 10
    ball.pos.y = Y_bola[i] * 10 """

#-----------------------------Calculo do ponto de encontro--------------------


""" if(escolha == 1):
	if(regras == 1):
		while((dist_centro > 91 or dist_centro < -109 or Yr < 9)):
			Xr = uniform(0.09,1.91)
			Yr = uniform(0.09,1.41)
		  
		  # Adequação ao padrão canvas
			Xr = Xr*100
			Yr = Yr*100
			Xbi = 1 * 100
			Ybi = 0.5 * 100
		  
			dist_centro = math.sqrt((Xbi-Xr)**2+(Ybi-Yr)**2)
			robo = box(x=Xr, y=Yr, size=vector(90, 75, 90), color=color.red)
	elif(regras == 2):
		Xr = uniform(0.09,8.91)
		Yr = uniform(0.09,5.91)
		
		# Adequação ao padrão canvas
		Xr = Xr*100
		Yr = Yr*100
		robo = box(x=Xr, y=Yr, size=vector(90, 75, 90), color=color.red)
        
elif(escolha == 2): """

if(regras == 1):
	while((dist_centro > 45 or dist_centro < -45 or Yr < 9)):
		Xr = float(input("Escolha o ponto X: "))
		Yr = float(input("Escolha o ponto Y: "))
          
		# Adequação ao padrão canvas
		Xr = Xr*10
		Yr = Yr*10
		Xbi = 1 * 10
		Ybi = 0.5 * 10
		print({ Xr, Yr, Xbi, Ybi })

		robo = box(pos=vector(Xr, Yr, 0), size=vector(9, 7.5, 9), color=color.red)
          
		dist_centro = math.sqrt((Xbi-Xr)**2+(Ybi-Yr)**2)
		if((dist_centro > 45 or dist_centro < -45 or Yr < 9)):
			print("Escolha invalida! Lembre-se dos limites de 1m de distância da bola.")
elif(regras == 2):
	while(True):
		Xr = float(input("Escolha o ponto X: "))
		Yr = float(input("Escolha o ponto Y: "))
          
		# Adequação ao padrão canvas
		Xr = Xr*10
		Yr = Yr*10

		if((Xr < 0.9 or Xr > 89.1) or (Yr < 0.9 or Yr > 59.1)):
			print("Escolha invalida, lembre-se dos limites do campo (9x6 m)\n")
		else:
			print(f'Xr: {Xr}, Yr: {Yr})')
			robo = box(pos=vector(Xr, Yr, 0), size=vector(9, 7.5, 9), color=color.red)
			break
        

""" for i in range(len(X_bola)):
	X_bola_teste = X_bola[i] * 100
	Y_bola_teste = Y_bola[i] * 100
      
      
	dist_robo_bola = math.sqrt((X_bola_teste-Xr)**2+(Y_bola_teste-Yr)**2)
	# ??????????????????????????????  Raio de interceptação   ????????????????????????
	# raio_interceptação = 0.15 * 100
	# dist_robo_bola -= 11.15 + raio_interceptação
      
      
	velocidade_robo = 280
	if (dist_robo_bola >= 140):
		Tr = ((dist_robo_bola-140) / velocidade_robo) + 1
	else:
		Tr = math.sqrt(dist_robo_bola*2/velocidade_robo)
        

	if(T_bola[i] >= Tr):
		Xfinal = X_bola_teste
		Yfinal = Y_bola_teste
		Tfinal = T_bola[i]
		finalizar = 2
		robo.x = Xfinal
		robo.y = Yfinal
		break
      
	if(i == 1000):
		print("Ponto de encontro inexistente!")
 """

robo.velocidade = 2.8
robo.aceleracao = 2.8
dest = 50

tempo = 0.0
dt = 2.8

while robo.pos.x < dest:
    sleep(0.028)
    robo.pos.x = (robo.velocidade * tempo) + robo.pos.x
    robo.velocidade = robo.velocidade * robo.aceleracao + robo.velocidade
    print(
	  "Robo:\ntempo: ", tempo, "\tpos:", robo.pos.x, "\tvelocidade: ", robo.velocidade
    )
    tempo += dt
