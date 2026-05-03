# Tehtäväsi on laskea, monellako tavalla merkeistä a–z 
#   voidaan muodostaa n merkin pituinen merkkijono,
#   jossa kaikki vierekkäiset merkit ovat myös vierekkäin aakkosissa.
def count_strings(n):
    base_case = [1]*26
    for _ in range(n-1):
        current_case = [0]*26 # if we don't 0 it, we will end up adding new n counts on the n-1 counts
        for char in range(0,26):
            if char == 0:
                current_case[0]+= base_case[1]
            elif char == 25:
                current_case[25]+= base_case[24]
            else:
                current_case[char]+= base_case[char-1] + base_case[char+1]
        base_case = current_case.copy()
    return sum(base_case)

if __name__ == "__main__":
    print(count_strings(1)) # 26
    print(count_strings(2)) # 50
    print(count_strings(3)) # 98
    print(count_strings(4)) # 192

    print(count_strings(42)) # 36766943673096
    print(count_strings(100)) # 7073450400109633000218032957656