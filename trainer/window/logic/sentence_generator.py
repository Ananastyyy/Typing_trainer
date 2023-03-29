from random import randint


class SentenceGenerator:
    sentences = [
        "Съешь ещё этих мягких французских булок",
        "Мама мыла раму",
        "Я пошёл гулять в парк",
        "Он приготовил обед для своих друзей",
        "Ребёнок играл в футбол на улице"
    ]
    size = len(sentences)

    def get_sentence(self):
        return self.sentences[randint(0, self.size - 1)]
