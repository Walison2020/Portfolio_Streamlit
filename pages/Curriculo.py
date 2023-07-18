from pathlib import Path # usado para trabalhar com arquivos#
import streamlit as st
from PIL import Image # usado para trabalhar com imagens#

st.set_page_config(page_title="Walison - Curriculo", layout="centered", page_icon="☘️", initial_sidebar_state="expanded")
# Configurações Estruturais #
diretorio = Path(__file__).parent if "_file_" in locals() else Path.cwd()
arquivo_css = diretorio / "pages"/"styles" /"geral1.css"
arquivo_pdf = diretorio / "pages" / "assets" / "WalisonCurri2023.pdf"
arquivo_img = diretorio / "pages" / "assets" / "FOTOwa.jpg"

st.markdown(f"""
            <style>
            .stApp {{background-image: url("https://images.unsplash.com/photo-1509537257950-20f875b03669?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1469&q=80"); 
                     background-attachment: fixed; color: white;
                     background-size: cover}}
         </style>
         """, unsafe_allow_html=True)



# Configurações Geral das Informações#

tit = "Curriculum | Walison Ferreira Antunes"
nome = "Walison Ferreira Antunes"
Descric = """Estudante de Curso de TI Curso Banco de dados, com foco em 
Desenvolvimento Web e Data Science."""
email = "walison@unoeste.edu.br"
midia_social = {"LinkedIn": "http://www.linkedin.com/in/walison-f-antunes",
                 "GitHub":  "https://github.com/Walison2020"}

Cursos = {"":""}


with open(arquivo_css) as c:
    st.markdown("<style>{}</style>".format(c.read()), unsafe_allow_html=True)
with open(arquivo_pdf, "rb") as arquivo_pdf:
    pdfLeitura = arquivo_pdf.read()

imagem = Image.open(arquivo_img)


#Separar por 2 colunas com tamanho small - pequeno#

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(imagem,width=200)
    # Experiência  #
    st.write("#") 
     
st.subheader("Histórico de Trabalho - Experiência")
st.write("""
        💹 Analista Administrativo - Viação Motta LTDA
        
        💹 Programador de internet - PCI Concurso e Apostilas LTDA
              
                """)   
   
    #Skills#
    #midias Sociais#
st.markdown("#")
st.subheader("Skills")
st.write("🐍 Conhecimento em Linguagem de Programação: Python, R, C#, Spark, etc.")
st.write("📊 Visualização de dados com Power BI e Tableau")     
st.markdown("#")

with col2:
    st.subheader(nome)
    st.markdown("#")
    st.write(Descric)
    st.markdown("#")
    st.download_button(
        label= "Download Curriculum",
        data=pdfLeitura,
        file_name=arquivo_pdf.name,
        mime="application/octet-stream"
        )
    st.write("✉️", email)

    colunas =st.columns(len(midia_social))
    for indice, (plataforma, link) in enumerate(midia_social.items()):
        colunas[indice].write(f"[{plataforma}]({link})")  
    st.markdown("#")
    st.markdown("#")
    st.markdown("#")

st.subheader("Formação Académica")
st.write("🔥 Tecnólogo em Banco de Dados  / Faculdade Impacta -- Agosto 2025")
st.write("🔥 Pós-Graduação Lato Sensu – MBA em Data Science / USP -Piracicaba, SP -- Agosto 2022")
st.write("🔥 Superior Gestão Empresarial FATEC - Presidente Prudente/SP -- Março 2016")
