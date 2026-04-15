import heapq
def find_smallest(steps):
    my_heap = []
    heapq.heappush(my_heap, 1)
    my_heap_set = set()
    my_heap_set.add(1)
    lastSmallestValue = 1

    for s in range(0, steps):
        lastSmallestValue = heapq.heappop(my_heap) # remove last smallest value
        my_heap_set.remove(lastSmallestValue)

        firstAdd = 2*lastSmallestValue
        if firstAdd not in my_heap_set:
            heapq.heappush(my_heap, firstAdd)
            my_heap_set.add(firstAdd)

        secondAdd = 3*lastSmallestValue
        if secondAdd not in my_heap_set:
            heapq.heappush(my_heap, secondAdd)
            my_heap_set.add(secondAdd)

    return heapq.heappop(my_heap)
       
        



if __name__ == "__main__":
    print(find_smallest(0)) # 1
    print(find_smallest(1)) # 2
    print(find_smallest(2)) # 3
    print(find_smallest(3)) # 4
    print(find_smallest(4)) # 6
    print(find_smallest(5)) # 8

    print(find_smallest(42)) # 1296
    print(find_smallest(1337)) # 16210220612075905068
    print(find_smallest(123123)) # 47241633171870338440585357243035120029747450090811731814934867117962334088709324512562801224664331563355142646399182644605958987116029586018592281978123083613432358051028210559768563023872