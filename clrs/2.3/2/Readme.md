### 2.3-2

Rewrite the MERGE procedure so that it does not use sentinels, instead stopping once either array L or R has had all its elements copied back to A and then copying the remainder of the other array back into A.
```
MERGE(A,p,q,r)
	n1 = q - p + 1
	n2 = r - q
	let L[1..n1 + 1] and R[1..n2 + 1] be new arrays
	for i = 1 to n1
		L[i] = A[p + i - 1]
	for j = 1 to n2
		R[j] = A[q + j]
	i = 1
	j = 1 
        k = 1	
	while i < n1 and j < n2
		if L[i] <= R[j]
			A[k] = L[i]
			i = i + 1

		else A[k] = R[j]
			j = j + 1
		k = k + 1

	if i == n1
		for j to n2
			A[k] = R[j]
			k = k + 1

	if j == n2
		for i to n1
			A[k] = R[i]
			k = k + 1
```
