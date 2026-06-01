import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import nltk

nltk.download('punkt')

df = pd.read_csv('reviews.csv')
print("YOUR DATASET")
print(df)
print("Total rows:", len(df))

def get_sentiment(text):
    score = TextBlob(text).sentiment.polarity
    if score > 0.1:
        return 'Positive'
    elif score < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

def get_score(text):
    return round(TextBlob(text).sentiment.polarity, 2)

def get_emotion(score):
    if score >= 0.5:
        return 'Very Happy'
    elif score >= 0.1:
        return 'Happy'
    elif score <= -0.5:
        return 'Very Angry'
    elif score <= -0.1:
        return 'Unhappy'
    else:
        return 'Neutral'

df['sentiment'] = df['text'].apply(get_sentiment)
df['score'] = df['text'].apply(get_score)
df['emotion'] = df['score'].apply(get_emotion)

print("\nSENTIMENT RESULTS")
print(df[['source', 'text', 'sentiment', 'score', 'emotion']].to_string())

print("\nOVERALL SENTIMENT COUNT")
print(df['sentiment'].value_counts())

print("\nSENTIMENT BY SOURCE")
print(df.groupby(['source', 'sentiment']).size().unstack(fill_value=0))

colors1 = ['#66bb6a', '#ef5350', '#42a5f5']
df['sentiment'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=colors1, title='Overall Sentiment', figsize=(6, 6))
plt.ylabel('')
plt.tight_layout()
plt.savefig('chart1_overall.png')
plt.show()
print("Chart 1 saved")

colors2 = ['#ef5350', '#42a5f5', '#66bb6a']
df.groupby(['source', 'sentiment']).size().unstack(fill_value=0).plot(kind='bar', color=colors2, title='Sentiment by Source', figsize=(8, 5))
plt.xlabel('Source')
plt.ylabel('Number of Reviews')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('chart2_by_source.png')
plt.show()
print("Chart 2 saved")

df['emotion'].value_counts().plot(kind='bar', color='#7e57c2', title='Emotion Distribution', figsize=(8, 5))
plt.xlabel('Emotion')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('chart3_emotions.png')
plt.show()
print("Chart 3 saved")

pos = (df['sentiment'] == 'Positive').sum()
neg = (df['sentiment'] == 'Negative').sum()
neu = (df['sentiment'] == 'Neutral').sum()
total = len(df)

print("\nBUSINESS INSIGHTS")
print("Positive:", pos, "(" + str(round(pos/total*100)) + "%) -> Use in marketing")
print("Negative:", neg, "(" + str(round(neg/total*100)) + "%) -> Fix product issues")
print("Neutral :", neu, "(" + str(round(neu/total*100)) + "%) -> Engage customers")
print("Average Score:", round(df['score'].mean(), 2))

print("\nSOURCE WISE INSIGHTS")
for source in df['source'].unique():
    subset = df[df['source'] == source]
    avg = round(subset['score'].mean(), 2)
    dominant = subset['sentiment'].value_counts().idxmax()
    print(source + ": Avg Score=" + str(avg) + " Dominant=" + dominant)

print("\nTASK 4 COMPLETE!")