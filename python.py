def closestStraightCity(c, x, y, q):
    ans=[]
    c.sort()
    for i in range(0,len(q)):
        flag=0
        k=c.index(q[i])
        for j in range(0,len(x)):
            if((c[j]!=q[i]) and (x[k]==x[j] or y[k]==y[j] or x[k]==y[j] or x[j]==y[k])):
                flag=1
                ans.append(c[j])
                break
        if(flag==0):
            ans.append("NONE")        
    return(ans)              
    print(ans)
c=input().split()
x=list(map(int,input().split()))
y=list(map(int,input().split()))
q=input().split()
closestStraightCity(c, x, y, q)
