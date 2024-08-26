import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

df = pd.read_csv("billboard_song_500.csv")
df['lyrics'] = df['lyrics'].astype('str')
text = df['lyrics'].tolist()

scores = []
sid = SentimentIntensityAnalyzer()

for word in text:
    ss = sid.polarity_scores(word)
    scores.append(ss['compound'])

print(scores)











