from collections import deque,defaultdict
graph=defaultdict(list)
# undirected graph
def add_edge(adj_list,u,v):
    adj_list[u].append(v)
    adj_list[v].append(u)

def display(graph):
    for node,nigh in graph.items():
        print(f'{node}->{nigh}')

n,m=input("enter noof vertices and edges").split()
for i in range(int(m)):
    u,v=input("enter the edges").split()
    add_edge(graph,u,v)
display(graph)

# weighted Graph
x,y=input("enter the noof vertices, edges ").split()
graph1_weight=defaultdict(list)
def add_edge_weight(adj,u,v,w):
    adj[u].append((v,w))
    adj[v].append((u,w))
for i in range(int(y)):
    u,v,w=input("enter the nodes edges and weight").split()
    add_edge_weight(graph1_weight,u,v,w)
display(graph1_weight)








