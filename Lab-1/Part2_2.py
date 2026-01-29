FILENAME = "pg2701.txt"

vowels = "aeiouy"

# --- Load entire file into an array ---
with open(FILENAME, "r", encoding="utf-8") as file:
    lines = file.readlines()

# --- Find the starting line ---
start_index = None
for i in range(len(lines)):
    if lines[i].strip() == "CHAPTER 1. Loomings.":
        start_index = i
        break

if start_index is None:
    print("Start line not found.")
    exit()

total_vowels = 0
total_words = 0

# --- Process the lines ---
for line in lines[start_index:]:
    words = line.split()
    for word in words:
        clean_word = ""
        for c in word:
            if c.isalpha():
                clean_word += c

        if clean_word != "":
            vowel_count = 0
            for ch in clean_word.lower():
                if ch in vowels:
                    vowel_count += 1

            total_vowels += vowel_count
            total_words += 1

# --- Compute average ---
if total_words > 0:
    average = total_vowels / total_words
    print("Average number of vowels per word:", average)
else:
    print("No words found.")

