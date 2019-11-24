from urllib import request
import sys
import random
import time


# Alterar se utilizar outro host
host = "http://localhost:8080"

player = 1

done = False
while not done:
    # Pergunta quem eh o jogador
    resp = request.urlopen("%s/jogador" % host)
    player_turn = int(resp.read())

    # Se jogador == -1, o jogo acabou e o cliente perdeu
    if player_turn==-1:
        print("I lose.")
        done = True
        break

    # Se for a vez do jogador
    if player_turn==player:
        # Pega os movimentos possiveis
        resp = request.urlopen("%s/movimentos?player=%d" % (host,player))
        movimentos = eval(resp.read())

        # Escolhe um movimento aleatoriamente
        movimento = random.choice(movimentos)

        # Executa o movimento
        print(f"Player: {player_turn} - {movimento}")
        resp = request.urlopen("%s/move?player=%d&rule=%d&animal=%d&land=%d" % (host,player,movimento[0],movimento[1],movimento[2]))
        mensagem = eval(resp.read())

        #Se com o movimento o jogo acabou, o cliente venceu
        # if mensagem[0] == 0:
        #     print("I win")
        #     done = True
        # if mensagem[0] < 0:
        #     raise Exception(mensagem[1])
    
    # Descansa um pouco para nao inundar o servidor com requisicoes
    time.sleep(1)




