# Python script for pyemoodji package


























































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
