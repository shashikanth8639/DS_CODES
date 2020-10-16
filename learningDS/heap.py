class Heap:
	
	def __init__(self):
		self.heap = []
		self.size = 0
	
	def insert(self,data):
		self.heap.append(data)
		self.size += 1
		self.fixUp(self.size-1)
		
	def fixUp(self,index):
		
		parentIndex = (index-1)//2
		
		while parentIndex >= 0 and self.heap[parentIndex] > self.heap[index]:

			self.heap[index],self.heap[parentIndex] = self.heap[parentIndex],self.heap[index]
			parentIndex = (parentIndex-1)//2
			# parentIndex = (index-1)//2
		
	def heapsort(self):
		
		for i in range(self.size):
			print(self.heap[0])
			self.heap[0],self.heap[self.size-i-1] = self.heap[self.size-i-1],self.heap[0]
			self.fixDown(0,self.size-i-2)
			
	def fixDown(self,index,upto):
	
		while index <= upto:
		
			leftchild = index*2+1
			rightchild = index*2+2
				
			if leftchild < upto:
				childToSwap = None
				
				if rightchild > upto:
					childToSwap = leftchild
				else:
					if self.heap[leftchild] < self.heap[rightchild]:
						childToSwap = leftchild
					else:
						childToSwap = rightchild
				
				if self.heap[index] > self.heap[childToSwap]:
					self.heap[index],self.heap[childToSwap] = self.heap[childToSwap],self.heap[index]
				else:
					break
					
				index = childToSwap
			else:
				break
	
	def delete(self,data):
		
		for i in range(self.size):
			if self.heap[i] == data:
				self.heap[i] = self.heap[self.size-1]
				parent = self.heap[(i-1)//2]
				del self.heap[self.size-1]
				self.size -= 1
				if i == 0 or (i-1)//2 >0 and self.heap[i] > self.heap[(i-1)//2]:
					self.fixDown(i,self.size-1)
				else:
					self.fixUp(self.size-1)
				break
		else:
			print("DATA NOT FOUND")
	
	
	def display(self):
		print(self.heap)
	
	def isEmpty(self):
		return self.size == 0

hp = Heap()
hp.insert(45)
hp.insert(-2)
hp.insert(4)
hp.insert(23)
hp.insert(56)
hp.insert(32)

hp.display()

hp.delete(-2)
hp.delete(4)
hp.delete(23)
hp.delete(32)
hp.delete(45)
hp.delete(56)
hp.display()
hp.heapsort()
hp.display()

