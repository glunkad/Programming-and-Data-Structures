def insertion_sort(A,n):
    i = 0 
    first = A[i]
    p = 0 
    
    for i in range(1,n):
        if A[i] < first:
            p = i 
            first = A[i] 
        A[p] = A[0]
        A[0] = first 

    for i in range(2,n):
        x = A[i]
        j = i 
        while x < A[j-1]:
            A[j] = A[j-1]
            j = j - 1 
        A[j] = x 

    return A 

def main():
    A = [3,18,35,8,14,41,20,39]
    n = len(A)
    print(A)
    sorted_A = insertion_sort(A,n) 
    print(sorted_A) 

if __name__ == "__main__":
    main()
