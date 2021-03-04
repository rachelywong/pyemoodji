from sentiment_df import sentiment_df
import pandas as pd
import pytest


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


# res = textsentiment_to_emoji(
#     "I am very happy but scared aswell. I was shocked too see mary was really angry with me though. I hope I could make her sadness go away"
# )
def test_textsentiment_to_emoji():
    assert (
        textsentiment_to_emoji(
            "I am hi", pd.DataFrame({"key": ["Fear"], "word": ["hi"]})
        )
        == "\U0001F631"
    )
    assert (
        textsentiment_to_emoji("", pd.DataFrame({"key": ["Happy"], "word": ["hi"]}))
        == ""
    )

    with pytest.raises(TypeError):
        textsentiment_to_emoji(123, pd.DataFrame({"key": ["Fear"], "word": ["hi"]}))

    with pytest.raises(TypeError):
        textsentiment_to_emoji("I am sad", 123)

    with pytest.raises(Exception):
        textsentiment_to_emoji(123, pd.DataFrame({"keys": ["Fear"], "words": ["hi"]}))
