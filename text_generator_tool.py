import lorem
import secrets

def generate(source):
    if source == 'lorem_ipsum':
        return lorem.text()
    elif source == 'random_words':
        words = ['apple', 'banana', 'cherry', 'date', 'elderberry']  # Add more words as needed
        return ' '.join(secrets.choice(words) for _ in range(5))
    elif source == 'random_sentences':
        sentences = ['The quick brown fox jumps over the lazy dog.', 'Jack and Jill went up the hill.']  # Add more sentences as needed
        return ' '.join(secrets.choice(sentences) for _ in range(3))
    elif source == 'random_paragraphs':
        paragraphs = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'Vestibulum condimentum dolor nec bibendum laoreet.']  # Add more paragraphs as needed
        return '\n\n'.join(secrets.choice(paragraphs) for _ in range(2))
    # Add more sources as needed
