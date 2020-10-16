class BTree{

	class Node{
		int[] keys;
		Node[] child;
		int t;
		int nKeys;
		boolean isLeaf;
		Node(int t, boolean isLeaf){
			this.t=t
			this.keys = new int[2*t-1];
			this.child = new Node[2*t];
			this.nKeys= 0;
			this.isLeaf=isLeaf;
		}
	}
	Node root;
	int t;
	Btree(int t){
		this.root = null;
		this.t = t;
	}

	public void traverse(Node curNode){
		int i;
		for(i=0;i<curNode.nKeys;i++){
			if(!curNode.isLeaf){
				this.traverse(curNode.child[i]);
			}
			System.out.print(" "+curNode.keys[i]);
		}
		if(!curNode.isLeaf){
			this.traverse(curNode.child[i]);
		}	
	}

	public boolean search(int key){
		boolean this.search(this.root, key);
	}
	public boolean search(Node curNode, int key){
		int i=0;
		while(i<curNode.nKeys && key>curNode.keys[i]){
			i++;
		}
		if(curNode.keys[i]==k){
			return true;
		}
		if(curNode.isLeaf){
			return false;
		}
		return this.search(curNode.child[i], key);
	} 

	public void insert(int key){
		if(this.root==null){
			this.root = new Node(this.t, true);
			this.root.keys[0] = key;
			this.root.nKeys = 1
		}else{
			if(this.root.nKeys==2*this.t-1){
				Node newNode = new Node(this.t, false);
				newNode.child[0]=this.root;
				this.splitChild(newNode, 0, this.root);
				int i=0;
				if(newNode.keys[0]<key){
					i++;
				}
				this.insertNonFull(newNode.child[i], key);
				this.root = newNode;
			}else{
				this.insertNonFull(this.root, key);
			}
		}
	}
	public void insertNonFull(Node curNode, int key){
		int i = curNode.nKeys;
		if(curNode.isLeaf){
			while(i>0 && curNode.keys[i-1]>key){
				curNode.keys[i]=curNode.keys[i-1];
				i--;
			}
			curNode.keys[i]=key;
			curNode.nKeys+=1;
		}else{
			while(i>0 && curNode.keys[i-1]>key){
				i--;
			}
			if(curNode.child[i].nKeys==2*this.t-1){
				this.splitChild(curNode, i, curNode.child[i]);
				if(curNode.keys[i]<key){
					i++;
				}
			}
			this.insertNonFull(curNode.child[i], key)
		}
	}

	public void splitChild(Node curNode, int i, Node cNode){
		Node newNode = new Node(this.t, cNode.isLeaf);
		newNode.nKeys = this.t-1;
		for(int j=0;j<this.t-1;j++){
			newNode.keys[j]=cNode.keys[j+this.t];
		}
		if(!cNode.isLeaf){
			for(int j=0;j<this.t-1;j++){
				newNode.child[i]=cNode.child[j+this.t];
			}
		}
		cNode.nKeys=this.t-1;
		for(int j=curNode.nKeys;j>=i+1;j--){
			curNode.child[j+1]=curNode.child[j];
		}
		curNode.child[i+1]=newNode;
		for(int j=curNode.nKeys-1;j>=i;j--){
			curNode.keys[j+1]=curNode.keys[j];
		}
		curNode.keys[i]=cNode.keys[this.t-1];
		curNode.nKeys+=1;
	}
}