import collections
def find_boxes(boxes, products):
    result_unsort = []
    sort_box_deque = collections.deque(sorted(boxes))
    
    product_index = []
    for i in range(len(products)): # O(n)
        product_index.append((products[i],i))
    product_index.sort()

    for p in product_index: # O(n)
        if len(sort_box_deque) != 0:
            while True:
                first_box = sort_box_deque.popleft()
                if first_box >= p[0]:
                    result_unsort.append((p[1], first_box))
                    break
                elif len(sort_box_deque) == 0:
                    result_unsort.append((p[1], -1))
                    break
                else:
                    continue
        else:
            result_unsort.append((p[1],-1))

    # currently the result is not in correct index order
    # fixing that:
    result = [el[1] for el in sorted(result_unsort)]

    return result

        

    

if __name__ == "__main__":
    print(find_boxes([4, 4, 6, 8], [5, 5, 4, 6, 1]))
    # [6, 8, 4, -1, 4]

    print(find_boxes([1, 2, 3, 4], [1, 1, 1, 1, 1]))
    # [1, 2, 3, 4, -1]

    print(find_boxes([2, 2, 2, 2], [1, 1, 1, 1, 1, 1]))
    # [2, 2, 2, 2, -1, -1]

    print(find_boxes([1, 1, 1, 1], [2, 2]))
    # [-1, -1]

    print(find_boxes([9, 6], [7, 5, 1, 6, 10, 2, 8]))
    # [9, 6, -1, -1, -1, -1, -1]

    boxes = []
    products = []
    for i in range(10**5):
        boxes.append(i % 100 + 1)
        products.append(3 * i % 97 + 1)
    result = find_boxes(boxes, products)
    print(result[42]) # 30
    print(result[1337]) # 35
    print(result[-1]) # 100