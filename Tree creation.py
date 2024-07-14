class node:
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None
    
class BST:
    def __init__(self):
        self.root=None

    def add(self,newnode):
        if self.root==None:
            self.root=newnode
        else:
            temp=self.root
            while True:
                if newnode.item>=temp.item and temp.right==None:
                    temp.right=newnode
                    print("Data inserted successfully...!!")
                    break
                elif newnode.item<temp.item and temp.left==None:
                    temp.left=newnode
                    print("Data inserted successfully...!!")
                    break
                elif newnode.item>=temp.item:
                    temp=temp.right
                else:
                    temp=temp.left

    def search(self,element):
        if self.root==None:
            print("Oops...Tree is empty...!!")
        else:
            temp=self.root
            while temp!=None:
                if temp.item==element:
                    print("search successfull...!!")
                    break
                elif element>temp.item:
                    temp=temp.right
                elif element<temp.item:
                    temp=temp.left
            if temp==None:
                print("search unsuccessfull...!!")

    def traversal(self):
        self.inorder(self.root)
    def inorder(self,root):
            if root:
                self.inorder(root.left)
                print(root.item)
                self.inorder(root.right)    
                

tree=BST()
while True:
    print("""press 1 to add element in tree
press 2 to perform searching""")
    choice=int(input("enter your choice: "))
    if choice==1:
        tree.add(node(int(input("Enter data: "))))
    elif choice==2:
        tree.search(int(input("Enter element to be searched: ")))  
    elif choice==3:
        tree.traversal()
    elif choice==4:
        pass
    elif choice==5:
        pass
    else:
        print("Exit...") 
        break 
