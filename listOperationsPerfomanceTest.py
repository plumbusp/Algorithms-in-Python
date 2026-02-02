# Testing performance of list operations with O(1) complexity
import time
numbers = []

start_time = time.time()
for n in range(0, 10**5):
    numbers.append(n)
stop_time = time.time()

time_appending = stop_time-start_time

numbersTest1 = numbers[:]

start_time = time.time()
for n in range(0, 10**5):
    numbersTest1.pop(-1) 
stop_time = time.time()

time_removing = stop_time-start_time

print(f"Time taken to append: {time_appending}, Time taken to remove: {time_removing}")

# Testing performance of list operation with O(n) complexity

numbersTest2 = numbers[:]

start_time = time.time()
for n in range(0, 10**5):
    numbersTest2.pop(0) 
stop_time = time.time()

time_removing_first_element = stop_time-start_time

print(f"Time taken to remove all first elements: {time_removing_first_element}")
