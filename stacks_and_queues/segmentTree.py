class SegmentTree:
    def __init__(self,n):
        self.n=n
        self.lo = [0]*(4*self.n+1)
        self.hi = [0]*(4*self.n+1)
        self.rmin = [0]*(4*self.n+1)
        self.delta = [0]*(4*self.n+1)
        self.initialize(1,0,n-1)
    
    def increment(self,a,b,val):
        self.inc(1,a,b,val)
		
    def minimun(self,a,b):
        return self.mini(1,a,b)
		
    def initialize(self,i,a,b):
        lo[i]=a
        hi[i]=b
        if a==b: return
        m=(a+b)//2
        self.initialize(2*i,a,m)
        self.initialize(2*i+1,m+1,b)

    def prop(self,i):
        self.delta[2*i]+=self.delta[i]
        self.delta[2*i+1]+=self.delta[i]
        self.delta[i]=0
    
    def update(self,i):
        self.rmin[i]= min(rmin[2*i]+delta[2*i],rmin[2*i+1]+delta[2*i+1])
		
    def inc(self,i,a,b,val):
        if a>self.hi[i] or b<self.lo[i]:
            return
        if a<=self.lo[i] and self.hi[i]>=b:
            self.delta[i]+=val
            return
        self.prop(i)
        self.inc(2*i,a,b,val)
        self.inc(2*i+1,a,b,val)
        self.update(i)
		
    def mini(self,i,a,b):
        if a>self.hi[i] or b<self.lo[i]:
            return -99999
        if a<=self.lo[i] and self.hi[i]>=b:
            return self.rmin[i]+self.delta[i]
        self.prop(i)
        minLeft = self.mini(2*i,a,b)
        minRight = self.mini(2*i+1,a,b)
        update(i)
        return min(minLeft,minRight) 