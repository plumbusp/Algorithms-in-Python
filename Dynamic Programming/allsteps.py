# Working as in machine.py (bottom-up), but now in reusult
#   we store amount of ways on each index i 
def count_steps(x):
    result = {} # stores amount of ways to achive each value
    result[1] = 1
    for i in range(2, x+1):
        result[i] = 0
        if i - 3 > 0: #just calculates that the i-3 can be done
            result[i] += result[i-3]
        if i % 2 == 0: # must be even cause we multiply by 2 originally
            result[i] += result[i/2]

    return result[x]

if __name__ == "__main__":
    print(count_steps(1)) # 1
    print(count_steps(2)) # 1
    print(count_steps(3)) # 0
    print(count_steps(4)) # 2
    print(count_steps(5)) # 1
    print(count_steps(17)) # 5
    print(count_steps(42)) # 0
    print(count_steps(100)) # 242
    print(count_steps(1000)) # 2948311