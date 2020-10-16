#Node data structure
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

#linkedlist class
class SinglyLinkedList:
	
	def __init__(self):
		self.head = None
		self.tail = None
	
	def insert(self,data,end=True):
	
		if self.head is None:
			self.head = self.tail = Node(data)
		else:
			newNode = Node(data)
			self.insertNode(newNode,end)
	
	def insertNode(self,node,end):
		if end:
			self.tail.next = node
			self.tail = node
		else:
			node.next = self.head
			self.head = node
	
	def delete(self,data=None):
		if self.head is None:
			print('Empty Linkedlist')
		else:
			self.deleteNode(data)
	
	def deleteNode(self,data):
		if data is None:
			data = self.tail.data
		
		if data == self.head.data:
			self.head = self.head.next
		else:
			tmp = self.head
			while tmp and tmp.next:
				if tmp.next.data == data:
					tmp.next = tmp.next.next
				tmp = tmp.next
			self.tail = tmp
	
	def search(self,data):
		if self.head is None:
			print('Empty Linkedlist')
		else:
			self.serachNode(data)
	
	def serachNode(self,data):
		tmp=self.head
		while tmp:
			if tmp.data == data:
				print('Value found')
				return
			tmp=tmp.next
	
	def display(self):
		if self.head is None:
			print('Empty Linkedlist')
		else:
			tmp=self.head
			while tmp.next:
				print(tmp.data,end='-->')
				tmp=tmp.next
			print(tmp.data)
	
	def deleteLL(self):
		self.head = self.tail = None

	def swap(self,data1,data2):
		tmp=self.head
		t1=t2=None
		while tmp.next:
			if tmp.next.data==data1:
				t1=tmp
			elif tmp.next.data == data2:
				t2=tmp
			if not t1 and not t2:
				break
			tmp=tmp.next
		c1=t1.next.next
		c2=t2.next.next
		t2.next=t1.next
		t1.next=t2.next
		t2.next=c2
		t1.next.next.next=t2.next
		t2.next=t1.next.next.next
			
sl=SinglyLinkedList()
sl.insert(45)
sl.insert(12,end=False)
sl.insert(62)
sl.display()
sl.delete()
sl.display()
sl.delete(12)
sl.display()
sl.delete(45)
sl.display()
sl.display()
sl.insert(45)
sl.insert(12,end=False)
sl.insert(62)
sl.search(62)
sl.search(45)
sl.display()
sl.insert(12,end=False)
sl.insert(62)
sl.search(62)
sl.search(45)		
sl.deleteLL()
sl.display()	