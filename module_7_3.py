import io
from pprint import pprint
import re

class WordsFinder:
    file_names = []
    def __init__(self, *files):
        self.files = files

    def __str__(self):
        return f'{self.files}'

    def get_all_words(self):
        all_words = {}
        keys = []
        values = []
        for i in self.files:
            keys.append(i)
            with open(i, 'r', encoding='utf-8') as file:
                 content = file.read()
                 lower_content = content.lower()
                 with open(i, 'w', encoding='utf-8') as file:
                     file.write(lower_content)
        new_text = re.sub(r'[^\w\s]', '', lower_content)
        values.append(new_text.split())
        all_words = dict(zip(keys, values))
        return all_words

    def find(self, word):
        self.word = word
        dict_1 = {}
        for keys, values in self.get_all_words().items():
            if self.word.lower() in values:
                b = values.index(self.word.lower())
                a = keys
                print(dict(zip(a, b)))
        return dict_1

    # def count(self, word):
    #     self.word = word
    #     dict_1 = {}
    #     k = 0
    #     for keys, values in self.get_all_words().items():
    #         if self.word.lower() in values:
    #             k += 1
    #             print(k)
    #     #         dict_1 = dict(zip(a, b))
    #     # return dict_1

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего