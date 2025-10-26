#Tokenization
#Stop Word Removal
#Stemming and Lemmatization

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


documents = [
"Data preprocessing is an important step in machine learning."
,
"Machine learning models require clean and meaningful data."
,
"Preprocessing involves tokenization and TF-IDF computation."
]

# Tokenization and TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
# Fit and transform the documents
tfidf_matrix = vectorizer.fit_transform(documents)
#Transform the sparse matrix to a dense format and convert to DataFrame for better readability
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
#print(tfidf_df)

#Constructing a simple graph
import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()
# Add nodes
G.add_nodes_from(["Data Preprocessing", "Machine Learning", "Tokenization", "TF-IDF"])
# Add edges(relationships)
G.add_edges_from([
    ("Data Preprocessing", "Machine Learning"),
    ("Data Preprocessing", "Tokenization"),
    ("Tokenization", "TF-IDF")
])
# Draw the graph
plt.figure(figsize=(8,6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)
plt.title("Simple Graph Representation of Text Processing Concepts")
#plt.show()

#Tokenization
import nltk
from nltk.tokenize import word_tokenize
text = "Data preprocessing is essential for effective machine learning."
tokens = word_tokenize(text)
print("Tokens:", tokens)
#stemming
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
stems = [stemmer.stem(token) for token in tokens]
print("Stems:", stems)
#lemmatization
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(token) for token in tokens]
print("Lemmas:", lemmas)

#Visualize most frequent words
from collections import Counter

words = ['nlp','is','fun','nlp','fun','fun','great']

word_freq = Counter(words)
print(word_freq.most_common(4))