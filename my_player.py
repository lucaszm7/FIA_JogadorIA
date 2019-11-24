from urllib import request
from server import Animal, Land
import random
import time

def calcula_jogada(possiveis_jogadas, ultima_jogada):
    """Retorna a jogada a ser realizada"""
    jogada_escolhida = random.choice(possiveis_jogadas)
    return jogada_escolhida


player = 0
host = "http://localhost:8080"

finished = False
while not(finished):

    resp = request.urlopen("%s/jogador" %host)
    jogador_atual = eval(resp.read())
    # SE FOR A MINHA VEZ
    if (jogador_atual == player):

        # PEGANDO AS JOGADAS POSSIVEIS
        resp = request.urlopen("%s/movimentos?player=%d" %(host,player))
        possiveis_jogadas = eval(resp.read())

        # PEGANDO O TABULEIRO
        resp = request.urlopen("%s/tabuleiro" %host)
        # tabuleiro = eval(resp.read()) # NÃO CONSEGUE TRANSFORMAR O TABULEIRO

        # PEGANDO A ULTIMA JOGADA
        resp = request.urlopen("%s/ultima_jogada" %host)
        ultima_jogada = eval(resp.read())

        #CALCULA  E FAZ A JOGADA
        proxima_jogada = calcula_jogada(possiveis_jogadas, ultima_jogada)
        print(f"Player: {jogador_atual} - {proxima_jogada}")
        resp = request.urlopen("%s/move?player=%d&rule=%d&animal=%d&land=%d" %(host, player, proxima_jogada[0], proxima_jogada[1], proxima_jogada[2]))
        
        # try:
        #     mensagem = eval(resp.read())
        # except TypeError as err:
        #     print("URL não retornou nada da jogada!")
        # except SyntaxError as non:
        #     print(non ,"\nMano sla que erro foi esse")
    time.sleep(1)


#finished = True
