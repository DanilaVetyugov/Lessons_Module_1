nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

from random import choice


def get_jokes():
    someList = []
    listOne = choice(nouns)
    listTwo = choice(adverbs)
    listThree = choice(adjectives)
    someList.append(f"{listOne} {listTwo} {listThree}")
    return someList


print(get_jokes())