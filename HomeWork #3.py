# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашнее задание по теме "Оператор "with"

import string


class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        file_string = ", ".join(self.file_names)
        file_list = file_string.split(', ')

        for i in file_list:
            with open(i, 'r', encoding='utf-8') as file:
                file_content = file.read()
                words_string = (' '.join(file_content.split('\n'))).lower()
                marks = str.maketrans('', '', string.punctuation)
                words_string = words_string.translate(marks)
                all_words_list = words_string.split(' ')
                all_words[i] = all_words_list
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        word = word.lower()
        result = {}
        for file_name, words in all_words.items():
            if word in words:
                position = words.index(word) + 1
                result[file_name] = position
        return result

    def count(self, word):
        all_words = self.get_all_words()
        word = word.lower()
        result = {}
        for file_name, words in all_words.items():
            count = words.count(word)
            result[file_name] = count
        return result


finder = WordsFinder('test_file_1.txt, test_file_2.txt', 'test_file_3.txt')
# print(finder.get_all_words())
# finder2 = WordsFinder('test_file.txt')
print(finder.get_all_words())  # Все слова
print(finder.find('TEXT'))  # 3 слово по счёту
print(finder.count('teXT'))  # 4 слова teXT в тексте всего
