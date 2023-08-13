# Linear search in unsorted array
def linear_search1(A:list, key:int, n:int) -> int:
    i = 0 # start index of the array 

    while i <= n-1 and key != A[i]:
        i += 1
    
    if i > n - 1:
        return -1 
    else:
        return i 

# Linear search in sorted array
def linear_search2(A:list, key: int, n: int) -> int:
    i = 0 # start index of the array 

    while i <= n-1 and key < A[i] :
        i += 1 

    if A[i-1] == key:
        return i 
    else:
        return -1 

def main():
    A = [20,35,18,8,14,4,3,39]
    key = -1 
    n = len(A)
    res1 = linear_search1(A,key,n)
    res2 = linear_search2(sorted(A), key, n)
    print(f"Linear search in unsorted array: {res1}")
    print(f"Linear search in sorted array: {res2}")

if __name__ == "__main__":
    main()

# Time Complexity
# Worst Case: O(n)
