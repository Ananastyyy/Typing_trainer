from random import randint


class SentenceGenerator:

    def __init__(self):
        self.sentences = [
            "Съешь ещё этих мягких французских булок",
            "Мама мыла раму",
            "Я пошёл гулять в парк",
            "Он приготовил обед для своих друзей",
            "Ребёнок играл в футбол на улице"
        ]
        self.size = len(self.sentences)

    def get_sentence(self):
        return self.sentences[randint(0, self.size - 1)]
