from pyemoodji import __version__
from pyemoodji import pyemoodji

def test_version():
    assert __version__ == '0.1.0'

# Tests for sentiment analysis df function
def test_sentiment_df():
    assert small_scatter.encoding.x.field == 'year', 'x_axis should be mapped to the x axis'
    assert small_scatter.encoding.y.field == 'measure', 'y_axis should be mapped to the y axis'
    assert small_scatter.mark == 'line', 'mark should be a line'
    assert small_scatter.encoding.x.scale.zero == False, "x-axis should not start at 0"
    assert small_scatter.encoding.x.axis.tickMinStep == 1, "x-axis small tick step should be 1"

# Tests for sentiment analysis plot function
def test_sentiment_plot():
    assert small_scatter.encoding.x.field == 'year', 'x_axis should be mapped to the x axis'
    assert small_scatter.encoding.y.field == 'measure', 'y_axis should be mapped to the y axis'
    assert small_scatter.mark == 'line', 'mark should be a line'
    assert small_scatter.encoding.x.scale.zero == False, "x-axis should not start at 0"
    assert small_scatter.encoding.x.axis.tickMinStep == 1, "x-axis small tick step should be 1"