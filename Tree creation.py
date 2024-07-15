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
        print("""press 1 for preorder traversal
press 2 for inorder traversal
press 3 for postorder traversal""")
        choice=int(input("Enter your choice: "))
        if choice==1:
            self.preorder(self.root)
        elif choice==2:
            self.inorder(self.root)
        elif choice==3:
            self.postorder(self.root)
    def inorder(self,root):
            if root is not None:
                self.inorder(root.left)
                print(root.item)
                self.inorder(root.right)  
    def preorder(self,root):
        if root:
            print(root.item)
            self.preorder(root.left)  
            self.preorder(root.right)
    
    def postorder(self,root):
        pass

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
    else:
        print("Exit...") 
        break 
