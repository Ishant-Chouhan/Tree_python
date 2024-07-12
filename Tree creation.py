class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
class BinaryTree:
    def __init__(self):
        self.root=None

    def add(self,newnode):
        if self.root==None:
            self.root=newnode
        else:
            temp=self.root
            while temp.link!=None:
                if newnode.data>=temp.data:
                    temp=temp.right
                else:
                    temp=temp.left

            if newnode.data>=temp.data:
                temp.right=newnode
            else:
                temp.left=newnode

    