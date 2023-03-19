import time
import random


def typing_trainer():
    print("Добро пожаловать в тренажер набора текста!")
    time.sleep(1)
    while True:
        print("Нажмите enter, чтобы начать набор.")
        input()
        sentence = generate_sentence()
        print("Наберите предложение ниже:\n")
        print(sentence)
        start_time = time.time()
        typed_sentence = input()
        end_time = time.time()
        typing_time = end_time - start_time
        correct_chars = 0
        for i in range(min(len(sentence), len(typed_sentence))):
            if sentence[i] == typed_sentence[i]:
                correct_chars += 1
        accuracy = correct_chars / len(sentence) * 100
        print(f"\nВаше время: {typing_time:.2f} секунд")
        print(f"Точность: {accuracy:.2f}%\n")
        time.sleep(1)


def generate_sentence():
    sentences = [
        "Съешь ещё этих мягких французских булок да выпей чаю",
        "Мама мыла раму",
        "Я пошёл гулять в парк",
        "Он приготовил обед для своих друзей",
        "Ребёнок играл в футбол на улице"
    ]
    return sentences[random.randint(0, len(sentences) - 1)]


typing_trainer()
