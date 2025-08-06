class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
class bst:
    def __init__(self):
        self.root=None
    def insert(self,data):
        
        if self.root==None:
            self.root=node(data)
        else:
            self.insertion(self.root,data)
    def insertion(self,root,data):
        if root.data>data:
            if root.left==None:
                root.left=node(data)
            else:
                self.insertion(root.left,data)
        else:
            if root.right==None:
                root.right=node(data)
            else:
                self.insertion(root.right,data)
    def preorder(self):
        st=[self.root]
        while st:
            curr=st.pop()
            print(curr.data)
            if curr.right:
                st.append(curr.right)
            if curr.left:
                st.append(curr.left)
    def height(self):
        st=[(self.root,1)]
        maxi=0
        while st:
            curr,height=st.pop()
            if maxi<height:
                maxi=height
            if curr.right:
                st.append((curr.right,height+1))
            if curr.left:
                st.append((curr.left,height+1))
        print(maxi)

    def shortest_path(self):
        st=[(self.root,[self.root.data],1)]
        ans=[]
        mini=float('inf')
        while st:
            node,path,height=st.pop()
            if (not node.left) and (not node.right):
                if height<mini:
                    mini=height
                    ans=path
            if node.left:
                st.append((node.left,path+[node.left.data],height+1))
            if node.right:
                st.append((node.right,path+[node.right.data],height+1))
        print(ans)
        

        

obj=bst()
obj.insert(10)
obj.insert(6)
obj.insert(8)
obj.insert(5)
obj.insert(15)
obj.insert(11)
obj.insert(17)
obj.preorder()
obj.height()
obj.shortest_path()

