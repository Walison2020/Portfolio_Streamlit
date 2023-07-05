
from pathlib import Path
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
import plotly.figure_factory as ff

st.set_page_config(page_title="Walison - Projetos", layout="centered", page_icon="☘️", initial_sidebar_state="expanded")

diretorio = Path(__file__).parent if "_file_" in locals() else Path.cwd()
arquivo_css = diretorio / "pages"/"styles" /"geral.css"
with open(arquivo_css) as c:
    st.markdown("<style>{}</style>".format(c.read()), unsafe_allow_html=True)

st.title("Mini Projetos com Gráficos")

st.header("Gráfico Line Chart")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.header("Gráfico Area Chart")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.area_chart(chart_data)

st.header("Gráfico Bar Chart")

chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=["a", "b", "c"])

st.bar_chart(chart_data)

st.header("Gráfico Mapa Scatterplot")

df = pd.DataFrame(
     np.random.randn(10, 2) / [10, 15] + [-22.1017, -51.42148625080566],
     columns=['lat', 'lon'])

st.map(df)

st.header("Gráfico Matplotlib")

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

st.header("Gráfico Altair")

df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode( # type: ignore
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)

st.header("Gráfico Plotly")

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5]) # type: ignore

# Plot!
st.plotly_chart(fig, use_container_width=True)

st.header('Fim dos projetos graficos')
