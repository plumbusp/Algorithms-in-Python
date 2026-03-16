# Insertion sort is a O(n^2) sorting alogorithm.
#  It loops though list, and shifts current number to left as much,
#  as needed for the left side to be fully sorted.

#helper function
def swap(list:list, a,b):
    temp = list[b]
    list[b] = list[a]
    list[a] = temp

def insertion_sort(items):
    for i in range(0,len(items)):
        for j in range(i-1, -1, -1):
