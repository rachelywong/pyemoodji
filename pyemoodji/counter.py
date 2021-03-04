import pandas as pd
import re
from nltk.tokenize import sent_tokenize

def counter(text):
    """
    Generates a summary dataframe of the input text which contains counts for characters, words, and sentences.
    
    Parameters:
    -----------
        text (str): the input text for sentiment analysis
        
    Returns:
    --------
        data frame: a data frame that contains the summary statistics for character, word, and sentence count.
    
    example:
        text_counter("I am very happy.")
        returns: {'characters':16,'words':4,'sentences':1}
    """
    def counter(text):
        num_char = 0
        num_word = 0
        num_sentences = 0

        for char in text:
            num_char += 1
            
        num_word = len(re.findall(r'\w+', text))

        number_of_sentences = sent_tokenize(text)

        num_sentences = len(number_of_sentences)

        return pd.DataFrame({"char_count": [num_char], "word_count": [num_word], "sentence_count": [num_sentences]})