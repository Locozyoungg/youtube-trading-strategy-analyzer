import spacy

# Load the NLP model
nlp = spacy.load('en_core_web_sm')

def preprocess_text(transcription):
    """
    Cleans and preprocesses the transcription text.
    
    Args:
        transcription (str): Raw transcription text from audio.
    
    Returns:
        str: Cleaned and preprocessed text.
    """
    filler_words = ["um", "uh", "you know", "like", "so", "actually", "basically"]
    cleaned_text = transcription
    for filler in filler_words:
        cleaned_text = cleaned_text.replace(filler, "")
    return cleaned_text

def extract_strategies(cleaned_text):
    """
    Extracts trading strategies from the cleaned text using NLP.
    
    Args:
        cleaned_text (str): Preprocessed transcription text.
    
    Returns:
        list: A list of extracted trading strategies with details.
    """
    doc = nlp(cleaned_text)
    strategies = []
    for sent in doc.sents:
        if "strategy" in sent.text.lower() or "trade" in sent.text.lower():
            strategies.append(sent.text)
    detailed_strategies = [
        {"strategy": s, "details": "Details extracted here (e.g., entry points, indicators)"}
        for s in strategies
    ]
    return detailed_strategies
