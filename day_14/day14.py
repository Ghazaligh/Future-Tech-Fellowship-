paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# Convert to lowercase and remove punctuation
cleaned = paragraph.lower().replace('.', '')

# Split into words
words = cleaned.split()

# Count frequency
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Find most frequent word
most_frequent = max(word_count, key=word_count.get)

print("Most frequent word:", most_frequent)
print("Count:", word_count[most_frequent])


import re

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

# Extract numbers (including negatives)
numbers = list(map(int, re.findall(r'-?\d+', text)))

print("Extracted numbers:", numbers)

# Find distance between furthest particles
distance = max(numbers) - min(numbers)

print("Distance between furthest particles:", distance)


import re
import keyword

def is_valid_variable(name):
    pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
    
    if re.match(pattern, name) and not keyword.iskeyword(name):
        return True
    return False


# Test cases
tests = ["name", "_age", "2value", "class", "user_name1"]

for t in tests:
    print(f"{t}: {is_valid_variable(t)}")


import re
from collections import Counter

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# Function to clean text
def clean_text(text):
    # Remove special characters (keep only letters and spaces)
    cleaned = re.sub(r'[^A-Za-z\s]', '', text)
    return cleaned

# Function to find most frequent words
def most_frequent_words(text):
    words = text.split()
    count = Counter(words)
    return count.most_common(3)

# Clean the text
cleaned_text = clean_text(sentence)
print(cleaned_text)

# Get most frequent words
print(most_frequent_words(cleaned_text))
