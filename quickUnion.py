
#quick union is lazy method
def initilaize():
    global n
    n=[]
    mn= int(input("Enter the number of elements: "))
    for i in range(mn):
         n.append(int(input(f"Enter the parent of {i} : ")))
  
    print(n)
    
def root(i):
    while(i !=n[i]): i=n[i]
    return i
initilaize()
def isConnected(a,b):
    return root(a)==root(b)

def union(a,b):
    rootA = root(a)
    rootB = root(b)
    n[rootB] = rootA



# n=[0, 1, 2, 3,4,5,6,7,8,9] avg =5.11
#out is [6, 2, 7, 4, 9, 6, 6, 6, 4, 6]
#for the wieghtedqioc union the max depth  is in order of logn to the base 2  avg =1.11 depth is much much lower
# union(4,3)
# union(3,8)
# union(6,5)
# union(9,4)
# union(2,1)
# union(5,0)
# union(7,2)
# union(6,1)
# union(7,3)
# print(n)