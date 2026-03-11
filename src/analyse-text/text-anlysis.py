import os
from dotenv import load_dotenv
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Load environment variables
load_dotenv()

endpoint = os.getenv("AI_SERVICE_ENDPOINT")
key = os.getenv("AI_SERVICE_KEY")

credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)


# Load reviews from folder
def load_reviews(folder="reviews"):
    reviews = []

    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        with open(path, "r", encoding="utf-8") as f:
            reviews.extend(f.readlines())

    return [r.strip() for r in reviews if r.strip()]


# Helper function to split reviews into batches of max n
def chunks(lst, n):
    """Yield successive n-sized chunks from list"""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def analyze_reviews():
    reviews = load_reviews()

    for batch in chunks(reviews, 10):  # Batch of max 10
        sentiments = client.analyze_sentiment(batch)
        languages = client.detect_language(batch)

        for review, lang, sent in zip(batch, languages, sentiments):
            print("\nReview:", review)
            print("Detected Language:", lang.primary_language.name)
            print("Language Code:", lang.primary_language.iso6391_name)
            print("Sentiment:", sent.sentiment)
            print("Positive:", sent.confidence_scores.positive)
            print("Neutral:", sent.confidence_scores.neutral)
            print("Negative:", sent.confidence_scores.negative)


if __name__ == "__main__":
    analyze_reviews()