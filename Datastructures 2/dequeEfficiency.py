import collections
import time

deq = collections.deque()

start_time_append = time.time()
for i in range(10**5 + 1):
    deq.appendleft(i)
end_time_append = time.time()

print(f"Apend time {end_time_append-start_time_append}")

start_time_pop = time.time()
for i in range(len(deq)):
    deq.popleft()
end_time_pop = time.time()

print(f"Pop time {end_time_pop-start_time_pop}")

# Times:
# Apend time 0.011150836944580078
# Pop time 0.008955717086791992

# Alternative for list
# Apend time 0.010902881622314453
# Pop time 0.9773049354553223