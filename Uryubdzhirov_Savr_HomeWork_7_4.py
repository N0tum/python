import os

dir_path = os.path.dirname(__file__)
data_path = os.path.join(dir_path, 'some_data')
result = {0: 0, 10: 0, 100: 0, 1000: 0, 10000: 0, 100000: 0, 1000000: 0}
keys = [0, 10, 100, 1000, 10000, 100000, 1000000]

for root, dirs, files in os.walk(data_path):
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        if size == 0:
            result[0] += 1
            continue
        for value, key in enumerate(keys):
            if key < size <= keys[value + 1]:
                result[keys[value + 1]] += 1
                break

print(result)
