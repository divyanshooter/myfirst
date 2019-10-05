import numpy as np
import matplotlib.pyplot as plt
d={}
dtype=[('Sname','S10'),('join_year','int'),('salary','int')]
values=[('r',2005,15000),('u',2006,16000),('y',2005,17000),('t',2005,18000),('e',2006,19000),('w',2003,12000)]
a=np.array(values,dtype=dtype)
print(a)

a=np.sort(a,order=['Sname','join_year','salary'])
print(a)

b=np.argmax(a['salary'])
print('Salary')
print(a[b])

c=np.argmax(np.unique(a['join_year'],return_counts=True))
print('\nyear',a[c]['join_year'])

z=np.unique(a['join_year'],return_counts=True)
plt.bar(z[0],z[1],color='blue',linewidth=5)
plt.xlabel('year')
plt.ylabel('count')
plt.show()
