from vpython import *
import unicodedata

def remove_control_characters(s):
	return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")

trajetoria_bola = open("./Ora_bolas-trajetoria_bola_oficial.txt", "r")
dados_bola = trajetoria_bola.readlines()
trajetoria_bola.close()

trajetoria_robo = open("./trajetoria_robo.txt", "r")
dados_robo = trajetoria_robo.readlines()
trajetoria_robo.close()
traj_robo = []

# -------------------------------Formatação de dados da bola e do robo-------------------
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

# Separar os dados do robo em listas
T_robo = []
X_robo = []
Y_robo = []
teste = []
for linha in traj_robo:
  linha = linha.split(" ")
  X_robo.append(float(linha[0]))
  Y_robo.append(float(linha[1]))
  T_robo.append(float(linha[2]))
  teste.append(linha)

# -------------------------------Desenha entidades da animação-------------------
positionInitialBall = vector(X_bola[0] * 10, Y_bola[0] * 10, 2)

campo = box(pos=vector(45, 30, 0), size=vector(90, 60, 0), color=color.green)
meioCampo = cylinder(pos=vector(45, 0, 0), axis=vector(0, 60, 0), radius=0.5)
circuloCentral = ring(pos=vector(45, 30, 0), axis=vector(0, 0, 1), radius=10, thickness=0.5)

# -------------------------------Desenha gol do lado direito-------------------
travessaoGolDireito = cylinder(pos=vector(6, 25, 0), axis=vector(0, 15, 0), radius=0.5)
traveCimaGolDireito = cylinder(pos=vector(0, 25, 0), axis=vector(6, 0, 0), radius=0.5)
traveBaixoGolDireito = cylinder(pos=vector(0, 40, 0), axis=vector(6, 0, 0), radius=0.5)

# -------------------------------Desenha gol do lado esquerdo-------------------
travessaoGolEsquerdo = cylinder(pos=vector(84, 25, 0), axis=vector(0, 15, 0), radius=0.5)
traveCimaGolEsquerdo = cylinder(pos=vector(84, 25, 0), axis=vector(6, 0, 0), radius=0.5)
traveBaixoGolEsquerdo = cylinder(pos=vector(84, 40, 0), axis=vector(6, 0, 0), radius=0.5)

# ---------------------Desenha robo, bola e delimitador da condição-------------------
ball = sphere(pos=positionInitialBall, radius=2, color=color.cyan, make_trail=True, retain=1000)
robo = box(pos=vector(X_robo[0] * 10, Y_robo[0] * 10, 2.6), size=vector(2, 2, 2), color=color.red, make_trail=True, retain=1000)
delimiter = ring(pos=positionInitialBall, axis=vector(0, 0, 1), radius=10, thickness=0.1)

# ----------Movimentação da bola--------------------
# ----------Movimentação do Robô--------------------
print(f'tamanho lista X_robo: {len(X_robo)}')
for i in range(len(X_robo)):
	sleep(0.02)
	ball.pos.x = X_bola[i] * 10
	ball.pos.y = Y_bola[i] * 10

	robo.pos.x = X_robo[i] * 10
	robo.pos.y = Y_robo[i] * 10
