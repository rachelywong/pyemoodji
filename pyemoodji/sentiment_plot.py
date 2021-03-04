from nltk.tokenize import TweetTokenizer, RegexpTokenizer

from nltk import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download("stopwords")
import pandas as pd
import text2emotion as te
import altair as alt

def sentiment_plot(text, sentiment = "happy", width=800, height=300):
    """
    Generates a plot to show the top 10 sentiment words in the input text file.

    Parameters:
    -----------
        text (str): the input text for sentiment analysis
        sentiment (str, optional): the sentiment that the analysis focuses on. Defaults to "happy".
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