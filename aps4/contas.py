import numpy as np
import pygame 

def inicializar_vertices(vertice):

    cubo_vertices = [
        np.array([-vertice, vertice, vertice]),
        np.array([vertice, vertice, vertice]),
        np.array([vertice, -vertice, vertice]),
        np.array([-vertice, -vertice, vertice]),
        np.array([-vertice, vertice, -vertice]),
        np.array([vertice, vertice, -vertice]),
        np.array([vertice, -vertice, -vertice]),
        np.array([-vertice, -vertice, -vertice])
    ]
    return np.vstack(cubo_vertices).T

def aplicar_transformacoes(X, delta_x, delta_y, vertice, angulo, largura_tela, altura_tela):

    cos_ang, sin_ang = np.cos(angulo), np.sin(angulo)

    Translacao_Z = np.array([[1, 0, 0, delta_x], [0, 1, 0, delta_y], [0, 0, 1, 100], [0, 0, 0, 1]])

    Translacao_XY = np.array([[1, 0, largura_tela / 2 - delta_x], [0, 1, altura_tela / 2 - delta_y], [0, 0, 1]])

    Rotacao_X = np.array([[1, 0, 0, 0], [0, cos_ang, -sin_ang, 0], [0, sin_ang, cos_ang, 0], [0, 0, 0, 1]])

    Rotacao_Y = np.array([[cos_ang, 0, sin_ang, 0], [0, 1, 0, 0], [-sin_ang, 0, cos_ang, 0], [0, 0, 0, 1]])

    Rotacao_Z = np.array([[cos_ang, -sin_ang, 0, 0], [sin_ang, cos_ang, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

    P = np.array([[0, 0, 0, -vertice], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -(1/vertice), 0]])

    A = Translacao_Z @ Rotacao_Z @ Rotacao_Y @ Rotacao_X @ X

    A = P @ A

    A_ = np.ones((3, 8))
    for i in range(A.shape[1]):
        A_[0][i] = A[1][i] / A[3][i]
        A_[1][i] = A[2][i] / A[3][i]

    return Translacao_XY @ A_

def desenhar_cubo(screen, X):
    arestas = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]
    for aresta in arestas:
        pygame.draw.line(screen, 'WHITE', (X[0][aresta[0]], X[1][aresta[0]]), (X[0][aresta[1]], X[1][aresta[1]]), width=3)
    for i in range(8):
        pygame.draw.circle(screen, 'GREEN', (X[0][i], X[1][i]), 4)
