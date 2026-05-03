import re

class Oracle:
    def __init__(self, code):
        self.code = code
        self.counter = 0

    def check_code(self, code):
        self.counter += 1
        if self.counter > 16:
            raise RuntimeError("too many check_code calls")

        if type(code) != str or not re.match("^[1-9]{4}$", code) or len(code) != len(set(code)):
            raise RuntimeError("invalid code for check_code")

        in_place = in_code = 0
        for pos in range(4):
            if code[pos] in self.code:
                if code[pos] == self.code[pos]:
                    in_place += 1
                else:
                    in_code += 1

        return in_place, in_code


def get_string(numbers: list):
    return "".join(str(n) for n in numbers)


def find_code(oracle: Oracle):
    # Stage 1: search for numbers in the code
    numbers_in_code = []
    code_guess = [1,2,3,4]

    in_place, in_code = oracle.check_code(get_string(code_guess))

    for _ in range(0,5):
        code_guess = [n+1 for n in code_guess]
        in_place_now, in_code_now = oracle.check_code(get_string(code_guess))

        places_before = in_place+ in_code
        places_now = in_place_now + in_code_now

        if (places_before != places_now):
            if places_before > places_now:
                numbers_in_code.append(code_guess[0]-1)
            elif places_before < places_now:
                numbers_in_code.append(code_guess[-1])

        in_code = in_code_now
        in_place = in_place_now
        

    print(numbers_in_code)

    # Stage 2: find right places
    

if __name__ == "__main__":
    # # esimerkki oraakkelin toiminnasta
    # oracle = Oracle("4217")
    # print(oracle.check_code("1234")) # (1, 2)
    # print(oracle.check_code("3965")) # (0, 0)
    # print(oracle.check_code("4271")) # (2, 2)
    # print(oracle.check_code("4217")) # (4, 0)

    # # esimerkki funktion find_code toiminnasta
    oracle = Oracle("4217")
    code = find_code(oracle)
    print(code) # 4217