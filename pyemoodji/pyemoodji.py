def textsentiment_to_emoji(text):
    """
    Detect the word sentiments of a text and replace the
    with the matching emojis.

    Parameters:
    -----------

        text (str): A text string containing english words

    Returns:
    --------
        [str]: A string containing only emoji's with no words.
            The emojis are written in the CLDR short name format.

    example:
        textsentiment_to_emoji("I am very happy")
        returns: "\N{smiling face with smiling eyes}"
    """
    return None


def text_counter(text):
    """
    Counts the number of characters, words and sentences of a string.

    Parameters:
    -----------
        text (str): A text string which could contain any number
        of english words

    Returns:
    --------
        [dictionary]: A dictionary containing the number of characters,
        words and sentences. They could be indexed by using ['characters'],
        ['words'] and ['sentences']

    example:
        text_counter("I am very happy")
        returns: {'characters':15,'words':4,'sentences':1}
    """
    return None