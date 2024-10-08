# Projeto de Projeção 3D - Cubo em Wireframe

# Descrição

Este projeto tem como objetivo implementar uma projeção 3D em tempo real de um cubo em wireframe utilizando a biblioteca Pygame. Todas as transformações são realizadas manualmente, utilizando a biblioteca NumPy para manipulação matemática, sem o auxílio de bibliotecas adicionais para transformações automáticas. O projeto foi desenvolvido como parte da disciplina de algebra linear


# Como Executar

Para rodar este projeto, siga os passos abaixo:

- Certifique-se de ter Python instalado em sua máquina.
- Instale a biblioteca Pygame. Você pode fazer isso executando o comando pip install pygame no terminal.
- Clone este repositório para sua máquina local.
- Navegue até o diretório do projeto e execute o arquivo principal com o comando python main.py.

# Uso

Uma vez iniciado, o programa exibirá um cubo em wireframe girando em todas as direções. Você pode interagir com o programa da seguinte forma:

- Z para dar zoom
- X para remover o zoom
- Setas para mover o cubo
- Y para parar o cubo
- U para fazer o cubo girar para a esquerda
- I para fazer o cubo girar para a direita

# Descrição Matemática do Modelo

Este projeto implementa transformações geométricas para manipular e visualizar um cubo em 3D projetado em um espaço de visualização 2D. As transformações aplicadas incluem rotações ao redor dos eixos X, Y, e Z, translações no espaço 3D, e uma projeção perspectiva para mapear o cubo 3D para o espaço 2D. Utilizamos matrizes de transformação no NumPy para estas operações.

# Matrizes de Transformação

Matriz de Rotação ao redor do eixo X
A matriz de rotacao para um angulo theta ao redor do eixo X multiplica cada vertice do cubo alternando as coordenadas y e z do vertice, enquanto x permanece inalterado.
O produto resulta em um novo vetor onde as coordenadas y e z sao rotacionadas. Para os eixos Y e Z , similarmente as matrizes multiplicam os vertices apropriados afetando as coordenadas.

```plaintext
Matriz Rotação ao redor do eixo X (R_x(θ)):

|  1       0        0       0 |
|  0  cos(θ)  -sin(θ)  0 |
|  0  sin(θ)   cos(θ)  0 |
|  0       0        0       1 |
```

Matriz Rotação ao redor do eixo Y

```plaintext

| cos(θ)   0  sin(θ)  0 |
|      0       1        0       0 |
| -sin(θ)  0  cos(θ)  0 |
|      0       0        0       1 |
```


Matriz de Translação 
A matriz de translacao T e um vetor  v, a multiplicacao dse da adicionando os valores de translacao deltax,delta y  e delta z, as coordenadas x,y e z respectivamanete deslocando as coordenadas x, y e z

```plaintext

|  1    0    0  Δx |
|  0    1    0  Δy |
|  0    0    1  Δz |
|  0    0    0   1 |
```

Matriz Escala
Cada coordenada do vértice é multiplicada pelo fator de escala correspondente ao seu eixo. Por exemplo, a coordenada x é multiplicada por sx, sy e sz A componente de translação (a quarta componente do vetor de vértice, que é 1 para coordenadas homogêneas) permanece inalterada, garantindo que a transformação de escala não afete a posição do objeto no espaço.

```plaintext
Matriz de Escala (S):

| s_x   0     0    0 |
|  0   s_y    0    0 |
|  0    0   s_z   0 |
|  0    0     0    1 |
```


# Aplicação das Transformações

O processo para visualizar o cubo envolve aplicar sequencialmente as transformações de rotação, seguidas pela translação e pela projeção perspectiva. O resultado é então ajustado para coordenadas de tela 2D, considerando a posição central do cubo na tela.


# Gif do Cubo
![Gif Cubo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHp4NjBtMGo2azJ0dDBzMzhwZHltYW1rYXh6YXFuZmdnaTh3MzF4YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uNv1LB57KPALF5YI50/giphy.gif)
