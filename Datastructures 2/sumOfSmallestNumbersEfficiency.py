import random
import heapq
import time
random_list = [random.randint(1,10**9) for _ in range(0,10**7)]

#Test with list
time1_s = time.time()

list1 = sorted(random_list)
length_of_loop= int(len(random_list) / 10)
list_el_sum = 0
for i in range(length_of_loop):
    list_el_sum += list1[i]

time1_e = time.time()
print(list_el_sum)
print("Time list:", time1_e-time1_s)

#Test with heap
time2_s = time.time()
list2 = []
for i in range(len(random_list)):
    heapq.heappush(list2, random_list[i])
list2_el_sum = sum(list2[0:int(len(list2)/10)])

time2_e = time.time()
print(list_el_sum)
print("Time heap:", time2_e-time2_s)


# Heapified
time3_s = time.time()

heapq.heapify(random_list)# O(n)
fully_sorted_list = heapq.nsmallest(int(len(random_list)/10),random_list)
list3_el_sum = sum(fully_sorted_list[0:int(len(random_list)/10)])

time3_e = time.time()
print(list3_el_sum)
print("Heapified", time3_e-time3_s)