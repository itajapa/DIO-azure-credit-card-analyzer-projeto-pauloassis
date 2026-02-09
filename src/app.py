import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analyze_credit_card

def configure_interface():
    st.title("Upload de Arquivo DIO - Desafio 1 - Azure - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        fileName = uploaded_file.name
        # enviar para o blob storage
        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url:
            st.success(f"Arquivo '{fileName}' enviado com sucesso! URL: {blob_url}")
            credit_card_info = analyze_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Erro ao enviar o arquivo. {fileName} Tente novamente.")

def show_image_and_validation(blob_url, credit_card_info):
  st.image(blob_url, caption="Imagem enviada", width=700)
  st.write("Resultado da validação:   ")
  if credit_card_info and credit_card_info["card_name"]:
    st.markdown(f"<h1 style='color: green;'>Cartão de Crédito Válido</h1>", unsafe_allow_html=True)
    st.write(f"Nome do Titular: {credit_card_info['card_name']}")
    st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
    st.write(f"Data de Validade: {credit_card_info['expiration_date']}")
  else: 
    st.markdown(f"<h1 style='color: red;'>Cartão de Crédito Inválido</h1>", unsafe_allow_html=True)
    st.write("Não foi possível extrair informações válidas do cartão de crédito. Verifique a imagem e tente novamente.")

if __name__ == "__main__":
    configure_interface()

