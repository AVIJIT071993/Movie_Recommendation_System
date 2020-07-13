# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 23:41:26 2020

@author: Avijit Banduri
"""


import pandas as pd
import numpy as np

movie =pd.read_csv("IMDB-Dataset//movies.csv")
rating = pd.read_csv("IMDB-Dataset//ratings.csv")
df = pd.merge(movie, rating, on='movieId')

ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings['number_of_ratings'] = df.groupby('title')['rating'].count()
movie_matrix = df.pivot_table(index='userId', columns='title', values='rating')

def recommend_movie(movie_name):
    movie_user_rating = movie_matrix[movie_name]
    similar_to_movie = movie_matrix.corrwith(movie_user_rating)
    corr_movie = pd.DataFrame(similar_to_movie, columns=['Correlation'])
    corr_movie.dropna(inplace=True)
    corr_movie = corr_movie.join(ratings['number_of_ratings'])
    recom=corr_movie[corr_movie['number_of_ratings'] > 100].sort_values(by='Correlation', ascending=False).head(6)
    recom = recom.index.values[1:]
    return recom

