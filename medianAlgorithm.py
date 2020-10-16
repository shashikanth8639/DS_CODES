import random

def pivot(arr, k):
	n = len(arr)
	r = random.randrange(0, n)
	pivot = arr[r]
	arr[n-1], arr[r] = arr[r], arr[n-1]
	i = -1
	j = 0

	while(j < n-1):
		if arr[j] < pivot:
			i += 1
			if  i!=j: arr[i], arr[j] = arr[j], arr[i]
		j += 1
	arr[i+1],arr[n-1] = arr[n-1], arr[i+1]

	return i+1


def median(arr, k):
	n = len(arr)
	if n == 1:
		return arr[0]
	v = pivot(arr, k)
	if v == k:
		return arr[k]
	else:
		if v < k:
			return median(arr[v:], k-v)
		else:
			return median(arr[:v], k)

arr = list(map(int, input().split()))
print(median(arr, 2	))