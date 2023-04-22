from textblob import TextBlob
from newspaper import Article
import nltk

# commented code to scan existing articles
# nltk.download("all") # Download all the packages one time
# url = 'https://www.bbc.com/news/uk-england-london-52963555'
# article = Article(url)

# article.download()
# article.parse()
# article.nlp()

# text = article.summary
# print(text)

# to scan our own text
with open('mytext.txt', 'r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity  # - 1 to 1 on sentiment
print(sentiment)
