n= list()
def initialize():
       

        for i in range(10):
            n.append(i)
            
        print(n)
        
def isConnected(a,b)-> bool:
    return n[a]==n[b]
def union(a,b):
    if n[b] !=n[a]:
        root1 =n[a]
        root2=n[b]
        for i in range(0,len(n)):
            if n[i] == root1:
                n[i]=root2
            
        print(n)
def compnents():
    comp={}
    for i in range(len(n)):
        root=n[i]
        if root not in comp:
            comp[root]=[]
        comp[root].append(i)
    
    for cn in comp.values:
        print(sorted(cn))
         

    
    
initialize()
union(1,2)
union(1,9)
union(9,7)
union(7,8)
union(0,5)
union(5,6)
union(3,4)
union(2,8)
compnents()