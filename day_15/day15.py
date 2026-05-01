import json
from collections import Counter


# COUNT LINES & WORDS


def count_lines_words(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)

        return num_lines, num_words

    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return 0, 0


# MOST SPOKEN LANGUAGES

def most_spoken_languages(filepath, top_n=10):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)

        languages = []

        for country in data:
            languages.extend(country.get('languages', []))

        counter = Counter(languages)

        return counter.most_common(top_n)

    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return []


# MAIN EXECUTION

def main():
    print("=== SPEECH ANALYSIS ===")

    files = {
        "Obama": "data/obama_speech.txt",
        "Michelle Obama": "data/michelle_obama_speech.txt",
        "Donald Trump": "data/donald_speech.txt",
        "Melania Trump": "data/melina_trump_speech.txt"
    }

    for name, path in files.items():
        lines, words = count_lines_words(path)
        print(f"{name} Speech -> Lines: {lines}, Words: {words}")

    print("\n=== TOP 10 LANGUAGES ===")
    languages = most_spoken_languages("data/countries_data.json")

    for lang, count in languages:
        print(f"{lang}: {count}")


if __name__ == "__main__":
    main()
