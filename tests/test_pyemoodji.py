from pyemoodji import pyemoodji
import pandas as pd
import pytest


# Tests for sentiment analysis df function
def test_sentiment_df(text="I am happy"):
    """
    Test function for the sentiment_df function. Tests that the
    output of the function is a Panda's dataframe with 5 columns and
    contains the correct values given a toy text file.

    Parameters:
    -----------
        text (str): the input text for sentiment analysis
        (toy text file = "I am happy")

    Returns:
    --------
        none: all tests have passed, alternatively returns error message
        if a test has not passed
    """
    # 'output should be a dataframe'
    assert isinstance(pyemoodji.sentiment_df(text), pd.DataFrame)
    # 'output should have 5 columns'
    assert len(pyemoodji.sentiment_df(text).columns) == 5
    # 'output should be 1 (1 happy in text)'
    assert (pyemoodji.sentiment_df(text)).loc[0, "word_count"] == 1
    assert (pyemoodji.sentiment_df(text)
            ).set_index("word"
                        ).loc["happy", "emotion_count"] == 1
    with pytest.raises(TypeError):
        pyemoodji.sentiment_df(123)
    with pytest.raises(TypeError):
        pyemoodji.sentiment_df("I am happy", sentiment=123)
    with pytest.raises(Exception):
        pyemoodji.sentiment_df("I am happy", sentiment="happy")


# Tests for sentiment analysis plot function
def test_sentiment_plot(text="I am happy"):
    """
    Test function for the sentiment_plot function. Tests that the
    output of the function is a bar plot showing word versus
    word_count, and colored by emotion.

    Parameters:
    -----------
        text (str): the input text for sentiment analysis
        (toy text file = "I am happy")

    Returns:
    --------
        none: all tests have passed, alternatively returns error message
        if a test has not passed
    """
    plot = pyemoodji.sentiment_plot(text)
    # 'x_axis should be mapped to the x axis'
    assert plot.encoding.x.shorthand == 'word'
    # 'y_axis should be mapped to the y axis'
    assert plot.encoding.y.shorthand == 'word_count'
    # 'key should be mapped to the key'
    assert plot.encoding.color.shorthand == 'key'
    # 'mark should be a bar'
    assert plot.mark == 'bar'
    with pytest.raises(TypeError):
        pyemoodji.sentiment_plot(123)
    with pytest.raises(TypeError):
        pyemoodji.sentiment_plot("I am happy", sentiment=123)
    with pytest.raises(TypeError):
        pyemoodji.sentiment_plot("I am happy", sentiment="all", width="a")
    with pytest.raises(TypeError):
        pyemoodji.sentiment_plot("I am happy",
                                 sentiment="all", width=10, height="b")
    with pytest.raises(Exception):
        pyemoodji.sentiment_plot("I am happy", sentiment="happy")


def test_textsentiment_to_emoji():
    """
    Test function for the textsentiment_to_emoji function. Tests that
    the output of the function is a string containing key sentiment
    words replaced by emojis. Exceptions are also raised to test
    that the error messages are working properly.

    Parameters:
    -----------
        text (str): the input text for sentiment analysis
        (toy text file = "I am happy")

    Returns:
    --------
        none: all tests have passed, alternatively returns error message
        if a test has not passed
    """
    assert (
        pyemoodji.textsentiment_to_emoji(
            "I am hi", pd.DataFrame({"key": ["Fear"], "word": ["hi"]})
        )
        == "\U0001F631"
    )
    assert (
        pyemoodji.textsentiment_to_emoji("",
                                         pd.DataFrame({"key": ["Happy"],
                                                       "word": ["hi"]}))
        == ""
    )

    with pytest.raises(TypeError):
        pyemoodji.textsentiment_to_emoji(123,
                                         pd.DataFrame({"key": ["Fear"],
                                                       "word": ["hi"]}))

    with pytest.raises(TypeError):
        pyemoodji.textsentiment_to_emoji("I am sad", 123)

    with pytest.raises(Exception):
        pyemoodji.textsentiment_to_emoji(123,
                                         pd.DataFrame({"keys": ["Fear"],
                                                       "words": ["hi"]}))


# Tests for counter function
def test_counter(text="I am happy. This works."):
    """
    Test function for the counter function. Tests that the output of the
    function is a Panda's dataframe containing 3 columns.
    Also contains certain test cases for a toy text file
    given to test each column contains the correct values.

    Parameters:
    -----------
        text (str): the input text for sentiment analysis
        (toy text file = "I am happy. This works")

    Returns:
    --------
        none: all tests have passed, alternatively returns error message
        if a test has not passed
    """
    # 'output should be a dataframe'
    assert isinstance(pyemoodji.counter(text), pd.DataFrame)
    # 'output should have 3 columns'
    assert len(pyemoodji.counter(text).columns) == 3
    # 'output should be 23'
    assert (pyemoodji.counter(text)).loc[0, "char_count"] == 23
    # 'output should be 5'
    assert (pyemoodji.counter(text)).loc[0, "word_count"] == 5
    # 'output should be 2'
    assert (pyemoodji.counter(text)).loc[0, "sentence_count"] == 2
    with pytest.raises(TypeError):
        pyemoodji.counter(123)
