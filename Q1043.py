#BFS method (Faster)
PeopleNum, PartyNum = map(int, input().split())
TrueKnower = list(map(int, input().split()))[1:]
Party = [list(map(int, input().split()))[1:] for v in range(PartyNum)]

Truth = [0 for v in range(PeopleNum + 1)]
PartyCount = [False for v in range(PartyNum)]

for item in TrueKnower:
    queue = [item]
    Truth[item] = 1

    #BFS method
    while queue:
        Temp = queue.pop()
        for i in range(PartyNum):
            if Temp in Party[i]:
                PartyCount[i] = True

                for ppl in Party[i]:
                    if Truth[ppl] == 0:
                        queue.append(ppl)
                        Truth[ppl] = 1
print(PartyCount.count(False))


#Union find method (For practice on the topic)
PeopleNum, PartyNum = map(int, input().split())
TrueKnower = list(map(int, input().split()))[1:]
Party = [list(map(int, input().split()))[1:] for v in range(PartyNum)]

parent = [v for v in range(PeopleNum + 1)]
NoLies = 0

def Find(node):
    if parent[node] == node:
        return node
    
    parent[node] = Find(parent[node])
    return parent[node]

def Union(nodes):
  #Unit all nodes using a minimum
    minimum = 51
    for x in nodes:
        minimum = min(Find(x), minimum)
    
    for x in nodes:
        parent[x] = minimum

#Repeat it multiple times for it to completely register
for i in range(PeopleNum):
    for item in Party:
        Union(item)
#Check
for item in Party:
    Cannot = False
    for t in TrueKnower:
        for ppl in item:
            if parent[t] == parent[ppl]:
                NoLies += 1
                Cannot = True
                break
        if Cannot:
            break

print(PartyNum - NoLies)


