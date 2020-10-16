'''
    HEAP SORT
'''

def heapify(arr,n,i):
    largest = i
    leftChild = 2*i+1
    rightChild = 2*i+2
    if leftChild < n and arr[leftChild] > arr[largest]:
        largest = leftChild
    
    if rightChild < n and arr[rightChild] > arr[largest]:
        largest = rightChild
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)

# def heapify(arr,upto,index):
    
# 		while index <= upto:
		
# 			leftchild = index*2+1
# 			rightchild = index*2+2
				
# 			if leftchild < upto:
# 				childToSwap = None
				
# 				if rightchild > upto:
# 					childToSwap = leftchild
# 				else:
# 					if arr[leftchild] < arr[rightchild]:
# 						childToSwap = leftchild
# 					else:
# 						childToSwap = rightchild
				
# 				if arr[index] > arr[childToSwap]:
# 					arr[index],arr[childToSwap] = arr[childToSwap],arr[index]
# 				else:
# 					break
					
# 				index = childToSwap
# 			else:
# 				break
# def heapify1(arr,n,index):
#     parentIndex = (index-1)//2
		
#     while parentIndex >= 0 and arr[parentIndex] > arr[index]:

#         arr[index],arr[parentIndex] = arr[parentIndex],arr[index]
#         parentIndex = (parentIndex-1)//2
# def heapifyTopToBottom(i):
	

def heapSort(arr,n):
    for i in range(n,-1,-1):
        heapify(arr,n,i)
    print(arr)
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)

n = int(input("Enter the number of elements to be sorted: \n"))
arr = list(map(int,input("Enter the elements: \n").strip().split()))
heapSort(arr,n)
print(arr)

# for i in range(n):
#     print(arr.pop(0),end=" ")
#     heapify(arr,n-i-1,0)