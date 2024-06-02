#!/usr/bin/env python3
"""
0-bag_of_words.py
"""
from sklearn.feature_extraction.text import CountVectorizer

def bag_of_words(sentences, vocab=None):
    """function creates a bag of words embedding matrix"""

    vectorizer = CountVectorizer(vocabulary=vocab)
    X = vectorizer.fit_transform(sentences)

    embeddings = X.toarray()
    features = vectorizer.get_feature_names()

    return embeddings, features
