def thesaurus_adv(*args):
    i = dict()
    for name in args:
        last_name = name.split()[1][0]
        first_name = name[0]
        if last_name not in i:
            i[last_name] = dict()
        if first_name not in i[last_name]:
            i[last_name][first_name] = []
        i[last_name][first_name].append(name)
    return i


print(thesaurus_adv("Nathan Drake", "Dante Sparda", "Kung Lao", "Johny Silverhand", "Donkey Kong"))
