
#  Flask PyTorch MNIST Prediction
Esta aplicação é um serviço web desenvolvido com Flask que carrega um modelo de rede neural treinado em PyTorch para realizar previsões de dígitos manuscritos do dataset MNIST.

# Visão Geral
O aplicativo permite que o usuário envie uma imagem de um dígito manuscrito, que será então processada por um modelo PyTorch pré-treinado. O modelo fará uma previsão do dígito que corresponde à imagem enviada, retornando o resultado via uma API REST.

# Requisitos
- Python 3.7+
- PyTorch
- Flask


Aqui está um exemplo de um README para uma aplicação Flask que usa PyTorch para rodar um modelo de previsão no dataset MNIST:

Flask PyTorch MNIST Prediction
Esta aplicação é um serviço web desenvolvido com Flask que carrega um modelo de rede neural treinado em PyTorch para realizar previsões de dígitos manuscritos do dataset MNIST.

Visão Geral
O aplicativo permite que o usuário envie uma imagem de um dígito manuscrito, que será então processada por um modelo PyTorch pré-treinado. O modelo fará uma previsão do dígito que corresponde à imagem enviada, retornando o resultado via uma API REST.

Estrutura do Projeto
bash
Copiar código
flask-pytorch-mnist/
│
├── app/
│   ├── __init__.py        # Inicializa o app Flask
│   ├── main.py            # Arquivo principal da aplicação
│   ├── torch_utils.py      # Funções utilitárias para lidar com PyTorch
│   ├── static/            # Arquivos estáticos (CSS, JS, etc.)
│   └── templates/         # Templates HTML (se aplicável)
│
├── model/                 # Diretório para o modelo treinado
│   └── mnist_ffn.pth      # Modelo PyTorch treinado
│
├── venv/                  # Ambiente virtual (opcional)
│
├── requirements.txt       # Dependências da aplicação
├── README.md              # Instruções e documentação
└── .gitignore             # Arquivos ignorados pelo Git
Requisitos
Python 3.7+
PyTorch
Flask
Instalação
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/flask-pytorch-mnist.git
cd flask-pytorch-mnist
Crie e ative um ambiente virtual (opcional):

bash
Copiar código
python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate     # Para Windows
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Baixe o modelo treinado: Certifique-se de ter o modelo PyTorch treinado (exemplo: mnist_ffn.pth) no diretório model/. Se você não tiver o arquivo do modelo, poderá treinar um utilizando o dataset MNIST ou baixar um já treinado.

Iniciar a aplicação:

bash
Copiar código
export FLASK_APP=app/main.py  # Para Linux/macOS
set FLASK_APP=app/main.py     # Para Windows
flask run
Acesse a aplicação: Abra um navegador e acesse http://127.0.0.1:5000.

Como funciona
A aplicação aceita uma imagem de um dígito manuscrito como entrada.
A imagem é pré-processada (convertida para escala de cinza, redimensionada para 28x28 e normalizada).
O modelo PyTorch carregado faz a previsão do dígito com base na imagem.
A resposta é enviada ao cliente com a previsão do dígito.
API Endpoint
POST /predict: Envia uma imagem e retorna o dígito previsto.

# Modelo PyTorch
O modelo usado nesta aplicação é uma rede neural feedforward simples com a seguinte arquitetura:

- Camada de Entrada: 784 neurônios (28x28 pixels achatados)
- Camada Oculta: 500 neurônios com ativação ReLU
- Camada de Saída: 10 neurônios (um para cada dígito de 0 a 9)
- O modelo foi treinado com o dataset MNIST.
