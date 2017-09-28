### 2.2-2

Consider sorting n numbers stored in array A by first finding the smallest element of A and exchanging it with the element in A[1] . Then find the second smallest element of A, and exchange it with A[2] . Continue in this manner for the first n - 1 elements of A. Write pseudocode for this algorithm, which is known as selection sort. What loop invariant does this algorithm maintain? Why does it need to run for only the first n - 1 elements, rather than for all n elements? Give the best-case and worst-case running times of selection sort in θ-notation.

# pseudocode

# loop invariant

subarray A[1..i-1] has smallest elements in non-decreasing order. Where i is the number of iterations

# n - 1

If A[1..n-1] elements is sorted non-decreasing subarray, which loop invariant kinda proves, than n element is equal or greater than n-1. Since it's only one element left, it can't be compared to itself. 

# complexity

worst-case = θ(n^2) 
best-case = θ(n^2) # because of need to find minimal subarray value at each iteration.
