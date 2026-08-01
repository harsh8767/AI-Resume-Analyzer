import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk


# Download required NLTK resources (only first time)
nltk.download("punkt")
nltk.download("stopwords")


STOP_WORDS = set(stopwords.words("english"))


def preprocess_text(text):
    """
    Clean and tokenize text.
    Returns a list of meaningful words.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation and special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # Tokenize
    tokens = word_tokenize(text)

    # Remove stopwords
    filtered_tokens = [
        word
        for word in tokens
        if word not in STOP_WORDS and len(word) > 1
    ]

    return filtered_tokens