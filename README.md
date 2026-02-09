# Detecção de Cartão de Crédito – Azure AI Document Intelligence

Projeto desenvolvido como parte do **desafio prático da plataforma DIO.me**, utilizando serviços de **Inteligência Artificial do Microsoft Azure** para análise e extração de dados de cartões de crédito a partir de imagens.

---

## 🧠 Descrição do Projeto

Esta aplicação permite o **upload de imagens de cartões de crédito** e realiza a **extração automática de informações** relevantes utilizando o modelo **Prebuilt Credit Card** do **Azure AI Document Intelligence**.

As informações extraídas incluem:
- Nome do titular
- Número do cartão
- Data de validade
- Banco emissor

A interface foi desenvolvida com **Streamlit**, proporcionando uma experiência simples e interativa.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Streamlit
- Azure AI Document Intelligence
- Azure Blob Storage
- python-dotenv
- Git & GitHub

---

## 🧱 Arquitetura da Solução

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Armazenamento:** Azure Blob Storage  
- **IA:** Azure AI Document Intelligence (Prebuilt Credit Card)  

Fluxo da aplicação:
1. Upload da imagem do cartão
2. Armazenamento da imagem no Azure Blob Storage
3. Análise do documento via Azure Document Intelligence
4. Extração e exibição dos dados na interface

---

## 📂 Estrutura do Projeto

DOCS/
├── src/
│ ├── app.py
│ ├── services/
│ │ ├── blob_service.py
│ │ └── credit_card_service.py
│ └── utils/
│ └── Config.py
├── .env.example
├── .gitignore
├── README.md


---

## ▶️ Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/itajapa/DIO-azure-credit-card-analyzer-projeto-pauloassis.git
cd DIO-azure-credit-card-analyzer-projeto-pauloassis

2️⃣ Criar e ativar ambiente virtual

python -m venv .venv
Windows

.venv\Scripts\activate
Linux / macOS

source .venv/bin/activate

3️⃣ Instalar as dependências

pip install -r src/requirements.txt

4️⃣ Configurar variáveis de ambiente

Crie um arquivo .env na raiz do projeto com base no arquivo .env.example, preenchendo as credenciais do Azure:

ENDPOINT=
SUBSCRIPTION_KEY=
AZURE_STORAGE_CONNECTION_STRING=
CONTAINER_NAME=
⚠️ Nunca versionar o arquivo .env

5️⃣ Executar a aplicação

streamlit run src/app.py
A aplicação será aberta automaticamente no navegador.

🔐 Segurança

As credenciais do Azure não são versionadas no repositório.
O projeto utiliza variáveis de ambiente e o arquivo .env está protegido via .gitignore, seguindo boas práticas de segurança.

📜 Autor

Paulo Assis
Projeto desenvolvido para fins educacionais na plataforma DIO.me
