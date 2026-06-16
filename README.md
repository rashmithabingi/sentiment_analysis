# Sentiment Analysis
A Python-based sentiment analysis project that analyzes customer/user reviews
and visualizes emotional trends across different sources.

##  Project Structure

| File | Description |
| `sentiment.py` | Main Python script for sentiment analysis |
| `reviews.csv` | Dataset containing reviews for analysis |
| `chart1_overall.png` | Overall sentiment distribution chart |
| `chart2_by_source.png` | Sentiment breakdown by source |
| `chart3_emotions.png` | Emotion-wise analysis chart |

### Prerequisites
```bash
pip install pandas matplotlib nltk textblob
```
### Run
```bash
python sentiment.py
```

##  Features
- Analyzes sentiment (positive / negative / neutral) from reviews
- Breaks down sentiment by source
- Detects emotions across the dataset
- Generates visual charts for easy interpretation

##  Output Charts
- **Overall Sentiment** – pie/bar chart of sentiment distribution
- **By Source** – sentiment comparison across different platforms/sources
- **Emotions** – deeper emotion categorization

##  Tech Stack
- Python
- Pandas
- Matplotlib / Seaborn
- NLTK / TextBlob
