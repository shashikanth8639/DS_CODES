class STree:
	def __init__(self,n):
		self.n=n
		self.mins=[0]*(2*n+1)
		self.delta=[0]*(2*n+1)
	
	def init(self,arr,n):
		self.initialize(arr,1,0,n-1)
	
	def update(self,i):
		self.mins[i] = min(self.mins[2*i]+self.delta[2*i],self.mins[2*i+1]+self.delta[2*i+1])
	
	def prop(self,i):
	
		self.delta[2*i]+=self.delta[i]
		self.delta[2*i+1] += self.delta[i]
		self.delta[i]=0
	
	def initialize(self,arr,i,start,end):
		
		if start==end:
			self.mins[i]=arr[start]
			return
		mid = (start+end)//2
		
		self.initialize(arr,2*i,start,mid)
		self.initialize(arr,2*i+1,mid+1,end)
		
		self.update(i)
		
	#Single value increment
	def increment(self,index,val):
		self.inc(arr,1,0,n-1,index,val)
	
	def inc(self,arr,i,start,end,index,val):
		
		if start==end:
			arr[index]+=val
			self.mins[i]+=val
			return
		
		mid = (start+end)//2
		
		if index>=start and index<=mid:
			self.inc(arr,2*i,start,mid,index,val)
		else:
			self.inc(arr,2*i+1,mid+1,end,index,val)
			
		self.update(i)
	
	def incrementRange(self,a,b,val):
		self.incMany(arr,1,0,n-1,a,b,val)
	
	def incMany(self,arr,i,start,end,a,b,val):
		
		if a>end or b<start:
			return
		
		if a<=start and b>=end:
			delta[i]+=val
			return
		
		self.prop(i)
		
		mid = (start+end)//2
		self.incMany(arr,2*i,start,mid,a,b,val)
		self.incMany(arr,2*i+1,mid+1,end,a,b,val)
		
		self.update(i)
	
	def minimum(self,a,b):
		return self.mini(arr,1,0,n-1,a,b)
	
	def mini(self,arr,i,start,end,a,b):
		if a>end or b<start:
			return
		
		if a>=start and b<=end:
			return self.mini[i]+self.delta[i]
		
		self.prop(i)
		
		mid=(start+end)//2
		l = self.mini(arr,2*i,start,mid,a,b)
		r = self.mini(arr,2*i+1,mid+1,end,a,b)
		
		self.update(i)
		
		return min(l,r)