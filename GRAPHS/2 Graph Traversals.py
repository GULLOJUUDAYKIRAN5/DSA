from collections import defaultdict,deque
graph=defaultdict(list)
def add_edge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)
n,m=input("enter the noof nodes and edges").split()
for i in range(int(m)):
    u,v=input("enter the edges").split()
    add_edge(graph,u,v)
for node,nebigh in graph.items():
    print(f'{node}--->{nebigh}')
# traveling through the node by its level
def BFS(graph,start):
    visited=set()
    visited.add(start)
    st=deque([start])
    while st:
        node=st.popleft()
        print(node)
        for nebigh in graph[node]:
            if nebigh not in visited:
                st.append(nebigh)
                visited.add(nebigh)
BFS(graph,'a')

def DFS(graph,start):
    st=[start]
    visited=set()
    while st:
        node=st.pop()
        if node not in visited:
            print(node,end=" ")
            visited.add(node)
            # to maintain from left to right
            st.extend(reversed(graph[node]))
DFS(graph,'a')
            




