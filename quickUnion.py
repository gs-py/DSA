
#quick union is lazy method
def initilaize():
    global n
    n=[]
    mn= int(input("Enter the number of elements: "))
    for i in range(mn):
        n.append(int(input(f"Enter the parent of {i} : ")))
  #[0, 1, 2, 8, 3, 5, 5, 7, 8, 9]
    print(n)
    
def root(i):
    while(i !=n[i]): i=n[i]
    return i
#initilaize()
def isConnected(a,b):
    return root(a)==root(b)

def union(a,b):
    rootA = root(a)
    rootB = root(b)
    n[rootA] = rootB
n=[0, 1, 1, 8, 3, 5, 5, 7, 8, 8]


print(n)
print(isConnected(5,4)) #true
union(5,0)
print(n)
union(7,2)
print(n)
union(6,1)
print(n)
union(7,3)
print(n) #trure