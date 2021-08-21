import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

'''
    Lê a imagem de entrada
'''
in_image = mpimg.imread("input_image.png") 
# plt.imshow(msg)

'''
    Cria a lista com as coordenadas normalizadas dos pontos no espaço de cores baseado na imagem de entrada "input_image".
    
    Cada pixels da imagem de entrada que é bastante escuro gera um ponto no espaço de cores.
    As coordenadas do ponto são cridas da seguinte forma:

        x (Vermelho): Coluna do pixel da imagem de entrada normalizada.
        y (Verde): Valor arbitrário decidido pelo programador.
        z (Azul): Linhha do pixel da imagem de entrada normalizada.

    Os pontos são armazenados na lista "pointsCS", de tal forma que a coordenada do n-ésimo ponto é (pointsCS[0][n], pointsCS[1][n], pointsCS[2][n])

    OBS: A origem do sistema de coordenadas está no canto esquerdo inferior da imagem.
'''
pointsCS = [[], [], []]
num_lin, num_col = in_image.shape
for i in range(num_lin):
    for j in range(num_col):
        if in_image[i][j] < 0.2:
            pointsCS[0].append(j/(num_col-1))
            pointsCS[2].append((-i + (num_lin-1))/(num_lin-1))
# plt.scatter(color_coords[0], color_coords[2])


### Arbitrariamente atribui os valores da coordenada y normalizada
num_points = len(pointsCS[0])
points_y = []
for i in range(num_points):
    points_y.append(0.5  +  0.01 * np.sin(2*np.pi * pointsCS[0][i]))
pointsCS[1] = points_y
# color_coords[1] = list(0.3 + 0 * np.random.random_sample(num_colors)*np.random.choice([-1, 1], num_colors))

### pointsCS é convertido para um np-array para facilitar o forma de obter a sua transposta.
pointsCS = np.array(pointsCS) 

'''
    Configuraçõoes para vizualizar o gráfico dos pontos criados.
'''
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.set_xlabel("Vermelho")
ax.set_ylabel("Verde")
ax.set_zlabel("Azul")

ax.scatter(*pointsCS, facecolor=pointsCS.transpose())

'''
    Cria uma imagem RGB "out_image" baseado nos pontos criados.
    
    O formato da imagem é o menor quadrado que consegue conter todos os pontos. 
    Cado ponto criado corresponde a um pixel na imagem de saída, cuja cor é a própria coordenada do ponto.
    Os pixels que faltam para completar a imagem de saída são escolhidos aleatoriamente dos pontos criados. 
'''
out_image = pointsCS.transpose()
img_width = int(np.ceil(num_points**(1/2)))
img_size = int(img_width**2)

### Escolhendo aleatoriamente pontos para preencher a imagem de saída
remaing_px = out_image[np.random.randint(0, num_points, img_size - num_points)] 

### Formatando os dados para ficarem na forma de uma imagem RGB.
out_image = np.concatenate((out_image, remaing_px)).reshape(img_width, img_width, 3) 

### Visualizando a imegem de saída criada
fig_coded, ax_coded = plt.subplots()
ax_coded.imshow(out_image)

### Salvando a imagem de saída
mpimg.imsave("output_image.png", out_image, pil_kwargs={"optimize": False, "compress level": 0, "srgb": 2})

plt.show()
