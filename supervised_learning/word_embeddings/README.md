# An Introduction to Word Embeddings

## Table of Contents

1. **Introduction to Word Embeddings**
2. **Natural Language Processing (NLP)**
    - Bag Of Words Intuition
    - TF-IDF Intuition
    - Text Preprocessing
3. **Word Embedding - Natural Language Processing**
    - Deep Learning
4. **Word2Vec Tutorials**
    - The Skip-Gram Model
    - Negative Sampling
5. **GloVe Explained**
6. **FastText: Under the Hood**
7. **ELMo Explained**

## Content

### 1. Introduction to Word Embeddings
Word embeddings are dense vector representations of words that capture their meanings, semantic relationships, and syntactic similarities. They are crucial in natural language processing tasks as they enable algorithms to understand and manipulate text data effectively.

### 2. Natural Language Processing (NLP)

#### Bag Of Words Intuition
The Bag of Words (BoW) model represents text data by treating each document as an unordered collection of words, disregarding grammar and word order. Each word's frequency is recorded, and this model is often used as a baseline for text classification tasks.

#### TF-IDF Intuition
Term Frequency-Inverse Document Frequency (TF-IDF) is a numerical statistic that reflects the importance of a word in a document relative to a collection of documents. It balances the frequency of a word in a document with its rarity across all documents, helping to identify significant words.

#### Text Preprocessing
Text preprocessing involves cleaning and transforming raw text data into a format suitable for analysis. Common steps include tokenization, removing stop words, stemming, lemmatization, and converting text to lower case.

### 3. Word Embedding - Natural Language Processing

#### Deep Learning
Deep learning techniques have revolutionized word embeddings by leveraging neural networks to create high-dimensional representations of words. These methods capture intricate patterns and relationships in the data, leading to more effective and nuanced embeddings.

### 4. Word2Vec Tutorials

#### The Skip-Gram Model
The Skip-Gram model predicts context words from a given target word within a fixed window size. This approach helps capture word associations and semantic relationships by maximizing the probability of context words given a target word.

#### Negative Sampling
Negative sampling is an optimization technique used in training the Skip-Gram model. It improves computational efficiency by only updating a small sample of negative examples, rather than all words in the vocabulary, during each training step.

### 5. GloVe Explained
GloVe (Global Vectors for Word Representation) is a word embedding technique that constructs vectors by aggregating global word-word co-occurrence statistics from a corpus. It combines the benefits of both matrix factorization and local context window methods.

### 6. FastText: Under the Hood
FastText extends the Word2Vec model by considering subword information. It represents words as bags of character n-grams, enabling the model to generate embeddings for rare and out-of-vocabulary words by composing the embeddings of their subwords.

### 7. ELMo Explained
ELMo (Embeddings from Language Models) provides deep contextualized word representations by considering the entire context of a word within a sentence. It uses a bidirectional LSTM to generate word embeddings that capture both syntactic and semantic nuances, improving performance on a variety of NLP tasks.