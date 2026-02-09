# Detecção de Cartão de Crédito – Azure AI Document Intelligence

Projeto desenvolvido como parte do desafio prático da plataforma **DIO.me**, utilizando
serviços de **Inteligência Artificial do Microsoft Azure** para análise e validação de
cartões de crédito a partir de imagens.

## 🧠 Descrição do Projeto

A aplicação permite o upload de imagens de cartões de crédito e realiza a extração
automática de informações como:
- Nome do titular
- Número do cartão
- Data de validade
- Banco emissor

A validação é feita utilizando o modelo **Prebuilt Credit Card** do Azure AI Document Intelligence.

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Streamlit
- Azure AI Document Intelligence
- Azure Blob Storage
- python-dotenv

## 🧱 Arquitetura da Solução

- **Frontend**: Streamlit
- **Backend**: Python
- **Armazenamento**: Azure Blob Storage
- **IA**: Azure AI Document Intelligence (Prebuilt Credit Card)

## 📂 Estrutura do Projeto

```text
DOCS/
├── src/
│   ├── app.py
│   ├── services/
│   │   ├── blob_service.py
│   │   └── credit_card_service.py
│   └── utils/
│       └── Config.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

▶️ Como Executar o Projeto
Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
Crie um ambiente virtual e instale as dependências:

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
Configure as variáveis de ambiente:

cp .env.example .env
Execute a aplicação:

streamlit run src/app.py

🔐 Segurança
As credenciais do Azure não são versionadas no repositório. O projeto utiliza
variáveis de ambiente para garantir boas práticas de segurança.

📜 Autor
Projeto desenvolvido por Paulo Assis
Plataforma: DIO.me
