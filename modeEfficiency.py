import time
import random
def find_mode(numbers):
    count = {}
    mode = (0, 0)

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1

        mode = max(mode, (count[x], x))

    return mode[1]

def find_mode_2(numbers):
    mostRepeatedCount = 0
    currentCount = 0
    sortedNumbers = sorted(numbers)
    previousNumber = sortedNumbers[0]
    mostRepeated = sortedNumbers[0]

    for i in range(0,len(sortedNumbers)):
        if sortedNumbers[i] == previousNumber:
            currentCount += 1
        if sortedNumbers[i] != previousNumber or i + 1 == len(sortedNumbers):
            if mostRepeatedCount <= currentCount:
                mostRepeatedCount = currentCount
                mostRepeated = previousNumber
            currentCount = 1
                   
        previousNumber = sortedNumbers[i]
    return mostRepeated

print(find_mode([1,2,2,2,4,5,4,3,4,5,6,5,2,3,2,4,4,7,1]))
print(find_mode_2([1,2,2,2,4,5,4,3,4,5,6,5,2,3,2,4,4,7,1]))

listt = random.sample(range(1, 10**7 + 1), 10**7)

start_time = time.time()
find_mode(listt)
stop_time = time.time()

start_time_2 = time.time()
find_mode_2(listt)
stop_time_2 = time.time()

print(stop_time-start_time, "with dict")
print(stop_time_2- start_time_2, "with sort")
    