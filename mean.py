import numpy as np
print("Enter the data under the attribute Waiting_Time:\n")
val=list(map(float,input().split()))
def mean_observ(dat):
    sum=0
    for i in dat:
        sum=sum+i
        return sum/len(dat)
mean=mean_observ(val)
print('\n (i)The average Waiting Time is={:.4f}'.format(mean))
def variance_observ(dat,mean):
    SS_observ=0
    for i in dat:
        SS_observ=SS_observ+(i-mean)**2
    Var_observ=SS_observ/len(dat)
    return(Var_observ)
varian=variance_observ(val,mean)
print('\n (ii)The varaince is={:.4f}'.format(varian))
