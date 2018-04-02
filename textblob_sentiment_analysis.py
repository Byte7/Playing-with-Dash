from textblob import TextBlob

analysis = TextBlob("python sure has some amazing features")
print(dir(analysis))
print(analysis.translate(to='es'))
print(analysis.tags)
print(analysis.sentiment)