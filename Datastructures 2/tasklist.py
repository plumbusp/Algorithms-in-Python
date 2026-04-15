# Task: Maintain a task list where each task has a name and an integer priority.
#       You can fetch and remove the task with the highest priority. If multiple tasks
#       share the highest priority, return the one that comes first alphabetically.
#       Both add_task and fetch_task should work efficiently with large amounts of tasks.

# Solution: heapq gives us an efficient min-heap; since heapq is a min-heap by default,
#           priority is stored as negative to simulate max-heap behavior; tuples (-priority, name)
#           are pushed, so heapq naturally sorts by highest priority first, then alphabetically;
#           fetch_task pops the root of the heap and returns the task name.

import heapq
class Tasks:
    def __init__(self):
        self.heap = []

    def add_task(self, name, priority):
        heapq.heappush(self.heap, (-priority, name))

    def fetch_task(self):
        return  heapq.heappop(self.heap)[1]

if __name__ == "__main__":
    tasks = Tasks()

    tasks.add_task("siivous", 20)
    tasks.add_task("koodaus", 90)
    tasks.add_task("treffit", 80)

    print(tasks.fetch_task()) # koodaus

    tasks.add_task("nukkuminen", 20)

    print(tasks.fetch_task()) # treffit
    print(tasks.fetch_task()) # nukkuminen