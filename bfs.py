import heapq
visited=[0]*10000
def make_graph(e):
    d = {}
    for i in range(e):
        x, y, z = map(int,input().split())
        if x not in d:
            d[x]=[[z,y]]
        else:
            d[x].append([z,y])
        if y not in d:
            d[y]=[[z,x]]
        else:
            d[y].append([z,x])
    return d
def best_first_search(graph,head,goal,n):
    q=[head]
    l=[-1]*n
    heapq.heapify(q)
    visited[head[1]]=1
    while len(q)!=0:
        x=heapq.heappop(q)
        if x[1]==goal:
            return True,l
        for i in graph[x[1]]:
            if visited[i[1]]==0:
                visited[i[1]]=1
                l[i[1]]=x[1]
                i[0]+=x[0]
                heapq.heappush(q,i)
n,e=map(int,input().split())
d=make_graph(e)
print(d)
i=9
x,l=best_first_search(d,[0,0],9,n)
print(l)
if x:
    while l[i]!=-1:
        print(str(i)+'<---')
        i=l[i]
