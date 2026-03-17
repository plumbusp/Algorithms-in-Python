# Task: The task is to form all the words that can be made from the letters 
#       of the given word and that do not contain two consecutive identical letters.
#       Here, a "word" refers to any combination of letters and does not have to be, for example, 
#       a word in the English language. For example, if the word is "kala," 
#       the desired words are "akal," "akla," "alak," "alka," "kala," and "laka."

# Soltution: itertools creates all possible permutations; valid_order function checks, if permutation tuple
#           is valid (has no consecutive identical letters), returns bool; if permutation tuple is valid,
#           and not in seen, we add it to the 'words' list; 'return words'

import itertools
def create_words(word):
    seen = set()
    words = []
    tuples = itertools.permutations(word, len(word))

    for tuple in tuples: 
        joinedTuple = "".join(tuple)
        if valid_order(joinedTuple):
            if joinedTuple in seen:
                continue
            seen.add(joinedTuple)
            words.append(joinedTuple)
    return sorted(words)

def valid_order(order):
    for i in range(1, len(order)):
        if order[i-1] == order[i]:
            return False
    return True

if __name__ == "__main__":
    print(create_words("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(create_words("aab")) # ['aba']
    print(create_words("aaab")) # []

    print(create_words("kala"))
    # ['akal', 'akla', 'alak', 'alka', 'kala', 'laka']

    print(create_words("syksy"))
    # ['ksysy', 'kysys', 'skysy', 'syksy', 'sykys', 'sysky', 
    #  'sysyk', 'yksys', 'ysksy', 'yskys', 'ysyks', 'ysysk']

    # print(len(create_words("aybabtu"))) # 660
    # print(len(create_words("abcdefgh"))) # 40320