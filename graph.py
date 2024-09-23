# class graph():
#     gdict = { }
#     def __init__(self ,edges,):
        
#         self.edges =edges;
       
        
#         for start , end in self.edges:
#             if start in graph.gdict and ( end not in graph.gdict[start] ):
                
#                 graph.gdict[start].append(end)
#             else:
#                graph.gdict[start] = [end]

#         print(graph.gdict)                
        
        

# if __name__ == '__main__':
    
#     routes = [
#         ("mumbai","delhi"),
#         ("mumbai","newyork"),
#         ("paris","delhi"),
#         ("paris","dubai"),
#         ("delhi","dubai"),
#         ("newyork","paris")
#             ]
#     routes2 = [
#         ("mumbai","delhi"),
#         ("mumbai","newyork"),
#         ("paris","delhi"),
#         ("kochi", "chennai"),
#         ("chennai", "bangalore"),
#         ("delhi","dubai"),
#         ("newyork","paris")
    
#             ]

# graph(routes)
# graph(routes2)

class Graph:
    gdict = {}  # Class variable shared by all instances

    def __init__(self, edges):
        self.edges = edges
        
        for start, end in self.edges:
            if start in Graph.gdict  :
                if end not in Graph.gdict[start]:
                    Graph.gdict[start].append(end)
            else:
                            
                Graph.gdict[start] = [end]
        print("Routes adddes Sucessfulyy....")
        print(Graph.gdict)
    @classmethod
    def get_path(cls, start ,end , path = []):
        
        path = path + [start]
        
        if start == end:
            return [path]
        
        if start not in cls.gdict:
            return []
        
        paths = []
        for node in cls.gdict[start]:
            if node not in path:
                new_path = cls.get_path(node , end, path)
                for p in new_path:
                    paths.append(p)
        return paths
        
            

        

if __name__ == '__main__':

    routes = [
        ("mumbai", "paris"),
        ("mumbai", "dubai"),
        ("paris", "newyork"),
        ("dubai", "newyork"),
      
        ("newyork", "toronto")
    ]

    routes2 = [
        ("mumbai", "delhi"),
        ("mumbai", "newyork"),
        ("paris", "delhi"),
        ("kochi", "chennai"),
        ("chennai", "bangalore"),
        ("delhi", "dubai"),
        ("newyork", "paris")
    ]

    graph1 = Graph(routes)
    graph2 = Graph(routes2)

    # Print the combined routes
    
    print(Graph.get_path("mumbai" ,"newyork"))