# Task: find out if lists overlap
import random


def check_overlapping(reservations):
    sortedReservations = sorted(reservations)
    start=0
    finish=0
  
    for tuple in sortedReservations:
        if start <= tuple[0] <= finish:
            return True
        start = tuple[0]
        finish = tuple[1] # thanks to sorted we know for sure that next element cannot be earlier in the line
    return False

    # covered = set()
    # hasOverlaps = False
    # def checkForOverlap(entry:tuple) -> tuple:
    #     nonlocal hasOverlaps
    #     newCoverage = range(entry[0], entry[1]+1)
    #     for i in newCoverage:
    #         if i in covered:
    #             hasOverlaps = True
    #     covered.update(set(newCoverage))
                
    #     return entry
    # sortedReservations =sorted(reservations, key=checkForOverlap)
    # return hasOverlaps

if __name__ == "__main__":
    print(check_overlapping([])) # False
    print(check_overlapping([(1, 3)])) # False
    print(check_overlapping([(4, 7), (1, 2)])) # False
    print(check_overlapping([(4, 7), (1, 5)])) # True
    print(check_overlapping([(1, 1), (2, 2)])) # False
    print(check_overlapping([(1, 1), (1, 1)])) # True
    print(check_overlapping([(2, 3), (5, 5), (3, 4)])) # True
    print(check_overlapping([(2, 3), (5, 5), (1, 4)])) # True
    print(check_overlapping([(2, 3), (5, 5), (1, 5)])) # True

    reservations = [(day, day) for day in range(1, 10**5+1)]
    random.shuffle(reservations)
    print(check_overlapping(reservations)) # False

    reservations.append((42, 1337))
    random.shuffle(reservations)
    print(check_overlapping(reservations)) # True