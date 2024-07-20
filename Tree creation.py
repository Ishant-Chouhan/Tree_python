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
            self.preorder_wr(self.root)
        elif choice==2:
            self.inorder_wr(self.root)
        elif choice==3:
            self.postorder_wr(self.root)
    def inorder(self,root):#using recursion
            if root is not None:
                self.inorder(root.left)
                print(root.item)
                self.inorder(root.right)  
    def preorder(self,root):#using recursion
        if root:
            print(root.item)
            self.preorder(root.left)  
            self.preorder(root.right)
    
    def postorder(self,root):#using recursion
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.item)

    def inorder_wr(self,root):
        stack=[]
        result=[]
        current=root
        while current or stack:
            while current:
                stack.append(current)
                current=current.left
            
            current=stack.pop()
            result.append(current.item)
            current=current.right
        print(result)

    def preorder_wr(self,root):
        stack=[]
        result=[]
        current=root
        while current or stack:
            while current:
                 stack.append(current)
                 current=current.left
            current=stack.pop(0)
            result.append(current.item)
            current=current.right
        print(result)

    def postorder_wr(self,root):
        stack=[]
        current=root
        while current or stack:
            while current:
                if current.left.left==None or current.left.left in stack:
                    temp=current
                #stack.append(current.item)
                current=current.left
            stack.append(current)
            current=temp
            current=temp.right

tree=BST()
while True:
    print("""press 1 to add element in tree
press 2 to perform searching
press 3 to perform travelsal
press any other key to exit""")
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
