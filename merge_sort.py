def merge(A:list, tmpArray:list, leftPos:int, rightPos:int, rightEnd:int) -> list:
    leftEnd = rightPos - 1 
    tmpPos = leftPos # pos of sorted completed elements 
    numElement = rightEnd - leftPos + 1 # total number of elements 

    while (leftPos <= leftEnd) and (rightPos <= rightEnd) :
        if A[leftPos] <= A[rightPos]:
            tmpArray[tmpPos] = A[leftPos] 
            tmpPos += 1
            leftPos += 1 
        else:
            tmpArray[tmpPos] = A[rightPos] 
            tmpPos += 1 
            rightPos += 1

    while leftPos <= leftEnd:
        tmpArray[tmpPos] = A[leftPos] 
        tmpPos += 1 
        leftPos += 1 

    while rightPos <= rightEnd:
        tmpArray[tmpPos] = A[rightPos] 
        tmpPos += 1 
        rightPos += 1

    i = 1 
    while i <= numElement:
        A[rightEnd] = tmpArray[rightEnd]
        rightEnd -= 1 
        i += 1 

    return A 

def merge_sort(A:list, tmpArray:list, left:int, right:int) -> list:
    middle = 0 
    sorted_A = []

    if left < right:
        middle = (left + right) // 2
        merge_sort(A, tmpArray, left, middle)
        merge_sort(A, tmpArray, middle+1, right)
        sorted_A = merge(A, tmpArray, left, middle+1, right) 
    
    return sorted_A 


def main():
    A = [44,55,12,42,94,18,6,17]
    n = len(A) 
    tmpArray = [0]*n
    print(f"unsorted array: {A}")
    sorted_A = merge_sort(A,tmpArray,0,n-1)
    print(f"sorted array: {sorted_A}")

if __name__ == "__main__":
    main()
 
 # Time Complexity 
 # O(n**2)
