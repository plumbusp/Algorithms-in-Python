# Task: Count amount of sublists that start and end with same number, O(n)

# First attempt:
# Problems: not O(n), while is a nesting loop and in worth case -- repeats n times (O(n^2))
# Note: This is not a sliding window solution. I reset left each iteration, but
#   in sliding windown pointers can move only forward.
def count_lists_first_attempt(numbers):
    sublists =[]
    left = 0
    right = 0
    for i in range(0,len(numbers)):
        right = i
        left = 0
        while left <= right:
            if numbers[left] == numbers[right]:
                if left == right:
                    sublists.append([numbers[right]])
                    break
                sublists.append(numbers[left:right])
            left += 1
    return len(sublists)

# Second attempt: Reaised sliding window is not the right solution in here.
#   It works only if shrinking window can make it valid, and making it bigger never can,
#   In this example making window bigger lead to more valid sublists.
def count_lists_second_attempt(numbers):
    sublists =[]
    left = 0
    right = 0
    for i in range(0,len(numbers)):
        sublists.append([numbers[i]]) # substring with only a number itself
        right = i
        
        while left < right:
            if numbers[left] == numbers[right]:
                sublists.append(numbers[left:right])
                break
            left += 1
    return len(sublists)

# I need to count appearances. I can derive formula for it.
# appearances count (not including oneself): 1:0, 2:1, 3:3, 4:6, 5:10, so triangular numbers for (k-1).
#
# This works just fine.
def count_lists_third_attempt(numbers):
    appearance = {} # number: time appeared
    for n in numbers: 
        appearance[n]= appearance.get(n,0) + 1
    
    count = 0
    for number, appearedCount in appearance.items():
        count += appearedCount
        # triangular number
        count += int(((appearedCount-1)*(appearedCount))//2)
    return count

# Note how the previous code could be simplified by acumulate triangular 
# numbers each time we increase variable count
def count_lists_final_attempt(numbers):
    appearance = {} # number: time appeared
    result = 0
    for n in numbers:
        appearance[n]= appearance.get(n,0) + 1 # let's say we had 1 appearance before, so now 2
        # that means that amount of pairs by trangular numbers rule increased by:
        # 1 -- before, 1+2 -- three now
        result += 1
        result += appearance[n]
    
    return result


print(count_lists_third_attempt([1, 2, 1, 2, 1])) #9

print(count_lists_third_attempt([1, 2, 3])) #3