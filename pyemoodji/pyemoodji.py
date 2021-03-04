# Python script for pyemoodji package

import nltk
nltk.download("stopwords")
from nltk.tokenize import TweetTokenizer, RegexpTokenizer
from nltk import word_tokenize
import pandas as pd
import text2emotion as te
from nltk.corpus import stopwords
import altair as alt
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
    num_char = 0
    num_word = 0
    num_sentences = 0
    
    for char in text:
        num_char += 1
    
    num_word = len(re.findall(r'\w+', text))
    
    number_of_sentences = sent_tokenize(text)

    num_sentences = len(number_of_sentences)
    
    return pd.DataFrame({"char_count": [num_char], "word_count": [num_word], "sentence_count": [num_sentences]})
  

def sentiment_df(text, sentiment="all"):
    """
    Generates a sentiment analysis summary dataframe of the input text. The summary dataframe would include 
    the sentiment type, sentiment words, number of sentiment words, and highest sentiment percentage.

    Parameters:
    -----------
        text (str): the input text for sentiment analysis
        sentiment (str, optional): the sentiment that the analysis focuses on, could be happy, angry, or sad etc. Defaults to "all".

    Returns:
    --------
        data frame: a data frame that contains the summary of sentiment analysis
    """

    sen_list = ["all", "Happy", "Sad", "Surprise", "Fear", "Angry"]
    
    if not type(text) is str:
        raise TypeError("Only strings are allowed for function input")
    elif not type(sentiment) is str:
        raise TypeError("Only strings are allowed for sentiment input")
    elif sentiment not in sen_list:
        raise Exception("Input not in ['all', 'Happy', 'Sad', 'Surprise', 'Fear', 'Angry']")

    
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    word_list = tokenizer.tokenize(text)

    stop_words = set(stopwords.words("english"))

    cleaned_list = []

    for i in word_list:
        if i not in stop_words:
            cleaned_list.append(i)
    
    count_dict = {}
    for i in cleaned_list:
        count_dict[i] = cleaned_list.count(i)


    df = pd.DataFrame()
    for i in set(cleaned_list):
        df_current = pd.DataFrame()
        dictionary = te.get_emotion(i)
        df_current = pd.DataFrame(dictionary, index = [i])
        if sum(dictionary.values()) == 0:
            df_current["key"] = "None"
        else:
            key = max(dictionary, key=dictionary.get)
            df_current["key"] = key
        df = pd.concat([df, df_current])

    df['emotion_count'] = df.sum(axis=1)

    for i in list(df.index):
        df.loc[i, "word_count"] = count_dict[i]
    df = df.reset_index().rename(columns={'index':'word'})

    df['dummy'] = df['emotion_count'] * df['word_count']
    total_emotion = df['dummy'].sum()
    
    df['emotion_percentage'] = df['dummy'] / total_emotion

    if sentiment == "all":
        return df[["word", "key", "emotion_count", "emotion_percentage", "word_count"]]
    else:
        df = df[df["key"] == sentiment]
        return df[["word", "key", "emotion_count", "emotion_percentage", "word_count"]]

    return df

def sentiment_plot(text, sentiment = "Happy", n=10, width=10, height=10):
    """
    Generates a plot to show the top n sentiment words in the input text file. 

    Parameters:
    -----------
        text (str): the input text for sentiment analysis
        sentiment (str, optional): the sentiment that the analysis focuses on. Defaults to "happy".
        n (int, optional): the number of sentiment words to show in the plot
        width (int, optional): the width of the output plot. Defaults to 10.
        height (int, optional): the height of the output plot. Defaults to 10.
    
    Returns:
    --------
        graph: a plot that shows the top n sentiment words of the input text file
    """

    sen_list = ["all", "Happy", "Sad", "Surprise", "Fear", "Angry"]
    
    if not type(text) is str:
        raise TypeError("Only strings are allowed for function input")
    elif not type(sentiment) is str:
        raise TypeError("Only strings are allowed for sentiment input")
    elif not type(width) is int:
        raise TypeError("Only integers are allowed for width input")
    elif not type(height) is int:
        raise TypeError("Only integers are allowed for height input")
    elif sentiment not in sen_list:
        raise Exception("Input not in ['all', 'Happy', 'Sad', 'Surprise', 'Fear', 'Angry']")
    



    df = sentiment_df(text, sentiment = sentiment)
    df = df.sort_values(by=['emotion_percentage'], ascending=False)
    df = df[0:10]

    title = "Top 10 " + sentiment + " Words"
    sentiment_plot = alt.Chart(df, title = title).mark_bar().encode(
        x=alt.X('word', title = 'Word', axis=alt.Axis(labelAngle=-45)),
        y=alt.Y('word_count', title = 'Word Count in Text'),
        color=alt.Color("key", title = "Emotion")
    ).properties(
        width=width,
        height=height
    ).configure_axis(
        labelFontSize=15,
        titleFontSize=15
    ).configure_title(fontSize=20)

    return sentiment_plot


def textsentiment_to_emoji(text, sentiment_dataframe=None):
    """
    Detect the word sentiments of a text and replace the
    with the matching emojis.

    Parameters:
    -----------

        text (str): A text string containing english words

        sentiment_dataframe (pandas dataframe) : A dataframe which contains
        word and key column which shows the sentiment of each word. Only supports
        the Happy, Sad, Suprise, Fear and Angry as keys. If no dataframe is given
        the results of sentiment_df function would be used.

    Returns:
    --------
        [str]: A string containing only emoji's with no words.
            The emojis are written in the CLDR short name format.

    example:
        textsentiment_to_emoji("I am very happy")
        returns: "\U0001f600"
    """

    # testing text be a str type
    if not type(text) is str:
        raise TypeError("text must be a str type")

    # If no dataframe is given use the results of sentiment_df
    if sentiment_dataframe is None:
        sentiment_dataframe = sentiment_df(text)

    # testing type to be dataframe and also to contain two columns named 'word' and 'key'
    if not type(sentiment_dataframe) is pd.core.frame.DataFrame:
        raise TypeError("sentiment_dataframe must be a pandas DataFrame type")

    if not "word" in sentiment_dataframe or not "key" in sentiment_dataframe:
        raise Exception(
            "sentiment_dataframe must have the two columns 'word' and 'key'"
        )

    # Add the emojis of each word one by one
    emojis = []
    for word in text.split():
        word_emotion = sentiment_dataframe.query("word==@word").loc[:, "key"]
        # If the word doesn't exist in the dataframe skip the word
        if len(word_emotion) == 0:
            continue
        if word_emotion.iloc[0] == "Happy":
            emojis.append("\U0001f600")
        elif word_emotion.iloc[0] == "Sad":
            emojis.append("\U0001F62D")
        elif word_emotion.iloc[0] == "Surprise":
            emojis.append("\U0001F62E")
        elif word_emotion.iloc[0] == "Fear":
            emojis.append("\U0001F631")
        elif word_emotion.iloc[0] == "Angry":
            emojis.append("\U0001F621")
    # join all the emojis to a single string
    return "".join(emojis)
