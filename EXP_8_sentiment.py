import PyPDF2
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)

    if scores['compound'] >= 0.05:
        return 'Positive'
    elif scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Example usage
pdf_path = 'C:/Users/Vedant Deshmukh/Documents/Final Year/NLP/EXP_2/novels/sign-of-the-four.pdf'
pdf_text = extract_text_from_pdf(pdf_path)

sentiment_result = analyze_sentiment(pdf_text)

print(f"Sentiment: {sentiment_result}")
