# Python script for pyemoodji package
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
  

def sentiment_df(text, sentiment="all"):
    """
    Generates a sentiment analysis summary dataframe of the input text. The summary dataframe would include 
    the sentiment type, sentiment words, percentage of sentiments and highest sentiment percentage.

    Parameters:
    -----------
        text (str): the input text for sentiment analysis
        sentiment (str, optional): the sentiment that the analysis focuses on, could be happy, positive or sad etc. Defaults to "all".

    Returns:
    --------
        data frame: a data frame that contains the summary of sentiment analysis
    """

    return result_df

  
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


def sentiment_plot(text, sentiment = "happy", n=10, width=10, height=10):
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



























































