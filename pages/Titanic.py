import streamlit as st
from pathlib import Path
from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style

diretorio = Path(__file__).parent if "_file_" in locals() else Path.cwd()
arquivo_css = diretorio / "pages"/ "styles" / "geral.css"

with open(arquivo_css) as c:
    st.markdown("<style>{}</style>".format(c.read()), unsafe_allow_html=True)




st.subheader('Data App - Referente a dados retirados do Titanic')

def cria_grafico():
    chart = Chart(width="600px", height="300px" ,display="manual")
    data = Data()
    dataframe = pd.read_csv("pages/assets/titanic.csv")
    data.add_data_frame(dataframe)
    chart.animate(data)


    #configurações#
    chart.animate(
        Config(
                {
                    "x":"Count", "y": "Sex", 
                    "label": "Count",
                    "title": "Passageiros do Titanic"
                }

        )
    )

    chart.animate(
                Config({
                        "x":["Count", "Survived"],
                        "label":["Count", "Survived"],
                        "color":"Survived"}
                )
    )

    chart.animate(
        Config({
                    "x": "Count",
                    "y": ["Sex", "Survived"]

        }
        )
    )

    # Style #

    chart.animate(
        Style(
            {
                    "title": {"fontSize":35 }
            } 
              )
              
    )
    return chart._repr_html_()

grafico = cria_grafico( )
html(grafico, width=600, height=300)
