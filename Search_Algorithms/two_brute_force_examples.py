# Task is to count, how many mathematically valid combinations of "(" and ")" can be formed 
import itertools

def valid_sequence(sequence):
    depth = 0
    for bracket in sequence:
        if bracket == "(":
            depth += 1
        if bracket == ")":
            depth -= 1
        if depth < 0:
            return False
    return depth == 0

# Slow solution creates cartesian product strings of "()", even though we never needed those stings for logic
def count_sequences_slow(n):
    count = 0
    for sequence in itertools.product("()", repeat=n):
        if valid_sequence(sequence):
            count += 1
    return count

# Faster solution is recursive. 'n' follows how many "(" or ")" is still needed to add. 'd' is depth-
#   'd' can grow (another "(") or decrease (another ")").
#    If depth is lower than 0 => current sequence is not valid 
#    If depth is heigher than n is the opposite boundary> means we don\t have a chance
#    to close all our braces => not valid

def count_sequences(n, d=0):
    if d < 0 or d > n:
        return 0
    if n == 0:
        return 1
    return count_sequences(n - 1, d + 1) + count_sequences(n - 1, d - 1)


