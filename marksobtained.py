print("Enter the data under the attribute obtained:\n")
x=list(map(float,input().split()))
print("Enter the data under the attribute No. of students:\n")
f=list(map(float,input().split()))
N=sum(f)
cusum=0
for i in range(len(x)):
    cusum=cusum+f[i]
    if cusum>N/2:
        print("(i) The value of median is=",int(x[i]))
        break   
i=f.index(max(f))
Mode=x[i]

print("(ii) The value of mode is :",Mode)