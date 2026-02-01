import time
import random
# toteutus 1
def count_even1(numbers:list):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result
# toteutus 2
def count_even2(numbers:list):
    return sum(x % 2 == 0 for x in numbers)

random.seed(100)
numbers = [random.randint(1, 10**7) for i in range(10000)]
startTime1 = time.time()
count_even1(numbers)
stopTime1 = time.time()
print(f"count_even1: {round(stopTime1-startTime1, 6)}s")

startTime2 = time.time()
count_even2(numbers)
stopTime2 = time.time()
print(f"count_even2: {round(stopTime2-startTime2, 6)}s")