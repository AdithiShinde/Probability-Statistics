import numpy as np 
print('Enter the data under the attribute lower bound of no. of letters:\n')
L=list(map(float,input().split())) 
print('Enter the data under the attribute upper bound of no. of letters:\n')
U=list(map(float,input().split())) 
print('Enter the data under the attribute Number of Surnames:\n') 
F=list(map(float,input().split()))  
def mean_cont(l,u,f): 
     
    x=list((np.array(l)+np.array(u))/2) 
     
    prod_sum=0 
     
    for i,j in zip(x,f): 
     
        prod_sum=prod_sum+i*j 
     
    return(prod_sum/sum(f)) 
 
mean=mean_cont(L,U,F) 
 
x=list((np.array(L)+np.array(U))/2) 
 
sum_squares=0 
for i,j in zip(x,F) : 
    sum_squares=sum_squares+(i-mean)**2*j 
     
var_cont= sum_squares/sum(F) 
 
print('\n (i) The mean of letters in the surnames is = {:.4f}'.format(mean))
print('\n (ii) The standard deviation is = {:.4f}'.format(np.sqrt(var_cont))) 
 

