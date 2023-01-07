# Color-Space-Message
Pequeno projeto pessoal para criar uma imagem de saída cujas cores contém informações de uma imagem de entrada. 

O objetivo desse projeto é criar um subconjunto C do espaço de cores, baseado nas coodendas dos pixels de uma imagem de entrada, para então criar uma imagem de saída, cuja todas as cores estão justantemente em C, assim inserindo informações da imagem de entrada nas cores da imagem de saída. A informação inserida na imagem de saída pode ser obtida fazendo um gráfico de suas cores.

Uma aplicação interessante desse projeto é utilizá-lo para codificar uma mensagem nas cores de uma imagem.

## Como utilizar
Primeiro você deve subtituir a imagem `input_image.png` por uma de sua escolha, é nessa imagem que vai a mensagem que será codificada. Essa imagem deve ser grayscale, ter fundo branco, e sua mesagem deve ser escrita nela com a cor preta. Para exemplificar, considere a seguinte imagem como a `input_image.png`

![This is an image](/input_image.png)

Em sequência rode o script `main.py`, ele irá criar outra imagem chamada `output_image.png`. Após rodar o script com a imagem de exemplo, é gerado a seguinte imagem

<img src="/output_image.png" width="255" height="255" />

Agora, se for feito um gráfico em um sistema de coordenadas cartesianas 3D, das cores da imagem gerada pelo scrip, em que cada eixo corresponde a alguma cor primária (vermelho, verde, azul), de tal foram que cada cor da imagem gera o ponto

$$
  \begin{bmatrix}
  \text{Valor do canal vermelho} \\
  \text{Valor do canal verde} \\ 
  \text{Valor do canal azul}
  \end{bmatrix}
$$

Irá ser obtido a mensagem escrita em `input_image.png`. O script `view_color_space.py` faz justamente isso, então rodando ele no exemplo em questão é gerado o seguinte gráfico

<img src="/graph_example.png"/>
