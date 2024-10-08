import pygame
import numpy as np
from aps4.contas import * 

def main():

    #variaveis iniciais 
    largura_tela = 500
    altura_tela = 500
    vertice = 50
    angulo = 0
    rotacao = 1
    delta_x = 0
    delta_y = 0

    #criando a matriz do cubo
    matriz_cubo = inicializar_vertices(vertice)
    matriz_cubo = np.vstack((matriz_cubo, np.ones(8)))

    #inicializando pygame
    pygame.init()
    screen = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("CUBO 3D TRANSFORMACOES")
    clock = pygame.time.Clock()

    #loop prinicipal do pygame 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        key = pygame.key.get_pressed()

        #movimentacao do cubo com as setas
        if key[pygame.K_LEFT]:
            delta_x += 3
        if key[pygame.K_RIGHT]:
            delta_x -= 3
        if key[pygame.K_UP]:
            delta_y += 3
        if key[pygame.K_DOWN]:
            delta_y -= 3

        #mudando o tamanho do cubo
        if key[pygame.K_z]:
            vertice += 10
        if key[pygame.K_x] and vertice > 10:
            vertice -= 10

        #mudar a rotacao do cubo
        if key[pygame.K_y]:
            rotacao = 0  #parar rotacao
        if key[pygame.K_u]:
            rotacao = 1  #retormar rotacao
        if key[pygame.K_i]:
            rotacao = -1  #muda sentido da rotacao 

        #aumentando valor do angulo de rotacao dado a variacao
        angulo += rotacao
        angulo_rad = np.deg2rad(angulo)

        #aplicando as trasnformacoes e desenhando o cubo
        X_transformado = aplicar_transformacoes(matriz_cubo, delta_x, delta_y, vertice, angulo_rad, largura_tela, altura_tela)
        screen.fill((0, 0, 0))  
        desenhar_cubo(screen, X_transformado)

        pygame.display.flip() 
        clock.tick(60) #jogo em 60 fps

if __name__ == "__main__":
    main()