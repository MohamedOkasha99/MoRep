import nltk
nltk.download('stopwords')
nltk.download('punkt')

import re
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

input_file = "paragraphs.txt"

def preprocess_text(text):
  
    text = text.lower()
    
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    words = word_tokenize(text)
  
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

def count_word_frequency(words):
   
    word_freq = Counter(words)
    return word_freq

def main():
    try:
        
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
        
        filtered_words = preprocess_text(text)
        
        
        word_freq = count_word_frequency(filtered_words)
        
      
        for word, freq in word_freq.most_common():
            print(f'{word}: {freq}')

    except FileNotFoundError:
        print(f'Error: File "{input_file}" not found.')

if __name__ == "__main__":
    main()
