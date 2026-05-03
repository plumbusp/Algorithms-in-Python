# Task: find best amount of way to get a number 
#   x by making 2 types of operations
#   Operations are add number 3 and multiply by 2
# Solution: I use bottom up, store min amount of actions to achive x,
#   store in result dict
# In the beginning number is 1
import math
def min_steps(x:int):
    result = {} # stores min steps to achive each value
    result[1] = 0
    for i in range(2, x+1):
        result[i] = 4000
        if i - 3 > 0: #just calculates that the i-3 can be done
            result[i] = min(result[i-3]+ 1, result[i])
        if i % 2 == 0: # must be even cause we multiply by 2 originally
            result[i] = min(result[int(i/2)] + 1, result[i])

    if result[x] != 4000:
        return result[x]
    else:
        return -1
    

if __name__ == "__main__":
    print(min_steps(1)) # 0
    print(min_steps(2)) # 1
    print(min_steps(3)) # -1
    print(min_steps(4)) # 1
    print(min_steps(5)) # 2
    print(min_steps(17)) # 4
    print(min_steps(42)) # -1
    print(min_steps(100)) # 7
    print(min_steps(1000)) # 13