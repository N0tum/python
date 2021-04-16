nums = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
         'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

print('this is the number translater')
def num_translate_adv():
    eng_words = dict([[v, k] for k, v in nums.items()])
    find_word = input('Enter a number ' '')
    print(eng_words.get(find_word))


def lang_num():
    key = input('Enter a number ' '')
    print(nums.get(key))


if __name__ == '__main__':
    x = input('Enter a language of numbers(eng/rus): ' '')
    if x == 'rus':
        num_translate_adv()
    elif x == 'eng':
        lang_num()
