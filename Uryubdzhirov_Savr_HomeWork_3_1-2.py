NUMS = {'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'}

print('this is the number translator')


def num_translate_adv():
    eng_num = dict([[v, k] for k, v in NUMS.items()])
    find_num = input('Enter a number ' '')
    print(eng_num.get(find_num))


def lang_num():
    key = input('Enter a number ' '')
    print(NUMS.get(key))


if __name__ == '__main__':
    x = input('Enter a language of number(eng/rus): ' '')
    if x == 'rus':
        num_translate_adv()
    elif x == 'eng':
        lang_num()
