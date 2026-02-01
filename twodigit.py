# Counts how many integers within a given range can be formed using only the digits 2 and 5.

def count_numbers(a, b) -> int:
    cnt = 0
    def count(number)-> int:
        cn = 0
        if number > b:
            return 0
        elif number >= a:
            cn += 1
        cn+= count(number*10+5)
        cn += count(number*10+2)
        return cn
    cnt += count(2)
    cnt += count(5)
    return cnt

if __name__ == "__main__":
    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    print(count_numbers(585, 884))
    print(count_numbers(1, 10**9)) # 1022
    print(count_numbers(123456789, 987654321)) # 512