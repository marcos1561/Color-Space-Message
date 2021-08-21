import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

'''
    Visualiza o espaço de cores da imagem gerada dawd
'''
img = mpimg.imread("output_image.png", "png")
plt.imshow(img)

colors = [[] for _ in range(3)]
for line in img:
    for pixel in line:
        for i in range(3):
            colors[i].append(pixel[i])
colors = np.array(colors)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.set_xlabel("Vermelho")
ax.set_ylabel("Verde")
ax.set_zlabel("Azul")

ax.scatter(*colors, c=colors.transpose())

plt.show()
