from socket import *
import pickle
import os 

serverName = "127.0.0.1"
serverPort = 27123
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

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
       
        print(f"Rodada:{md5}")
        print(f"Placar Vitorias: {vic} x {lose} :Derrotas")
        escolha = int(input("Escolha seu pokémon, opções válidas de 1 a 3: "))
        

    x = escolha.to_bytes((escolha.bit_length() + 7) // 8, byteorder='little')
    clientSocket.send(bytes(x))
    result = clientSocket.recv(1024)
    escolha = 4
    text = pickle.loads(result)
    
        
    if (text == "Vitória"):
        md5 += 1
        vic += 1
    if (text == "Derrota"):
        md5 += 1
        lose += 1 
    

  

if (md5 > 5):
     print('Jogo encerrado')
        
if (vic >= 3 ):
     print('Você mostrou quem é o mestre pokémon')
        
if (lose >= 3 ):
     print('Foi de base')

os.system("pause")     
clientSocket.close()
