doc1_tech = "Scientific innovations or technology is the most amazing thing that has ever happened to humankind. In this modern world, technology is no more a luxury; it has become a necessity. Life without technology is next to impossible since humans have become dependent on technological advancements. For every human activity, we need a machine, and then there comes technology. It has made all our lives easier and more convenient and has also made transportation, education, labour, etc., more accessible. Technological breakthroughs change from time to time in today’s fast-paced, ever-changing world. However, in today’s world, technology plays a critical role in strengthening a country’s economy and people’s lives."
doc2_health = "Health is wealth, and maintaining good health is essential for a happy and fulfilling life. A balanced diet, regular exercise, and adequate sleep are crucial components of a healthy lifestyle. In addition to physical health, mental well-being is equally important. Stress management, social connections, and mindfulness practices can significantly contribute to overall health. Preventive healthcare measures, such as vaccinations and regular medical check-ups, are vital in avoiding diseases and ensuring long-term health." 
doc3_sports = "Sports play a significant role in promoting physical fitness, teamwork, and discipline among individuals. Engaging in sports activities helps improve cardiovascular health, build muscle strength, and enhance flexibility. Moreover, sports foster social interaction and camaraderie, teaching valuable life skills such as leadership, perseverance, and time management. Whether it’s team sports like football and basketball or individual activities like tennis and swimming, participating in sports contributes to a well-rounded and healthy lifestyle."
doc4_travel = "Traveling opens up new horizons and broadens one’s perspective on the world. It allows individuals to experience different cultures, cuisines, and traditions, fostering a greater understanding and appreciation of diversity. Traveling can also be a source of relaxation and rejuvenation, providing a break from the routine of daily life. Whether exploring historical landmarks, natural wonders, or vibrant cities, travel enriches the mind and soul. Additionally, it can create lasting memories and strengthen relationships through shared experiences."
doc5_food = "Food is not just a source of nourishment; it is also a reflection of culture and tradition. Different regions around the world boast unique culinary practices and flavors, shaped by local ingredients and historical influences. A balanced diet that includes a variety of foods is essential for maintaining good health. Moreover, food brings people together, fostering social connections and shared experiences. From street food to gourmet dining, the world of food offers endless opportunities for exploration and enjoyment."
documents = [doc1_tech, doc2_health, doc3_sports, doc4_travel, doc5_food]

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())


#Visualize most frequent words
import matplotlib.pyplot as plt 

word_sums = tfidf_matrix.sum(axis=0)
words_freq = [(word, word_sums[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
top_n = 10
top_words = words_freq[:top_n]
words, freqs = zip(*top_words)
plt.figure(figsize=(10,6))
plt.bar(words, freqs, color='skyblue')
plt.xlabel('Words')
plt.ylabel('TF-IDF Score')
plt.title('Top 10 Words by TF-IDF Score')
plt.xticks(rotation=45)
plt.show()

from collections import Counter
all_words = ' '.join(documents).split()
word_counts = Counter(all_words).most_common(10)
words, counts = zip(*word_counts)
print("Most common words:", word_counts)

plt.figure(figsize=(10,6))
plt.bar(words, counts ,color="#BC1C1C")
plt.xlabel('Words')
plt.ylabel('TF-IDF Score')
plt.title('Top 10 Words by frequency counter')
plt.xticks(rotation=45)
plt.show()
