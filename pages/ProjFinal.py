from tkinter import FALSE
import streamlit as st
import pandas as pd
import collections
import plotly.express as px
import numpy as np
from pathlib import Path



st.set_page_config(page_title="Dashboard Games", layout="centered", page_icon="☘️", initial_sidebar_state="expanded")

diretorio = Path(__file__).parent if "_file_" in locals() else Path.cwd()
arquivo = diretorio / "geral.css"

with open(arquivo) as c:
    st.markdown("<style>{}</style>".format(c.read()), unsafe_allow_html=True)


# Importação e Manipulação dos Dados#


def importa_dados():
    df = pd.read_csv("data/vgsales.csv")
    df = df.dropna()  # para retirar valores ausentes#
    df["Year"] = df["Year"].astype(int)  # Tranformar em inteiro#
    df = df.sort_values("Year", ascending=False)
    return df


dF = importa_dados()


st.markdown(
    "<h1 style='text-align: center;'>📶	Dashboard Games</h1>", unsafe_allow_html=True
)
st.markdown("---")

st.sidebar.header("Informe o Filtro Desejado:")

plat = st.sidebar.multiselect(
    "Selecione a Plataforma",
    options=dF["Platform"].unique(),
    default=dF["Platform"].unique(),
)

generous = st.sidebar.multiselect(
    "Selecione a Genero",
    options=dF["Genre"].unique(),
    default=dF["Genre"].unique(),
)

ano = st.sidebar.multiselect(
    "Apartir de qual anos você deseja visualizar",
    options=dF["Year"].unique(),
    default=dF["Year"].unique(),
)

df_selecao = dF.query(
    "Genre == @generous & Platform == @plat & Year == @ano"
)



freq_vendas = (
    df_selecao.groupby("Year")
    .count()
    .sort_values("Name", ascending=False)
    .reset_index()[["Year", "Name"]]
)

st.dataframe(df_selecao)

top_10 = freq_vendas.head(10)
grafico1 = px.bar(
    top_10,
    x="Year",
    y="Name",
    title="Frequências de Vendas",
    labels={"Nome", "Frequências"},
    color_discrete_sequence=px.colors.sequential.Aggrnyl
)

top_10jogo = pd.DataFrame(collections.Counter(
    df_selecao['Name'].tolist()).most_common(10),  # Os 10 mai comuns #
    columns=['Game', 'Frequency'])

grafico2 = px.bar(top_10jogo, x='Game', y = 'Frequency')

coluna1, coluna2 = st.columns(2)
with coluna1:
    grafico1
with coluna2:
    grafico2

#Melhores Jogos#

coluna = ['NA_Sales']
titulo = ['North America']

for i, c in enumerate(coluna):
    df_vendas = df_selecao.groupby('Name').sum().sort_values(c, ascending=False).head(10).reset_index()[['Name', c]]
    grafico3 = px.bar(df_vendas, x = 'Name', y = c,
                      title= "Os 10 melhores Jogos em {}".format(titulo[i]),
                      labels={"Name", "Game"},
    )
    
grafico3

# Remove Estilo Streamlit #
remove_st_estilo = """
    <style>
        #MainMenu{visibility: hidden;}
        footer{visibility: hidden;}
        header{visibility: hidden;}
    </style>
 """
st.markdown(remove_st_estilo, unsafe_allow_html=True)
