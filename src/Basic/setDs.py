# Set Data Structure

def IsSumNosInList(lst, target):
    seen = set()

    for num in lst:
        num2 = target - num;

        if num2 in seen:
            return (True,num,num2);
        seen.add(num)
    
    return (False,0,0)

def removeDuplicates(lst):
    seen = set()
    for num in lst:
        if num in seen:
            continue;
        else:
            seen.add(num)
    return seen;
def main():
    lst = [3,4,8,9,10,7,12,3,2,7]
    ret = IsSumNosInList(lst,19)
    print(ret[0],ret[1],ret[2])
    unq = removeDuplicates(lst)
    print(unq)


if __name__ == "__main__":
    main()
