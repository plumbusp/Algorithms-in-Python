def can_create(coins, target): # coins = [2,4,6]
    result = {}
    result[0] = True
    for i in range(1, target+1):
        result[i] = False
        for j in coins:
            if i-j >= 0 and result[i-j]:
                result[i] = True
    
    return result[target]


if __name__ == "__main__":
    print(can_create([1, 2, 5], 13)) # True
    print(can_create([2, 4, 6], 13)) # False
    print(can_create([1], 42)) # True
    print(can_create([2, 4, 6], 42)) # True
    print(can_create([3], 1337)) # False
    print(can_create([3, 4], 1337)) # True