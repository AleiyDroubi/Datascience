import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import string
import nltk
from nltk.corpus import stopwords


# Load data
data = pd.read_csv(r"C:\Users\Surface Laptop 3\OneDrive\Documents\DataScience\Algorithms\section\UpdatedResumeDataset.csv")

def preprocess_text(text):
    """Clean and preprocess text data"""
    text = str(text).lower()
    text = re.sub(r"[%s]" % re.escape(string.punctuation), " ", text) 
    text = re.sub(r"\d+", " ", text)
    tokens = text.split()
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

def calculate_cv_similarity(cv1_idx, cv2_idx, data):
    """Calculate all similarity metrics for two CVs"""
    # Get and clean CV texts
    cv1_clean = preprocess_text(data.iloc[cv1_idx].to_string())
    cv2_clean = preprocess_text(data.iloc[cv2_idx].to_string())
    
    # Vectorize
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform([cv1_clean, cv2_clean]).toarray()
    
    # Calculate metrics
    cosine_sim = cosine_similarity(vectors)[0][1]
    euclidean_dist = np.linalg.norm(vectors[0] - vectors[1])
    
    # Jaccard similarity
    set1, set2 = set(cv1_clean.split()), set(cv2_clean.split())
    jaccard_sim = len(set1.intersection(set2)) / len(set1.union(set2))
    
    return {
        'cosine_similarity': cosine_sim,
        'euclidean_distance': euclidean_dist,
        'jaccard_similarity': jaccard_sim
    }

def print_similarity_results(pair_name, results):
    """Print formatted results"""
    print(f"\n{pair_name}:")
    print(f"  Cosine Similarity: {results['cosine_similarity']:.4f}")
    print(f"  Euclidean Distance: {results['euclidean_distance']:.4f}")
    print(f"  Jaccard Similarity: {results['jaccard_similarity']:.4f}")

def create_similarity_plot(labels, cosine_vals, euclidean_vals, jaccard_vals):
    """Create visualization for similarity metrics"""
    x = np.arange(len(labels))
    width = 0.25
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Create bars with colors
    bars1 = ax.bar(x - width, cosine_vals, width, label='Cosine Similarity', 
                   color='#1f77b4', alpha=0.8)
    bars2 = ax.bar(x, euclidean_vals, width, label='Euclidean Distance', 
                   color='#ff7f0e', alpha=0.8)
    bars3 = ax.bar(x + width, jaccard_vals, width, label='Jaccard Similarity', 
                   color='#2ca02c', alpha=0.8)
    
    # Add value labels on bars
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                   f'{height:.3f}', ha='center', va='bottom', fontsize=9)
    
    plt.xlabel('CV Pairs', fontsize=12, fontweight='bold')
    plt.ylabel('Values', fontsize=12, fontweight='bold')
    plt.title('Similarity and Distance Metrics between CV Pairs', 
              fontsize=14, fontweight='bold')
    plt.xticks(x, labels)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()

# MAIN EXECUTION
def main():
    # Define CV pairs to compare
    cv_pairs = [
        ('CV1 & CV22', 0, 59),
        ('CV2 & CV21', 1, 70), 
        ('CV1 & CV2', 0, 1)
    ]
    
    # Store results
    all_results = []
    labels = []
    cosine_values = []
    euclidean_values = []
    jaccard_values = []
    
    print("=== CV SIMILARITY ANALYSIS ===")
    
    # Calculate similarities for each pair
    for pair_name, idx1, idx2 in cv_pairs:
        results = calculate_cv_similarity(idx1, idx2, data)
        
        # Print results
        print_similarity_results(pair_name, results)
        
        # Store for visualization
        all_results.append(results)
        labels.append(pair_name)
        cosine_values.append(results['cosine_similarity'])
        euclidean_values.append(results['euclidean_distance'])
        jaccard_values.append(results['jaccard_similarity'])
    
    # Create visualization
    create_similarity_plot(labels, cosine_values, euclidean_values, jaccard_values)
    
    return all_results


results = main()