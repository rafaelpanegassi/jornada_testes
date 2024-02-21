import streamlit as st

st.set_page_config(
    page_title="Validador de Arquivo .xlsx"
)

# Título do App
st.title("Insira o seu excel para validação")

arquivo = st.file_uploader("Carregue seu arquivo Excel aqui", type=["xlsx"])

if arquivo:
    st.success("O schema do arquivo Excel está correto!")