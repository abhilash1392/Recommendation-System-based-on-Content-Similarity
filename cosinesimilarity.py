# Importing Libraries 
import numpy as np 
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
import matplotlib.pyplot as plt 
import nltk 
from nltk import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity

def recommend_movies(name):
    # Importing the data into a csv file
    df = pd.read_csv('netflix_titles.csv')
    # Removing any null values 
    for i in list(df.columns):
        df[i]=df[i].fillna('')
    df['text'] = df['title']+' '+df['director']+' '+df['cast']+' '+df['listed_in']+' '+df['description']
#     print(df['text'][0])
    # Creating vectorizer
    tfv = TfidfVectorizer(ngram_range=(1,2),stop_words='english',tokenizer=word_tokenize)
    text_features = tfv.fit_transform(df['text'])
    similarity_matrix = cosine_similarity(text_features)
    if name not in list(df['title']):
        return 'Sorry this movie is not in our database'
    else:
        movie_index = df[df['title']==name].index
        movie_similarity =similarity_matrix[movie_index]
        movie_data = pd.DataFrame(movie_similarity[0],columns=['cosine_similarity'])
        movie_data['index'] = np.arange(df.shape[0])
        movie_data = movie_data.sort_values(by='cosine_similarity',ascending=False)
        topn = 10
        movie_ids = movie_data['index'][1:topn]
        recommended_movies = []
        for temp in movie_ids:
            movie = df['title'][temp]
            recommended_movies.append(movie)
        return recommended_movies