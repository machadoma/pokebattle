from socket import *
import pickle
import os 

serverPort = 27123
serverSocket = socket(AF_INET, SOCK_STREAM)
HOST = '127.0.0.1'
serverSocket.bind(("", serverPort))
serverSocket.listen(5)
print("Aguardando outro jogador\n")
connectionSocket, addr = serverSocket.accept()

pkmon = ["Bulbasaur", "Charmander", "Squirtle"]
escolha = 4
md5 = 1
vic = 0
lose = 0


print("Escolha seu pokémon 1 - Bulbasaur, 2 - Charmander ou 3 - Squirtle.\n")
print("Bulbasaur > Squirtle > Charmander > Bulbasaur")

while (md5 <= 5) or (vic <= 3) or (lose <= 3):
    if (md5 > 5) or (vic >= 3) or (lose >= 3):
        break
    while escolha <=0 or escolha >=4:
        print(f"Rodada: {md5}")
        print(f"Placar Vitorias: {vic} x {lose} : Derrotas")
        escolha = int(input("Escolha seu pokémonfrom socket import *
import pickle
import os 

serverPort = 27123
serverSocket = socket(AF_INET, SOCK_STREAM)
HOST = '127.0.0.1'
serverSocket.bind(("", serverPort))
serverSocket.listen(5)
print("Aguardando outro jogador\n")
connectionSocket, addr = serverSocket.accept()

pkmon = ["Bulbasaur", "Charmander", "Squirtle"]
escolha = 4
md5 = 1
vic = 0
lose = 0


print("Escolha seu pokémon 1 - Bulbasaur, 2 - Charmander ou 3 - Squirtle.\n")
print("Bulbasaur > Squirtle > Charmander > Bulbasaur")

while (md5 <= 5) or (vic <= 3) or (lose <= 3):
    if (md5 > 5) or (vic >= 3) or (lose >= 3):
        break
    while escolha <=0 or escolha >=4:
        print(f"Rodada: {md5}")
        print(f"Placar Vitorias: {vic} x {lose} : Derrotas")
        escolha = int(input("Escolha seu pokémon, opções válidas de 1 a 3: "))
        
        

    received = connectionSocket.recv(1024)
    escolhaini = int.from_bytes(received, byteorder="little")

    if(escolha == escolhaini):
        response = "Empate"
        print("Empate")
       
    if((escolha== 2 and escolhaini == 1) or (escolha== 1 and escolhaini == 3) or (escolha== 3 and escolhaini == 2)):
        response = "Derrota"
        print("Você Venceu")
        md5 += 1
        vic += 1
      
    if ((escolha == 1 and escolhaini == 2) or (escolha == 3 and escolhaini == 1) or (escolha == 2 and escolhaini == 3)):
        response = "Vitória"
        print("Você Perdeu")
        lose += 1
        md5 += 1
        
    connectionSocket.send(pickle.dumps(response))
    escolha = 4
 


if (md5 >= 5):
        print('Jogo encerrado')
   
if (vic >= 3 ):
        print('Você mostrou quem é o mestre pokémon')
       
if (lose >= 3 ):
        print('Foi de base')
      
os.system("pause")
        
        

    received = connectionSocket.recv(1024)
    escolhaini = int.from_bytes(received, byteorder="little")

    if(escolha == escolhaini):
        response = "Empate"
        print("Empate")
       
    if((escolha== 2 and escolhaini == 1) or (escolha== 1 and escolhaini == 3) or (escolha== 3 and escolhaini == 2)):
        response = "Derrota"
        print("Você Venceu")
        md5 += 1
        vic += 1
      
    if ((escolha == 1 and escolhaini == 2) or (escolha == 3 and escolhaini == 1) or (escolha == 2 and escolhaini == 3)):
        response = "Vitória"
        print("Você Perdeu")
        lose += 1
        md5 += 1
        
    connectionSocket.send(pickle.dumps(response))
    escolha = 4
 


if (md5 >= 5):
        print('Jogo encerrado')
   
if (vic >= 3 ):
        print('Você mostrou quem é o mestre pokémon')
       
if (lose >= 3 ):
        print('Foi de base')
      
os.system("pause")
connectionSocket.close()
