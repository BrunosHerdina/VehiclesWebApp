import pandas as pd
import plotly.express as px
import streamlit as st

df_vehicles = pd.read_csv('../vehicles.csv') # lendo os dados
hist_button = st.button('Criar histograma') # criar um botão para a criação de um histograma
disp_button = st.button('Criar dispersão') # criar um botão para a criação de um gráfico de dispersão
bars_button = st.button('Criar barras') # criar um botão para a criação de um gráfico de barras

if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um histograma
    fig = px.histogram(
        df_vehicles, 
        x="price", 
        color="condition", 
        title="Vehicles price by condition"
    )
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if disp_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um gráfico de dispersão
    fig = px.scatter(
        df_vehicles, 
        y="model_year", 
        x="odometer", 
        title='Ano x Quilometragem'
    ) # criar um gráfico de dispersão
    fig.update_yaxes(title='Ano') # adicionando o título do eixo x
    fig.update_xaxes(title='Quilometragem') # adicionando o título do eixo y
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if bars_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um gráfico de barras para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um gráfico de barras
    fig = px.bar(
        df_vehicles.groupby(['type','condition']).size().reset_index(name='count'),
        x="type",
        y="count",
        color="condition",
        title="Condição dos veículos por tipo"
    )
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)