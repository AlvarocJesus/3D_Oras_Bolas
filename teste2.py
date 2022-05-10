from vpython import *
from random import uniform
import unicodedata
import math
import os

def remove_control_characters(s):
  return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")

tragetoria_bola = open("./trajetoria.txt", "r")
dados = tragetoria_bola.readlines()
tragetoria_bola.close()

campo = box(pos=vector(450, 300, 0), size=vector(900, 600, 0), color=color.green)

#-------------------------------Formatação de dados da bola-------------------
dados_formatados = []
for linha in dados:
  linha = remove_control_characters(linha)
  if linha == "":
    continue
  dados_formatados.append(linha)
dados_formatados.pop(0)

#Separar os dados da bola em listas
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

ball = sphere(radius=21.5, color=color.cyan, make_trail=True, retain=1000, x=X_bola[0]*100, y=Y_bola[0]*100, z=0)
print(f'Posicao bola Vetor:\n X: {X_bola[0]*100}\n Y: {Y_bola[0]*100}\n Z: {ball.pos.z}\n')

print("\n" * 130)

# robo = box(x=Xr, y=Yr, size=vector(150, 180, 150), color=color.red)

while(finalizar == 0 or finalizar == 2):
  os.system("start chrome http://localhost:8080/")
  if(finalizar == 2):
    print("\n" * 130)
    print("-------------------Dados-------------------")
    print("Ponto de inicio Robo: X {}, Y {}".format(round(Xr/100,4),round(Yr/100,4)))
    print("Ponto de encontro: X {}, Y {}".format(round(Xfinal/100,4),round(Yfinal/100,4)))
    print("Tempo de encontro: {}s".format(Tfinal))
    print("Tempo Robo: {}s".format(round(Tr,4)))
    print("Distancia Percorrida: {}m".format(round(dist_robo_bola/100,4)))
    print("-------------------------------------------")
    print()
  while(True):
    print("-------------------Opções-------------------")
    print("1 - Gerar pontos aleatórios")
    print("2 - Escolher pontos manualmente")
    print("3 - Finalizar programa")
    print("--------------------------------------------")
    escolha = int(input(""))
    print(escolha)
    
    if(escolha != 1 and escolha!= 2 and escolha!= 3):
      print("Input invalido, por favor digite novamente.\n")
    else:
      break
      
  if(escolha == 3):
    finalizar = 1
  else:
    print()
#-----------------------------Calculo do ponto de encontro--------------------
    dist_centro = 101
    Yr = -1

    print("-------------------Opções-------------------")
    print("1 - Obedecer limites")
    print("2 - Ignorar limites")
    print("--------------------------------------------")
    regras = int(input(""))

    if(escolha == 1):
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
        
        
#----------------------------------PONTO FIXO------------------------
    elif(escolha == 2):
      if(regras == 1):
        while((dist_centro > 91 or dist_centro < -109 or Yr < 9)):
          Xr = float(input("Escolha o ponto X: "))
          Yr = float(input("Escolha o ponto Y: "))
          
          # Adequação ao padrão canvas
          Xr = Xr*100
          Yr = Yr*100
          Xbi = 1 * 100
          Ybi = 0.5 * 100
          
          dist_centro = math.sqrt((Xbi-Xr)**2+(Ybi-Yr)**2)
          if((dist_centro > 91 or dist_centro < -109 or Yr < 9)):
            print("Escolha invalida! Lembre-se dos limites de 1m de distância da bola.")
      elif(regras == 2):
        while(True):
          Xr = float(input("Escolha o ponto X: "))
          Yr = float(input("Escolha o ponto Y: "))
          
          if((Xr < 0.09 or Xr > 8.91) or (Yr < 0.09 or Yr > 5.91)):
            print("Escolha invalida, lembre-se dos limites do campo (9x6 m)\n")
          else:
            break
        
        # Adequação ao padrão canvas
        Xr = Xr*100
        Yr = Yr*100
        
    for i in range(len(X_bola)):
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


#-----------------------------Tranferindo ponto de encontro para txt---------------

    # Verificando se ja existe um arquivo se sim apagar
    try:
      with open('ponto_de_encontro.txt', 'r') as f:
        os.remove('ponto_de_encontro.txt')
        arquivo = open("ponto_de_encontro.txt", "w");
    except IOError:
      arquivo = open("ponto_de_encontro.txt", "w");
      
    arquivo.write("{} {} {} {}".format(Xr,Yr, X_bola_teste, Y_bola_teste))

    arquivo.close()
    # -----------------Gera os pontos em que o robo passa para chegar na bola----------------

    # Pontos com a proporção modificada
    dist_robo_bola = dist_robo_bola
    Xr = Xr
    Yr = Yr


    X_robo = []
    Y_robo = []
    T_robo = []
    cronometro = 0.00
    sen = (Yfinal - Yr)/dist_robo_bola
    cos = (Xfinal - Xr)/dist_robo_bola
    for i in range(int(Tfinal/0.02)):
      cronometro += 0.02
      cronometro = round(cronometro,2)
      if (cronometro < 1):
        dist_ponto = (velocidade_robo*(cronometro**2))/2
      else:
        dist_ponto = velocidade_robo * cronometro
      
      X_robo.append((cos*dist_ponto) + Xr)
      Y_robo.append((sen*dist_ponto) + Yr)
      T_robo.append(cronometro)
    

    # os.system("taskkill /f /im chrome.exe")
    # -------------- Listas para serem usadas: -------------------
    
    # print("______________CORDENADAS X ROBO________________")
    # print(X_robo)
    # print("______________CORDENADAS Y ROBO________________")
    # print(Y_robo)
    # print("______________CORDENADAS T ROBO________________")
    # print(T_robo)
    
# os.system("taskkill /f /im chrome.exe")
# os.system("taskkill /f /im server.exe")