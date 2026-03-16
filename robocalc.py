# Task: make a Turing machine
def calculate(input, rules):
    string = list("L"+ input +"R")
    pos = 0
    state = 1
    action= 0
    maxSteps = 1000
    steps = 0

    def findNeededRule(symbol, state):
        newSymbol = -1
        newState = 0
        newAction = 0
        for rule in rules:
            if rule[0] == symbol and rule[1] == state:
                newSymbol = rule[2]
                newState = rule[3]
                newAction = rule[4]
        return newSymbol, newState, newAction
    
    while steps < maxSteps:
        steps += 1
        symbol, state, action = findNeededRule(string[pos], state)
        if symbol == -1:
            return False
        
        string[pos] = symbol
        if action == "LEFT":
            pos -= 1
            if pos < 0:
                return False
        elif action == "RIGHT":
            pos += 1
            if pos >= len(string):
                return False
        elif action == "ACCEPT":
            return True
        elif action == "REJECT":
            return False
    return False


if __name__ == "__main__":
    rules = []

    rules.append(("L", 1, "L", 2, "RIGHT"))
    rules.append(("L", 3, "L", 2, "RIGHT"))

    rules.append(("0", 2, "X", 4, "RIGHT"))
    rules.append(("1", 4, "X", 5, "RIGHT"))
    rules.append(("1", 2, "X", 6, "RIGHT"))
    rules.append(("0", 6, "X", 7, "RIGHT"))

    rules.append(("0", 4, "0", 4, "RIGHT"))
    rules.append(("0", 5, "0", 5, "RIGHT"))
    rules.append(("0", 7, "0", 7, "RIGHT"))
    rules.append(("1", 6, "1", 6, "RIGHT"))
    rules.append(("1", 5, "1", 5, "RIGHT"))
    rules.append(("1", 7, "1", 7, "RIGHT"))

    rules.append(("X", 2, "X", 2, "RIGHT"))
    rules.append(("X", 4, "X", 4, "RIGHT"))
    rules.append(("X", 5, "X", 5, "RIGHT"))
    rules.append(("X", 6, "X", 6, "RIGHT"))
    rules.append(("X", 7, "X", 7, "RIGHT"))

    rules.append(("R", 2, "R", 2, "ACCEPT"))
    rules.append(("R", 4, "R", 4, "REJECT"))
    rules.append(("R", 6, "R", 6, "REJECT"))

    rules.append(("R", 5, "R", 3, "LEFT"))
    rules.append(("R", 7, "R", 3, "LEFT"))
    rules.append(("0", 3, "0", 3, "LEFT"))
    rules.append(("1", 3, "1", 3, "LEFT"))
    rules.append(("X", 3, "X", 3, "LEFT"))

    print(calculate("0", rules)) # False
    print(calculate("00", rules)) # False
    print(calculate("01", rules)) # True
    print(calculate("0110", rules)) # True
    print(calculate("0101", rules)) # True
    print(calculate("1000", rules)) # False
    print(calculate("00110101", rules)) # True
    print(calculate("00111101", rules)) # False