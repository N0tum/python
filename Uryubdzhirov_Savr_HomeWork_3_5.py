import random

NOUNS = ["автомобиль", "лес", "огонь", "город", "дом"]
ADVERBS = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
ADJECTIVES = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count_j):
    joke = []
    for i in range(count_j):
        joke.append(f"{NOUNS[random.randint(0, 4)]} {ADVERBS[random.randint(0, 4)]} {ADJECTIVES[random.randint(0, 4)]}")
    return joke


count = int(input("How many jokes you want? \n"))

print(f"Here the jokes: \n {get_jokes(count)}")
