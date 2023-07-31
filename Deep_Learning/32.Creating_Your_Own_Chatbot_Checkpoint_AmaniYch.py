# Import libraries
import requests
import nltk
nltk.download('wordnet')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# 1. Choose a topic: Choose a topic that you are interested in and find a text file related to that topic.
# You can use websites such as Project Gutenberg to find free text files.
# Get the text file from the URL
url = "https://www.gutenberg.org/cache/epub/42671/pg42671.txt"
response = requests.get(url)
# Open and save the file
with open("pg42671.txt", "wb") as file:
    file.write(response.content)
# Load the text file and preprocess the data
with open('pg42671.txt', 'r', encoding='utf-8') as f:
    data = f.read()

# 2. Preprocess the data: Modify the preprocess() function in the code provided to preprocess the data in your text file.
# You may want to modify the stop words list or add additional preprocessing steps to better suit your needs.
# Tokenize the text into sentences
sentences = sent_tokenize(data)
# Define a function to preprocess each sentence
def preprocess(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)
    # Remove stopwords and punctuation
    words = [word.lower() for word in words if word.lower() not in stopwords.words('english') and word not in string.punctuation]
    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    # Convert the list of words back to a sentence
    processed_sentence = ' '.join(words)
    return processed_sentence
# Preprocess each sentence in the text
corpus = [preprocess(sentence) for sentence in sentences]

# 3. Define the similarity function: Modify the get_most_relevant_sentence() function to compute the similarity between
# the user's query and each sentence in your text file.
# You may want to modify the similarity metric or add additional features to improve the performance of your chatbot.
# Define a function to find the most relevant sentence given a query
def get_most_relevant_sentence(query, sentences):
    vectorizer = CountVectorizer().fit_transform(sentences + [query])
    vectors = vectorizer.toarray()
    similarity_scores = cosine_similarity(vectors)
    most_similar_index = similarity_scores.shape[0] - 1
    most_relevant_index = similarity_scores[most_similar_index].argsort()[-2]
    return sentences[most_relevant_index]

# 4. Define the chatbot function: Modify the chatbot() function to return an appropriate response based on the most relevant
# sentence in your text file.
# The chatbot function
def chatbot(question):
    # Preprocess the user's question
    processed_question = preprocess(question)
    # Find the most relevant sentence
    most_relevant_sentence = get_most_relevant_sentence(processed_question, corpus)
    # Return the answer
    return most_relevant_sentence

# 5. Create a Streamlit app: Use the main() function in the code provided as a template to create a web-based chatbot interface.
# Prompt the user for a question, call the chatbot() function to get the response, and display it on the screen.
# Create a Streamlit app
def main():
    st.title("Pride and Prejudice Chatbot")
    st.write("Hello! I'm a chatbot. Ask me anything about Pride and Prejudice Novel.")
    # Get the user's question
    question = st.text_input("Question:")
    # Create a button to submit the question
    if st.button("Submit"):
        # Call the chatbot function with the question and display the response
        response = chatbot(question)
        st.write("Chatbot response: ")
        st.text(response)
if __name__ == "__main__":
    main()