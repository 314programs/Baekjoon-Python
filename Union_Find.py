def FindParent(target):
    if target == parent[target]:
        return target
    parent[target] = FindParent(parent[target])
    return parent[target]
    
def UnionFind(a,b):
    a = FindParent(a)
    b = FindParent(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

