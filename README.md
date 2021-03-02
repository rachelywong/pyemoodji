# pyemoodji 

![](https://github.com/UBC-MDS/pyemoodji/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/pyemoodji/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/pyemoodji) ![Release](https://github.com/UBC-MDS/pyemoodji/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/pyemoodji/badge/?version=latest)](https://pyemoodji.readthedocs.io/en/latest/?badge=latest)

Pyemoodji is a text analysis package that focuses on sentiment analysis in text files in quantitative and qualitative ways. Specifically, it is used for determining what kind of underlying emotion your input text gives off and quantitatives analyses of your text (character, word, and sentence count as well as visual and quantitative sentiment analysis). The emotions analyzed include angry, sad, happy, and disgust. Another core feature of Pyemoodji is it replaces words with emojis to provide the user with a text file where it is easier to pick up on the emotions being conveyed in a visually appealling snapshot view. This package can be useful when proofreading an important message which you want to elicit a certain emotion or tone, particularly with a given pattern or rhythm (speeches, letters, applications, songs, poems, etc).

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ pyemoodji
```
## Functions

Counter:
- With an input of textfile it will output a dataframe with character count, word count, and sentence count.

Sentiment Analysis Dataframe:
- With an input of a textfile it will output a dataframe with sentiment analysis (e.g. sentiment type, sentiment words, and percentage of overall sentiment per emotion).

Character Replacement:
- With the input of a textfile and the ability to choose which emotions you would like to replace (e.g. certain emotions or all) it will output a textfile that has emotional words replaced with emojis.

Sentiment Analysis Plot:
- With the input of a dataframe from the sentiment analysis function it will output a visualization on the most emotionally charged words that appear in the text.

## Contribution to Ecosystem

- While [tidytext](https://github.com/juliasilge/tidytext) (R) and [nltk](https://github.com/nltk/nltk) (Python) already exist, this package takes it a step further by providing qualitative sentiment analysis in a visually appealing format by replacing emotional words with emojis and further analyzing text data to provide more quantitative sentiment analysis.
- We also add visualizations to further this quantitative sentiment analysis in a way that these packages do not.

## Documentation

The official documentation is hosted on Read the Docs: https://pyemoodji.readthedocs.io/en/latest/

## Dependencies

- TODO

## Contributors

* [Aidan Mattrick](https://github.com/aidanmattrick)
* [Kevin Shahnazari](https://github.com/kshahnazari1998)
* [Zhanyi Su](https://github.com/YikiSu)
* [Rachel Wong](https://github.com/rachelywong)

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
