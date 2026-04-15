# Task: cretae a method that creates a sequence from 1 to n of size ´size´ and then perform some amount of steps.
#   In each step the two first elements of sequence are taken from the beginning and 
#   moved to the end in reversed  order

import collections
def find_first(size, steps):
    deq = collections.deque()
    for i in range(1, size+1):
        deq.append(i)

    for _ in range(steps):
        two_first = [deq.popleft(), deq.popleft()]
        first_el = two_first[0]
        two_first[0] = two_first[1]
        two_first[1] = first_el

        deq.extend(two_first)
    return deq[0]


if __name__ == "__main__":
    print(find_first(4, 3)) # 4
    print(find_first(12, 5)) # 11
    print(find_first(2, 1000)) # 1
    print(find_first(99, 555)) # 11
    print(find_first(12345, 10**6)) # 12295