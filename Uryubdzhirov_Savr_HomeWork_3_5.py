import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

ran_nou = random.choice(nouns)
ran_adv = random.choice(adverbs)
ran_adj = random.choice(adjectives)

def get_jokes():
    for nou, adv, adj in zip(ran_nou, ran_adv, ran_adj):
        print(f'{nou}, {adv}, {adj}')

get_jokes()

# не доделал, ищу причину моей проблемы
