 from collections import Counter

def count_word_frequencies(text):
    words = text.lower().split()
    word_counts = Counter(words)
    return word_counts

# Example usage
text = "This is a sample text. This text is a simple example."
word_frequencies = count_word_frequencies(text)

# Display word frequencies
for word, count in word_frequencies.items():
    print(f"{word}: {count}")