from pathlib import Path
import streamlit as st
import pandas as pd
from joblib import load
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import base64
from PIL import Image

st.set_page_config(page_title="Walison - Contato", layout="centered", page_icon="☘️", initial_sidebar_state="expanded")
diretorio = Path(__file__).parent if "_file_" in locals() else Path.cwd()
arquivo_css = diretorio / "pages"/"styles" /"geral.css"
arquivo_img = diretorio / "pages" / "assets" / "FOTOwa.jpg"

with open(arquivo_css) as c:
    st.markdown("<style>{}</style>".format(c.read()), unsafe_allow_html=True)

st.caption("Mais um pequeno projeto tirado de: https://dadosaocubo.com/visualizacao-de-dados-com-plotly-python/")


st.title("Classificação Mercadológica")
st.subheader("**Classificação com NLP**")
st.markdown("""Este app faz a classificação mercadológica, a partir da descrição dos itens é
            feita a classificação por departamento. Com técnicas de NLP e aprendizagem de máquina,
            foi treinado um modelo capaz de categorizar itens em 53 departamentos. Você 
            pode testar a aplicação fazendo o dowload de uma relação de itens exemplos no botão (Link Exemplo), com o seu 
            próprio arquivo csv(apenas uma coluna com a descrição dos itens), ou escolher a opção(Digitar Itens) e inserir
            manualmente os itens separados apenas por vírgula. Você vai poder visualizar exemplos dos 
            dados gerados, alguns gráficos e ao final é possível fazer o dowload do arquivo classificado.A
            precisão deste  classificador e de 95%""")




## Fazendo uma limpeza nos dados##
def clean (df):
    df['nova_descricao'] = df['descricao'].copy()
    df['nova_descricao'] = df['nova_descricao'].str.replace('[,.:;!?]+', ' ', regex=True).copy()
    df['nova_descricao'] = df['nova_descricao'].str.replace('[/<>()|%&#@\'\"]+', ' ', regex=True).copy()
    df['nova_descricao'] = df['nova_descricao'].str.replace('[0-9]+', ' ', regex=True)
    return df.nova_descricao

def model(df):
    cvt = load('pages/models/cvt.joblib') #transformar textos em vetores númericos#
    tfi = load('pages/models/tfi.joblib') # Transformador dos vetores numéricos usando a função estatística Tf-idf#
    clf = load('pages/models/clf.joblib') # Modelo de classificação do tipo LinearSVC #
    new_cvt = cvt.transform(df)
    new_tfi = tfi.transform(new_cvt)
    result = clf.predict(new_tfi)
    return result

def get_download(df, arq):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode() 
    href = f'<a href="data:file/csv;base64,{b64}" download="'+arq+'.csv">Download</a>'
    return href

def main():
    
    imagem = Image.open(arquivo_img)
    st.sidebar.image(imagem,width=150, output_format="auto")
    st.sidebar.title('Walison Ferreira Antunes')
    st.sidebar.markdown('Email para contato:')
    st.sidebar.caption('walison@unoeste.edu.br')
    st.sidebar.markdown('LinkedIn:')
    st.sidebar.caption('https://www.linkedin.com/in/walison-f-antunes')

    if st.button('Link Exemplo'):
        exemplo = pd.read_csv('https://raw.githubusercontent.com/dadosaocubo/streamlit/master/itens.csv')
        st.markdown(get_download(exemplo, 'itens'), unsafe_allow_html=True)
            
    dados = ''
    stop_words = ['em','sao','ao','de','da','do','para','c','kg','un','ml',
                  'pct','und','das','no','ou','pc','gr','pt','cm','vd','com',
                  'sem','gfa','jg','la','1','2','3','4','5','6','7','8','9',
                  '0','a','b','c','d','e','lt','f','g','h','i','j','k','l',
                  'm','n','o','p','q','r','s','t','u','v','x','w','y','az','cx',
                  'bc', 'KIT','azul','bco','tp','sh','cond', 'mac', 'pote', 'mini']
    
    st.subheader('**Selecione uma das Opções**')
    options = st.radio('O que deseja fazer?',('Carregar Arquivo', 'Digitar Itens'))
    if options == 'Carregar Arquivo':
        data = st.file_uploader('Escolha o dataset (.csv)', type = 'csv')
        if data is not None:
            df = pd.read_csv(data)
            df['nova_descricao'] = clean(df)
            result = model(df['nova_descricao'])
            df['departamento'] = result
            st.subheader('**Dados Classificados**')
            qtd = st.slider('Quantos itens?', 0, 10000, 5)
            st.dataframe(df[['descricao','departamento']].head(qtd))
            dados = 'ok'
            st.caption(f"Total de Produtos baixados : {df['departamento'].count()} OBS: O indice começa em zero")
            
    if options == 'Digitar Itens':
        text = st.text_input('Digite os itens separados por vírgulas (Ex: Arroz, Feijão, Açúcar) :')
        if text is not '':
            itens = {'descricao': text.split(',')}
            df = pd.DataFrame(itens)
            df['nova_descricao'] = clean(df)
            result = model(df['nova_descricao'])
            df['departamento'] = result
            st.subheader('**Dados Classificados**')
            st.dataframe(df[['descricao','departamento']].head())
            dados = 'ok'

    st.subheader('**Visualização dos Dados**')
    if dados is not '':
        if st.checkbox('WordCloud'):
            all_words = ' '.join(s for s in df['nova_descricao'].values)
            st.set_option('deprecation.showPyplotGlobalUse', False)# adicionado para não aparecer informativos#

            # criar uma wordcloud
            wc = WordCloud(stopwords=stop_words, background_color="black", width=1600, height=800, max_words=30)
            wordcloud = wc.generate(all_words)
           
            # plotar wordcloud
            fig, ax = plt.subplots(figsize=(10,6))
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.set_axis_off()
            st.pyplot()

        
        if st.checkbox('Top10 Departamentos'):
            chart_data = df['departamento'].value_counts().head(10)
            st.bar_chart(chart_data)
        if st.checkbox('Bottom10 Departamentos'):
            chart_data = df['departamento'].value_counts().tail(10)
            st.bar_chart(chart_data)

    if dados is not '':
        st.subheader('**Download dos Dados**')
        st.markdown(get_download(df[['descricao','departamento']], 'Result'), unsafe_allow_html=True)

            
if __name__ == '__main__':
        main()
    
