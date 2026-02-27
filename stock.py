# Taks: Given the price of a single stock over n days, compute for each day
#       the maximum profit achievable by selling the stock on that day.
#       (The stock may be bought on the same day or any earlier day)
# Solution: The algorithm runs in O(n) time by tracking the minimum stock value
#           and calculating available profit based on current stock and min stock value difference.
def find_profits(prices):
    minPrice = -1
    profits = []
    for p in prices:
        if minPrice < 0:
            minPrice = p
        if p < minPrice:
            minPrice = p
        profits.append(p - minPrice if p > minPrice else 0)
    return profits
        

if __name__ == "__main__":
    print(find_profits([1, 2, 3, 4])) # [0, 1, 2, 3]
    print(find_profits([4, 3, 2, 1])) # [0, 0, 0, 0]
    print(find_profits([1, 1, 1, 1])) # [0, 0, 0, 0]
    print(find_profits([2, 4, 1, 3])) # [0, 2, 0, 2]
    print(find_profits([1, 1, 5, 1])) # [0, 0, 4, 0]
    print(find_profits([3, 2, 3, 5, 1, 4])) # [0, 0, 1, 3, 0, 3]

    prices = list(range(1, 10**5+1))
    print(find_profits(prices)[:5]) # [0, 1, 2, 3, 4]