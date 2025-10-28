"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""

def count_characters(text):
    """Count non-space characters in a string."""
    return len(text.replace(" ", ""))

def count_words(text):
    """Count number of words in a string."""
    return len(text.split())

def extract_numbers(text):
    """Return list of integers found in text."""
    numbers = []
    for item in text.split():
        if item.isdigit():
            numbers.append(int(item))
    return numbers

def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    char_count = count_characters(text)
    word_count = count_words(text)
    nums = extract_numbers(text)
    total = sum(nums) if nums else 0
    avg = total / len(nums) if nums else 0
    return char_count, word_count, total, avg

if __name__ == "__main__":
    text = input("Enter text: ")
    char_count, word_count, total, avg = analyze_text(text)
    print(f"Non-space characters: {char_count}")
    print(f"Word count: {word_count}")
    print(f"Sum of numbers: {total}")
    print(f"Average of numbers: {avg}")
