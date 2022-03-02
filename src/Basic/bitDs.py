# Bitwise Operators
# AND => & => Returns 1 if both are 1, else 0
def isOdd(num):
    r = num & 1
    return (r!=0)
def isEven(num):
    return ((num & 1) ==0)


if __name__ == "__main__":
    print(isOdd(32001))
    print(isOdd(7))
    print(isEven(4))
    print(isEven(7))