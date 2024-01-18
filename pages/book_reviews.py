import streamlit as st
import pandas as pd

st.set_page_config(layout="wide") #definir a largura como Wide.

df_reviews = pd.read_csv("datasets/customer reviews.csv") #importar a fonte de dados.
df_top_books = pd.read_csv("datasets/Top-100 Trending Books.csv") #importar a fonte de dados.

books =  df_top_books["book title"].unique() #fazer com que seja mostrada unicamente a coluna "Book Title".

option = st.sidebar.selectbox("Books:", books) #criação de um select box com os titulos dos livros.


df_book = df_top_books[df_top_books["book title"] == option] #serve para que se possa escolher o livro desejado a partir do selectbox usando o title.
#Ou seja está sendo conectado com o "Book Title que foi definido na variável books." 

df_reviews_f = df_reviews[df_reviews["book name"] == option] #esse aqui está fazendo a mesma coisa que a função anterior, a diferênça, é que agora está se ligando
#a coluna "Book Name" que está dentro da variável correspondente a outra fonte de dados. Deste arquivo só irá se usar as avaliações  e comentarios.


book_title = df_book["book title"].iloc[0] #trazendo a informação referente a cada coluna expecificada, solicitando apenas a primeira linha.
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rate = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]


st.title(book_title) #titulo
st.header(book_genre) #genero textual
col1, col2, col3 = st.columns(3) #criando colunas
col1.metric("Price", book_price) #preço
col2.metric("Rate", book_rate) #avaliação
col3.metric("Year", book_year) #ano publicação

st.divider() #linha de divisão

for row in df_reviews_f.values: #laço for responsável por trazer a respectiva nota e comentarios de cada livro. Quando eu imprimo o row, ele me mostra todas as informações de cada linha.
    
    message = st.chat_message (f"{row[4]}") #definindo a variável message, onde eu irei usar para agrupar as outras informações.
    #Depois eu escolhi o formato de mensagem. Foi necessário alterar a informação para string. E por fim escolhido o local da informação na linha.
    
    message.title(row[2]) #foi traga de volta a variável message para fazer a junção.
    message.write(row[5])



