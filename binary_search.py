def binary_search(A: list, key: int, n: int) -> int:
    lower = 0  # start index 
    upper = n - 1  # end index 
    
    middle = 0 
    while lower < upper:
        
        middle = (lower + upper) // 2

        if(key > A[middle] ) :
            lower = middle + 1 
        else:
            upper = middle - 1 

    if lower > upper :
        return -1 
    else:
        return middle 

def main():
    A = [2,4,6,8,10,12,14,16]
    n = len(A) 
    key = 10 
    pos = binary_search(A, key, n)
    print(f"Location of {key} is {pos}") 

if __name__ == "__main__":
    main()

# Time Complexity 
# O(logn)
