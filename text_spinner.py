from nltk.corpus import wordnet
import secrets
 
def text_spinner(text):
    """
    Function to spin the text by replacing words or phrases with synonyms.
 
    Parameters:
    - text: str
        The input text to be spun.
 
    Returns:
    - str:
        The spun text with replaced words or phrases.
 
    Raises:
    - ValueError:
        Raises an error if the input text is empty.
    """
 
    # Checking if the input text is empty
    if not text:
        raise ValueError("Input text cannot be empty.")
 
    # Splitting the text into words
    words = text.split()
 
    # Spinning each word in the text
    spun_words = []
    for word in words:
        # Checking if the word has synonyms
        synonyms = wordnet.synsets(word)
        if synonyms:
            # Choosing a random synonym for the word
            synonym = secrets.choice(synonyms).lemmas()[0].name()
            spun_words.append(synonym)
        else:
            spun_words.append(word)
 
    # Joining the spun words back into a spun text
    spun_text = ' '.join(spun_words)
 
    return spun_text
 
