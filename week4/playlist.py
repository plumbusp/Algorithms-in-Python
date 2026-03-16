def count_parts(songs):
    left = 0 
    count = 0
    currentSublist = {}
    for index,song in enumerate(songs):
        currentSublist[song] = currentSublist.get(song, 0) + 1
        while currentSublist[song] > 1:
            currentSublist[songs[left]]-= 1
            left+= 1

        count += index-left+1

    return count



    # length = len(songs)
    # right = 0
    # left = 0
    # count = 0
    # currentSublist = set()
    # for index, song in enumerate(songs):
    #     currentSublist.add(song)
    #     count += 1
    #     right = index
    #     while right+1 < length:
    #         right+=1
    #         if songs[right] in currentSublist:
    #             currentSublist.clear()
    #             break
    #         count += 1
    # return count
        



    # length = len(songs)
    # seen = set()
    # count = 0
    # for i in range(0, length):
    #     seen.add(songs[i])
    #     currentIndex = 1
    #     while currentIndex < length-1:
    #         currentIndex += 1
    #         if songs[currentIndex] in seen:
    #             continue
    #         count += 1
    #         seen.add(songs[currentIndex])
    #     seen.remove(songs[i])
    # return(count) 


    # count = 0
    # for i in range(0,len(songs)):
    #     lastingSet = set()
    #     for j in range(i, len(songs)):
    #         if songs[j] in lastingSet:
    #             break
    #         lastingSet.add(songs[j])
    #         count += 1
    # return count

if __name__ == "__main__":
    print(count_parts([1, 1, 1, 1])) # 4
    print(count_parts([1, 2, 3, 4])) # 10
    print(count_parts([1, 2, 1, 2])) # 7
    print(count_parts([1, 2, 1, 3])) # 8
    print(count_parts([1, 1, 2, 1])) # 6

    songs = [1, 2] * 10**5
    print(count_parts(songs)) # 399999
    songs = list(range(1, 10**5 + 1)) * 2
    print(count_parts(songs)) # 15000050000