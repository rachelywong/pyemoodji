from pyemoodji import __version__
from pyemoodji import pyemoodji
import pandas as pd
import pytest

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
    
def test_textsentiment_to_emoji():
    assert (
        pyemoodji.textsentiment_to_emoji(
            "I am hi", pd.DataFrame({"key": ["Fear"], "word": ["hi"]})
        )
        == "\U0001F631"
    )
    assert (
        pyemoodji.textsentiment_to_emoji("", pd.DataFrame({"key": ["Happy"], "word": ["hi"]}))
        == ""
    )

    with pytest.raises(TypeError):
        pyemoodji.textsentiment_to_emoji(123, pd.DataFrame({"key": ["Fear"], "word": ["hi"]}))

    with pytest.raises(TypeError):
        pyemoodji.textsentiment_to_emoji("I am sad", 123)

    with pytest.raises(Exception):
        pyemoodji.textsentiment_to_emoji(123, pd.DataFrame({"keys": ["Fear"], "words": ["hi"]}))

# Tests for counter function
def test_counter(text = "I am happy. This works."):
    assert isinstance(pyemoodji.counter(text), pd.DataFrame), 'output should be a dataframe'
    assert len(pyemoodji.counter(text).columns) == 3, 'output should have 3 columns'
    assert (pyemoodji.counter(text)).loc[0, "char_count"] == 23, 'output should be 23' 
    assert (pyemoodji.counter(text)).loc[0, "word_count"] == 5, 'output should be 5'   
    assert (pyemoodji.counter(text)).loc[0, "sentence_count"] == 2, 'output should be 2'  