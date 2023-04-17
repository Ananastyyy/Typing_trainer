import json
from random import randint


class SentenceGenerator:

    def __init__(self):
        self._read_sentences()
        self.size = len(self.sentences)

    def _read_sentences(self):
        with open('database/sentences.json', 'r', encoding="UTF-8") as f:
            self.sentences = json.load(f)

    def get_sentence(self):
        return self.sentences[randint(0, self.size - 1)]
