import re
import string

def sort_words(words):
    ukrainian_alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'

    def sorting_key(word):
        first_letter = word[0].upper()
        if first_letter in ukrainian_alphabet:
            return (0, word.lower())  # українські слова
        return (1, word.lower())     # англійські слова

    return sorted(words, key=sorting_key)

def process_file(filename):
    try:
        # відкриття файлу в режимі 'r' (читання)
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        # пошук першого речення
        first_sentence = re.split(r'[.!?]', text)[0].strip()
        print("Перше речення:", first_sentence)

        # розбивка тексту на слова без пунктуації
        no_punctuation = str.maketrans('', '', string.punctuation)
        words = first_sentence.translate(no_punctuation).split()

        # сортування слів
        sorted_words = sort_words(words)

        # виведення відсортованих слів та їх кількості на екран
        print("Відсортовані слова:", sorted_words)
        print("Кількість слів:", len(words))

    except FileNotFoundError:
        print(f"Помилка: не знайдено файл '{filename}'.")
    except Exception as e:
        print(f"Виникла помилка під час опрацювання файлу: {e}")

process_file('text.txt')