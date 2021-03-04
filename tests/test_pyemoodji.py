from pyemoodji import __version__
from pyemoodji import pyemoodji
import pandas as pd

def test_version():
    assert __version__ == '0.1.0'

# Tests for sentiment analysis df function
def test_sentiment_df(text = "I am happy"):
    assert isinstance(pyemoodji.sentiment_df(text), pd.DataFrame), 'output should be a dataframe'
    assert len(pyemoodji.sentiment_df(text).columns) == 5, 'output should have 5 columns'
    assert (pyemoodji.sentiment_df(text)).loc[0, "word_count"] == 1, 'output should be 1 (1 happy in text)'   
    assert (pyemoodji.sentiment_df(text)).loc[0, "emotion_count"] == 1, 'output should be 1 (1 Happy in text)'  

# Tests for sentiment analysis plot function
def test_sentiment_plot(text = "I am happy"):
    plot = pyemoodji.sentiment_plot(text)
    assert plot.encoding.x.field == 'word', 'x_axis should be mapped to the x axis'
    assert plot.encoding.y.field == 'word_count', 'y_axis should be mapped to the y axis'
    assert plot.encoding.color.field == 'key', 'key should be mapped to the key'
    assert plot.mark == 'bar', 'mark should be a bar'