import time
import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None
        self.max_depth = -1

    def add(self, value):
        depth = 0
        if not self.root:
            self.root = Node(value)
            self.max_depth = max(depth, self.max_depth)
            return

        node = self.root
        while True:
            if node.value == value:
                return
            if node.value > value:
                depth += 1
                self.max_depth = max(depth, self.max_depth)
                if not node.left:
                    node.left = Node(value)
                    return
                node = node.left
            else:
                depth += 1
                self.max_depth = max(depth, self.max_depth)
                if not node.right:
                    node.right = Node(value)
                    return
                node = node.right

    def height(self):
        return self.max_depth

#### test ####
start_time_1 = time.time()
bst1 = TreeSet()
for i in range(1000):
    bst1.add(i)
stop_time_1= time.time()
print(f"Binary tree 1 time: {stop_time_1-start_time_1}")

test_list = []
for _ in range(1000):
    test_list.append(random.randint(1,1000))

start_time_2= time.time()
bst2 = TreeSet()
for i in test_list:
    bst2.add(i)
stop_time_2= time.time()
print(f"Binary tree 2 time: {stop_time_2-start_time_2}")