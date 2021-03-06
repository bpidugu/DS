# List Data Structure


def reverseList(list):
    start,end = 0, len(list)-1
    while start < end:
        list[start], list[end] = list[end], list[start]
        start +=1
        end -=1
 
def reverseCharacters(charArr):
    start, end = 0, len(charArr) -1
    while start < end:
        charArr[start],charArr[end] = charArr[end], charArr[start]
        start +=1
        end -=1



if __name__ == "__main__":
    l1 = ["This","is","my","story"]
    l2 = ["This","is","my","great","story"]
    reverseList(l1)
    reverseList(l2)
    print (l1)
    print (l2)

    c1 = ['n','i','m','a','j','n','e','b']
    reverseCharacters(c1)
    print(c1)