import random
# пытаюсь создать рандомизатор чисел

def sample_floats(low, high, k=1):

    result = []
    seen = set()
    for i in range(k):
        x = random.uniform(low, high)
        while x in seen:
            x = random.uniform(low, high)
        seen.add(x)
        result.append(x)
    return result

nums = list(sample_floats(0, 100, k=10))
print(', '.join('{:0.2f}'.format(i) for i in nums))

# пока не приступил к заданию