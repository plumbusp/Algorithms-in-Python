# Task: count how many distinct substrings exist in a given string
# Solution: I looped over every possible starting index in the string,
#           from each start, I extend the substring character by character to the right
#           I add each formed substring into a set, which automatically removes duplicates
#           finally, I return the size of the set as the answer
# Time complexity: O(n^2) (substring generation, with n < 20 so this is efficient)

def count_substrings(string):
    substrings = set()
    for i in range(0,len(string)):
        lastingSubstring=""
        for j in range(i, len(string)):
            lastingSubstring += string[j]
            substrings.add(lastingSubstring)
    return len(substrings)

if __name__ == "__main__":
    print(count_substrings("aaaa")) # 4
    print(count_substrings("abab")) # 7
    print(count_substrings("abcd")) # 10
    print(count_substrings("abbbbbb")) # 13
    print(count_substrings("aybabtu")) # 26
    print(count_substrings("saippuakauppias")) # 110