from pathlib import Path
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu


diretorio = Path(__file__).parent if "_file_" in locals() else Path.cwd()
arquivo_css = diretorio / "pages"/ "styles" / "geral1.css"

with open(arquivo_css) as c:
    st.markdown("<style>{}</style>".format(c.read()), unsafe_allow_html=True)


st.sidebar.success("Escolha a Página", icon="✅" )



selecao = option_menu(
    menu_title="Home Page ",
    options=["Projetos","Deepnote"],
    icons=["house", "book", ],
     menu_icon="cast",
    orientation= "horizontal"

    )
    
if selecao == "Projetos":
    st.title(f"Você selecionou o menu {selecao}")


    col1, col2 = st.columns(2)

    with col1:
      st.header("Montanhas")
      st.image("Recursos/Montanhas.jpg", width=350)

    with col2:
      st.header("Imagem Gráfica")
      st.image("Recursos/image1.jpg", width=162)

#-----------------------------------------------------------------
    st.header("Usando tabelas ocultas")
    tab1, tab2, = st.tabs(["Montanhas", "Gráficas"])

    with tab1:
      st.header("Paisagem")
      st.image("Recursos/Montanhas.jpg", width=650)

    with tab2:
      st.header("Gráficas")
      st.image("Recursos/image1.jpg", width=350)

#------------------------------------------------------------------
    st.bar_chart({"data": [1, 5, 2, 16, 2, 1]})

    with st.expander("Visão expandida"):
     st.write('Imagem Dados :'
              
              )
     st.image("https://static.streamlit.io/examples/dice.jpg")

#-------------------------------------------------------------------

    with st.container():
        st.write("This is inside the container")

   # You can call any Streamlit command, including custom components:
        st.bar_chart(np.random.randn(50, 3))

        st.write("This is outside the container")

#____________________________________________________________________

    st.header("Container Vazio")
    placeholder = st.empty()

# Replace the placeholder with some text:
    placeholder.text("Hello")

# Replace the text with a chart:
    placeholder.line_chart({"data": [1, 5, 2, 6]})

# Replace the chart with several elements:
    with placeholder.container():
     st.write("This is one element")
     st.write("This is another")

# Clear all those elements:
    placeholder.empty()
    

if selecao == "Deepnote":
    st.title(f"Você selecionou o menu {selecao}")

    st.subheader("Gráficos do deepnote")

    import streamlit.components.v1 as components

    #components.iframe("https://docs.streamlit.io/en/latest")

    components.iframe("https://embed.deepnote.com/fc99f5f2-01be-4bf4-a5f3-4c94672b96c0/49d243ca60b142c5aff46621da71af39/7eda0f2b2d50424ebb620ea64b37a983?height=291.0625", height= 250)

    components.iframe("https://embed.deepnote.com/9dfd6154-805d-4cff-bdf3-d1aff2d50185/3ec5dfe0287241659c437ae2775a4782/34e018a6d8d64a52ab01dfed1d0621a5?height=371.8125", height=300)
    components.iframe("https://embed.deepnote.com/9dfd6154-805d-4cff-bdf3-d1aff2d50185/3ec5dfe0287241659c437ae2775a4782/fb4c94505bcd4fd484e7e6211b0e31b0?height=994", height=500)
    components.iframe("https://embed.deepnote.com/9dfd6154-805d-4cff-bdf3-d1aff2d50185/3ec5dfe0287241659c437ae2775a4782/1109077e4a8c4de0af23b6fc88942b14?height=133.34375S")
    st.subheader("**")
    st.subheader("Falando um pouco do Streamlit ")
    components.iframe("https://docs.streamlit.io/library/components/components-api", height=600, width=700, scrolling=True)
    st.balloons()
    st.subheader("Testando link  do Site Mercado Livre")
    st.caption("https://www.mercadolivre.com.br/")
    components.iframe("https://www.mercadolivre.com.br/ofertas/tendencias-explosivas#DEAL_ID=&S=MKT&V=1&T=MS&L=MKTPLACE_FASHION_BEAUTY_PPSMULTICAT__SEMANA_MODA_E_BELEZA&me.bu_line=26&me.flow=-1&me.bu=3&me.audience=all&me.content_id=MS_SEMANA_MODA_E_BELEZA_22_06&me.component_id=main_slider_web_ml_0&me.logic=user_journey&me.position=0&audience=all&bu=3&bu_line=26&component_id=main_slider_web_ml_0&content_id=MS_SEMANA_MODA_E_BELEZA_22_06&flow=-1&logic=user_journey&position=0&c_id=/home/exhibitors-carousel/element&c_campaign=MKTPLACE_FASHION_BEAUTY_PPSMULTICAT__SEMANA_MODA_E_BELEZA&c_element_order=1&c_uid=8bc910fd-1c2c-4582-9275-93b50adc811a", height=600, width=700, scrolling=True)