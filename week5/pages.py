#Task: shortly present a list of page numbers, return string 
def create_string(pages) -> str:
    pages = sorted(set(pages))
    result = []
    newStartPage = pages[0]
    previousPage = pages[0]

    for i in range(1, len(pages)):
        if pages[i] != previousPage + 1:
            if newStartPage == previousPage:
                result.append(str(newStartPage))
            else:
                result.append(f"{newStartPage}-{previousPage}")
            newStartPage = pages[i]
        previousPage = pages[i]

    if newStartPage == previousPage:
        result.append(str(newStartPage))
    else:
        result.append(f"{newStartPage}-{previousPage}")

    return ",".join(result)


if __name__ == "__main__":
    print(create_string([1])) # 1
    print(create_string([1, 2, 3])) # 1-3
    print(create_string([1, 1, 1])) # 1
    print(create_string([1, 2, 1, 2])) # 1-2
    print(create_string([1, 6, 2, 5])) # 1-2,5-6
    print(create_string([1, 3, 5, 7])) # 1,3,5,7
    print(create_string([1, 8, 2, 7, 3, 6, 4, 5])) # 1-8
    print(create_string([3, 2, 9, 4, 3, 6, 9, 8])) # 2-4,6,8-9

    pages = [3, 2, 1, 3, 2, 1]
    print(create_string(pages)) # 1-3
    print(pages) # [3, 2, 1, 3, 2, 1]