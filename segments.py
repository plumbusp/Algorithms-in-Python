from collections import defaultdict
def find_segments(data):
    previousLetter = ""
    segments = None
    for i in data:
        if not segments:
            segments = []
            segments.append((1,i))
        elif segments[-1][1] == i:
            segments[-1] = (segments[-1][0]+1, i)
        else:
            segments.append((1,i))
    return segments

        

if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]