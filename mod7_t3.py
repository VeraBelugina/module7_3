class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = []
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for names in self.file_names:
            with open(names, 'r', encoding='utf-8') as file:
                name = file.read().lower()
                pun = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for p in pun:
                    name = name.replace(p, '')
                elem = name.split()
            all_words[names] = list(elem)
        return all_words

    def find(self, word):
        fi = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                fi[key] = value.index(word.lower()) + 1
        return fi

    def count(self, word):
        co = {}
        for k, v in self.get_all_words().items():
            co[k] = v.count(word.lower())
        return co


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
