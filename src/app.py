import streamlit as st

# Título do App
st.title('Nosso Primeiro App com Streamlit')

# Escrevendo um Hello World com markdown
st.markdown('**Hello world!** 🌍')

# Escrevendo texto
st.write('Esta é uma demonstração de algumas funcionalidades do Streamlit.')

# Input de texto do usuário
input_texto = st.text_input('Digite algo aqui:')

# Mostrando o texto digitado
st.write(f'Você digitou: {input_texto}')

# Slider para números
numero = st.slider('Escolha um número', 0, 100, 50)

# Exibir o número escolhido
st.write(f'Você escolheu o número: {numero}')

# Gráfico de barras simples
import pandas as pd
import numpy as np

# Criando dados aleatórios
dados = pd.DataFrame({
  'colunas': ['A', 'B', 'C', 'D', 'E'],
  'valores': np.random.randn(5)
})