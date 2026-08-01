import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure required NLTK resources are available
resources = [
    ("tokenizers/punkt", "punkt"),
    ("tokenizers/punkt_tab", "punkt_tab"),
    ("corpora/stopwords", "stopwords"),
]

for path, package in resources:
    try:
        nltk.data.find(path)
    except LookupError:
        nltk.download(package)

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