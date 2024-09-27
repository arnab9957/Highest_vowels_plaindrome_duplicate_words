def analyze_words(words):
    """Analyzes a list of words and identifies patterns.

    Args:
        words: A list of strings representing words.

    Returns:
        A tuple containing the highest vowel count, palindromes, and duplicate words.
    """

    vowel_counts = []
    palindromes = []
    word_counts = {}

    for word in words:
        # Count vowels
        vowel_count = sum(1 for char in word if char in "aeiouAEIOU")
        vowel_counts.append((word, vowel_count))

        # Check for palindromes
        if word == word[::-1]:
            palindromes.append(word)

        # Count word frequencies
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Find word with highest vowel count
    if vowel_counts:
        highest_vowel_word = max(vowel_counts, key=lambda item: item[1])
    else:
        highest_vowel_word = None

    # Find duplicate words
    duplicate_words = [word for word, count in word_counts.items() if count > 1]

    return highest_vowel_word, palindromes, duplicate_words


# Example usage
words = ["hello", "world", "madam", "level", "noon", "apple", "banana", "hello"]

highest_vowel_word, palindromes, duplicate_words = analyze_words(words)

print("Highest Vowels:", highest_vowel_word[0] if highest_vowel_word else "None")
print("Palindrome:", ", ".join(palindromes) if palindromes else "None")
print("Duplicate Words:", ", ".join(duplicate_words) if duplicate_words else "None")
