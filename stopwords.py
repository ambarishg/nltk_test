import nltk
from nltk.corpus import stopwords

def get_stopwords(language='english'):
    """
    Returns a set of stopwords for the specified language.
    
    :param language: The language for which to retrieve stopwords (default is 'english').
    :return: A set of stopwords.
    """
    try:
        return set(stopwords.words(language))
    except Exception as e:
        print(f"Error retrieving stopwords for language '{language}': {e}")
        return set()

print(get_stopwords('english'))  # Example usage
    
