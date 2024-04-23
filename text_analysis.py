import nltk
nltk.download('stopwords')
nltk.download('punkt')

import re
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Define the path to your input text file
input_file = "paragraphs.txt"

def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove non-alphanumeric characters and single characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Tokenize the text into words
    words = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

def count_word_frequency(words):
    # Count word frequency
    word_freq = Counter(words)
    return word_freq

def main():
    try:
        # Read the contents of the file
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Preprocess text (remove stopwords, tokenize)
        filtered_words = preprocess_text(text)
        
        # Count word frequency
        word_freq = count_word_frequency(filtered_words)
        
        # Display word frequency count
        for word, freq in word_freq.most_common():
            print(f'{word}: {freq}')

    except FileNotFoundError:
        print(f'Error: File "{input_file}" not found.')

if __name__ == "__main__":
    main()
