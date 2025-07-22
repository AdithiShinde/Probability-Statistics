import numpy as np
print('Enter the data under the attribute Age of the Policy holder:\n')
x=list(map(float,input().split())) 
print('Enter the data under the attribute No. of policy holders:\n') 
f=list(map(float,input().split())) 
def mean_discrete(x,f):  
    prod_sum=0  
    for i,j in zip(x,f): 
        prod_sum=prod_sum + i*j    
    return(prod_sum/sum(f)) 
mean=mean_discrete(x,f)
print('(i)The mean age of the policy holders is = {:.4f}'.format(mean))  
sum_squares=0 
for i,j in zip(x,f): 
    sum_squares=sum_squares+(i-mean)**2*j 
var_discrete= sum_squares/sum(f) 
print('(ii) The Variance is = {:.4f}'.format(var_discrete),'and the standard deviation is = {:.4f}'.format(np.sqrt(var_discrete))) 



