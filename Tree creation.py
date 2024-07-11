class node:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
    
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
                    temp=temp.rchild
                else:
                    temp=temp.lchild

            if newnode.data>=temp.data:
                temp.rchild=newnode
            else:
                temp.lchild=newnode

    