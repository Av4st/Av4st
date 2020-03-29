import random

print("-------------------")
print("Welcome to the GAME")
print("-------------------")

while True:
    maquina = random.randint(0, 100)
    player = int(input("Digite um número: "))
    print()
    if maquina == player:
                 print("---------------------")
                 print("Parabéns você acertou")
                 print("---------------------")
                 continue
    else:
        print("---------------------")
        print("Você Errou")
        print("---------------------")
        continue
    
