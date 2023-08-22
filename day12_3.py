import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob

#Download NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

#Sample text
text = "Natural language processing is a field of artificial intelligence that deals with the interaction" \
       "between computers and humans using natural language."

#Tokenization using NLTK
words = word_tokenize(text) 
sentences = sent_tokenize(text)

#Part-of-speech tagging using NLTK
pos_tags = nltk.pos_tag(words)

#Sentiment analysis using TextBlob
blob = TextBlob(text)
sentiment_score = blob.sentiment.polarity

#Display results
print("Original Text:")
print(text)
print("\nTokenized Word:")
print(words)
print("\nSentences")
print(sentences)
print("\nParts-of-Speech Tags")
print(pos_tags)
print("\nSentiment Score:",sentiment_score)

#Filtering stopwords using NLTK
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word.lower() not in stop_words]
print("\nFiltered Words (without stopwords):")
print(filtered_words)