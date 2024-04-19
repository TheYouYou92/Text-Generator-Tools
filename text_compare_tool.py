# text_compare_tool.py
import difflib
from collections import Counter

def compare(text1, text2):
    # Line by line comparison
    d = difflib.Differ()
    line_differences = list(d.compare(text1.splitlines(), text2.splitlines()))

    # Word frequency comparison
    words1 = text1.split()
    words2 = text2.split()
    word_freq1 = Counter(words1)
    word_freq2 = Counter(words2)
    word_freq_differences = {'text1': word_freq1 - word_freq2, 'text2': word_freq2 - word_freq1}

    # Character frequency comparison
    char_freq1 = Counter(text1)
    char_freq2 = Counter(text2)
    char_freq_differences = {'text1': char_freq1 - char_freq2, 'text2': char_freq2 - char_freq1}

    return {
        'line_differences': line_differences,
        'word_freq_differences': word_freq_differences,
        'char_freq_differences': char_freq_differences,
    }