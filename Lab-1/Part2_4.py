import timeit

FILENAME = "pg2701.txt"
vowels = "aeiouy"

# -------- Load file ONCE (not timed) --------
with open(FILENAME, "r", encoding="utf-8") as file:
    lines = file.readlines()

# -------- Find start index --------
start_index = None
for i in range(len(lines)):
    if lines[i].strip() == "CHAPTER 1. Loomings.":
        start_index = i
        break

if start_index is None:
    print("Start line not found.")
    exit()


# -------- Function to time --------
def compute_average():
    total_vowels = 0
    total_words = 0

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

    average = total_vowels / total_words
    return average


# -------- Timing --------
runs = 100
total_time = timeit.timeit(compute_average, number=runs)
avg_time = total_time / runs

print("Average execution time over", runs, "runs:", avg_time, "seconds")
