import time
import random
def count_rounds_dict(numbers):
    n = len(numbers)

    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i

    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1

    return rounds

def count_rounds(numbers):
    n = len(numbers)
    pos = [0] * (n+1)

    for i in range(n):
        pos[numbers[i]] = i

    rounds = 1
    for number in range(2, n+1):
        if pos[number] < pos[number - 1]:
            rounds += 1

    return rounds

listt = list(range(1, 10**7 + 1))
random.shuffle(listt)

start_time = time.time()
count_rounds(listt)
stop_time = time.time()

start_time_dic = time.time()
count_rounds_dict(listt)
stop_time_dic = time.time()

print(stop_time-start_time, "list")
print(stop_time_dic- start_time_dic, "dict")