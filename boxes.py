# Calculates the minimum number of boxes needed to hold all products, rounding up when products don’t fit evenly.
import math
def min_count(product_count:int, box_size:int) -> int:
    return math.ceil(product_count/box_size)

if __name__ == "__main__":
    print(min_count(10, 3)) # 4
    print(min_count(10, 4)) # 3
    print(min_count(100, 1)) # 100
    print(min_count(100, 100)) # 1
    print(min_count(100, 99)) # 2
    print(min_count(5, 5)) # 1
    print(min_count(5, 6)) # 1