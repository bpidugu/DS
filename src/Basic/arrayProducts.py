# function to return product of every other numbers in the input array
# input => [5,1,4,2]
# output => [8,40,10,20]



def arrayOfProducts(array):

    products = [1 for _ in range(len(array))]

    leftProduct =1
    for i in range(len(array)):
        products[i] = leftProduct
        leftProduct *= array[i]
    
    rightProduct =1
    for i in reversed(range(len(array))):
        products[i] *= rightProduct
        rightProduct *= array[i]

    return products

def main():
     arr = [5, 1, 4, 2]
     print(arrayOfProducts(arr))


if __name__ == "__main__":
    main()

