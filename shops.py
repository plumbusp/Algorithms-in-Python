#Task: the lists of bits is given; 0 means a house, 1 means a shop
#      what is the distance from each building to the closest shop? (shop has a distance 0 from itself)
#      return list with distances
#      O(n) efficiency

def find_distances(street):
    shopIndexesList = [] # list of indexes with shops
    for i in range(0, len(street)):
        if street[i] == "1":
            shopIndexesList.append(i)
    shopIndexesList.reverse()

    distances = []
    nextShop = shopIndexesList.pop()
    if len(shopIndexesList) > 1:
        nextNextShop = shopIndexesList.pop()
    else:
        nextNextShop = nextShop

    for i in range(0, len(street)):
        if i == nextNextShop: # if we reached the second shop, we update the range of distance calculations
            nextShop = nextNextShop 
            if shopIndexesList:
                nextNextShop = shopIndexesList.pop()
        
        shortestDistance = min(abs((nextShop+1)-(i+1)), abs((nextNextShop+1)-(i+1)))
        distances.append(shortestDistance)
    return distances

        

if __name__ == "__main__":
    print(find_distances("00100010")) # [2, 1, 0, 1, 2, 1, 0, 1]
    print(find_distances("00100000")) # [2, 1, 0, 1, 2, 3, 4, 5]
    print(find_distances("11111111")) # [0, 0, 0, 0, 0, 0, 0, 0]
    print(find_distances("01010101")) # [1, 0, 1, 0, 1, 0, 1, 0]
    print(find_distances("10000000")) # [0, 1, 2, 3, 4, 5, 6, 7]
    print(find_distances("00000001")) # [7, 6, 5, 4, 3, 2, 1, 0]

    n = 10**5
    street = "0"*n + "1" + "0"*n
    distances = find_distances(street)
    print(distances[1337]) # 98663