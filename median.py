import numpy as np
print("Enter the data under the attribute scores:\n")
val=list(map(float,input().split()))
y=sorted(val)
n=len(val)
if n%2!=0:
    median=y[int(((n+1)/2))-1]
else:
    median=(y[int(n/2)-1]+y[int(n/2)])/2
    print('\n(i)The medain score is=',median)
vals,counts=np.unique(val,return_counts=True)
index=np.argmax(counts)
mode=vals[index]
print('\n(ii)The mode is=',mode)



