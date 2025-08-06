class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bst:
    def __init__(self):
        self.root=None
    def insert(self,data):
        new=Node(data)
        if self.root==None:
            self.root=new
        else:
            self.insertion(self.root,new)
    def insertion(self,root,new):
        if root.data>new.data:
            if root.left==None:
                root.left=new
            else:
                self.insertion(root.left,new)
        else:
            if root.right==None:
                root.right=new
            else:
                self.insertion(root.right,new)
    def inorder(self):
        st=[self.root]
        while st:
            curr=st.pop()
            if curr:
                print(curr.data)
                st.append(curr.right)
                st.append(curr.left)
      
obj=bst()
obj.insert(8)
obj.insert(9)
obj.insert(10)
obj.insert(99)
obj.inorder()
