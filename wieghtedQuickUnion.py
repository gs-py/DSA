def initialize():
    global n,sz

    n=[]
    num=int(input("Enter The number : "))
    sz=[1]*num
  
    for i in range(num):
        n.append(int(input(f"Enter The parent of Node {i} : ")))
        

def root(a):
        while(a != n[a]): a=n[a]
        return a
    
def union(a,b):
    root_a = root(a)
    root_b = root(b)
    
    if root_a != root_b:
        if sz[root_a] < sz[root_b]:
            n[root_a] = root_b
            sz[root_b] += sz[root_a]
        else:
            n[root_b] = root_a
            sz[root_a] += sz[root_b]
  
initialize()
union(4,3)
union(3,8)
union(6,5)
union(9,4)
union(2,1)
union(5,0)
union(7,2)
union(6,1)
union(7,3)
# in path compresssion change the root function
#rather than selecting paraent it select its grand parent so it improvise the legth by logn times

# def root(a):
#         while(a != n[a]): n[a]=n[n[a]];a=n[a]
#         return a
