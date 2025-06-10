import itertools

keywords = ["it", "support", "iiit", "iiitk", "admin", "itsupport"]
special_chars = ["@", "!", "#"]
numbers = ["123", "2024"]

# Generate combinations of keywords with special characters and numbers
wordlist = set()
for word in keywords:
    wordlist.add(word)  # Basic word
    for num in numbers:
        wordlist.add(f"{word}{num}")  # With numbers
    for char in special_chars:
        wordlist.add(f"{word}{char}")  # With special characters
        for num in numbers:
            wordlist.add(f"{word}{char}{num}")  # With both

# Save to file
with open("custom_wordlist.txt", "w") as f:
    for word in sorted(wordlist):
        f.write(word + "\n")
