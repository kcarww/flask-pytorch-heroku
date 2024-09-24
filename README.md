
#  Flask PyTorch MNIST Prediction
Esta aplicação é um serviço web desenvolvido com Flask que carrega um modelo de rede neural treinado em PyTorch para realizar previsões de dígitos manuscritos do dataset MNIST.

# Visão Geral
O aplicativo permite que o usuário envie uma imagem de um dígito manuscrito, que será então processada por um modelo PyTorch pré-treinado. O modelo fará uma previsão do dígito que corresponde à imagem enviada, retornando o resultado via uma API REST.

# Requisitos
- Python 3.7+
- PyTorch
- Flask

# Modelo PyTorch
O modelo usado nesta aplicação é uma rede neural feedforward simples com a seguinte arquitetura:

- Camada de Entrada: 784 neurônios (28x28 pixels achatados)
- Camada Oculta: 500 neurônios com ativação ReLU
- Camada de Saída: 10 neurônios (um para cada dígito de 0 a 9)
- O modelo foi treinado com o dataset MNIST.
