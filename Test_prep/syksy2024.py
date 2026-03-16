#Tehtava 1
def create_list(n):
    list = []
    for i in range(1,n+1):
        list.extend([i]*i)
    return list

# Tehtava 2
# Tehtava 3
def count_pairs(numbers):
    # even and odd counts
    evenCount = oddCount = 0
    result = 0
    for n in numbers:
        if n%2 == 0:
            evenCount+=1
        else:
            oddCount+=1
    # Tringular numbers represent amount of uniuew !pairs! from n elements.
    # (but we don't need elements paired with themselves)
    result += (oddCount*(oddCount+1))//2 - oddCount
    result += (evenCount*(evenCount+1))//2 - evenCount
    return result

print(count_pairs([1,2,1,4])) #2

print(count_pairs([1,2,1,1,4])) #4

# the given solution is impler: we 'track' addition for triangular numbers
# and add the lenght of the count to the result, starting with 0.
