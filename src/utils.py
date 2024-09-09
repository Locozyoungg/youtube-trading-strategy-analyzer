import re
import string

def clean_text(text):
    """
    Cleans and formats text by removing extra whitespace, punctuation, and converting to lowercase.
    
    Args:
        text (str): Text to be cleaned.
    
    Returns:
        str: Cleaned text.
    """
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert to lowercase
    text = text.lower()
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_keywords(text, num_keywords=10):
    """
    Extracts keywords from text based on word frequency.
    
    Args:
        text (str): Text to extract keywords from.
        num_keywords (int): Number of top keywords to extract.
    
    Returns:
        list: List of top keywords.
    """
    from collections import Counter
    
    # Tokenize text
    words = text.split()
    # Count word frequency
    word_counts = Counter(words)
    # Get most common keywords
    keywords = [word for word, count in word_counts.most_common(num_keywords)]
    return keywords

def format_strategy_details(strategy):
    """
    Formats strategy details for better readability.
    
    Args:
        strategy (dict): Dictionary containing strategy details.
    
    Returns:
        str: Formatted strategy details.
    """
    formatted_details = f"Strategy: {strategy.get('strategy', 'N/A')}\n"
    formatted_details += f"Details: {strategy.get('details', 'No details available')}\n"
    return formatted_details

def summarize_text(text, max_length=500):
    """
    Summarizes the text to a specified maximum length.
    
    Args:
        text (str): Text to be summarized.
        max_length (int): Maximum length of the summarized text.
    
    Returns:
        str: Summarized text.
    """
    if len(text) > max_length:
        # Truncate text and add ellipsis
        return text[:max_length] + '...'
    return text

def validate_url(url):
    """
    Validates if a URL is properly formatted.
    
    Args:
        url (str): URL to be validated.
    
    Returns:
        bool: True if URL is valid, False otherwise.
    """
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None
