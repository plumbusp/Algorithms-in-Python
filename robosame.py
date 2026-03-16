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

def create_rules(): #logic: go through bit sequence each time and look for match
    rules = [] #LX01001R
    rules.append(("L", 1, "L", 2, "RIGHT"))
    rules.append(("0", 2, "X", 9, "RIGHT"))
    rules.append(("1", 2, "X", 10, "RIGHT"))

    rules.append(("0", 9, "X", 3, "LEFT"))
    rules.append(("1", 10, "X", 4, "LEFT"))

    #checks
    rules.append(("0", 3, "X", 5, "LEFT"))
    rules.append(("1", 3, "1", 3, "REJECT"))
    rules.append(("1", 4, "X", 5, "LEFT"))
    rules.append(("0", 4, "0", 4, "REJECT"))
    #bounds
    rules.append(("R", 9, "R", 3, "LEFT"))
    rules.append(("R", 10, "R", 4, "LEFT"))

    #skips
    rules.append(("0", 9, "0", 9, "RIGHT"))
    rules.append(("1", 9, "1", 9, "RIGHT"))
    rules.append(("X", 9, "X", 9, "RIGHT"))
    rules.append(("0", 10, "0", 10, "RIGHT"))
    rules.append(("1", 10, "1", 10, "RIGHT"))
    rules.append(("X", 10, "X", 10, "RIGHT"))
    rules.append(("0", 5, "0", 5, "LEFT"))
    rules.append(("1", 5, "1", 5, "LEFT"))
    rules.append(("X", 5, "X", 5, "LEFT"))
    rules.append(("L", 5, "L", 2, "RIGHT"))
    return rules





if __name__ == "__main__":
    rules = create_rules()

    print(calculate("00", rules)) # True
    print(calculate("001001", rules)) # True
    print(calculate("10111011", rules)) # True
    print(calculate("01", rules)) # False
    print(calculate("00100", rules)) # False
    print(calculate("10111101", rules)) # False