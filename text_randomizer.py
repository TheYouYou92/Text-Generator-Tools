import random

def randomize_text(text: str, level: str) -> str:
    """
    Function to randomize the order of words, sentences, paragraphs, or characters in a given text.

    Parameters:
    - text: str
        The input text to be randomized.
    - level: str
        The level of randomization to be applied. It can be one of the following:
        - 'words': Randomize the order of words in the text.
        - 'sentences': Randomize the order of sentences in the text.
        - 'paragraphs': Randomize the order of paragraphs in the text.
        - 'characters': Randomize the order of characters in each word of the text.

    Returns:
    - str:
        The randomized text based on the specified level.

    Raises:
    - ValueError:
        Raises an error if the specified level is not one of the valid options.
    """

    # Splitting the text into words
    words = text.split()

    if level == 'words':
        # Randomizing the order of words
        random.shuffle(words)
        randomized_text = ' '.join(words)

    elif level == 'sentences':
        # Splitting the text into sentences
        sentences = text.split('. ')

        # Randomizing the order of sentences
        random.shuffle(sentences)
        randomized_text = '. '.join(sentences)

    elif level == 'paragraphs':
        # Splitting the text into paragraphs
        paragraphs = text.split('\n\n')

        # Randomizing the order of paragraphs
        random.shuffle(paragraphs)
        randomized_text = '\n\n'.join(paragraphs)

    elif level == 'characters':
        # Randomizing the order of characters in each word
        randomized_words = []
        for word in words:
            # Splitting each word into characters
            characters = list(word)

            # Randomizing the order of characters
            random.shuffle(characters)

            # Joining the characters back into a word
            randomized_word = ''.join(characters)
            randomized_words.append(randomized_word)

        randomized_text = ' '.join(randomized_words)

    else:
        raise ValueError("Invalid level. Please choose one of the following: 'words', 'sentences', 'paragraphs', 'characters'.")

    return randomized_text



