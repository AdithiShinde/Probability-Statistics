from scipy.stats import norm
import numpy as np
mu=2.2
sigma=0.3
n=100
def norm_cdf(a,mu,sigma,n):
    mean=mu;
    std=sigma/np.sqrt(n);
    z_score=(a-mean)/std;
    cdf_prob=norm.cdf(z_score)
    return cdf_prob
print("enter the value from case-1")
value1=float(input())
prob1=norm_cdf(value1,mu,sigma,n)
print(round(prob1,5))
print("enter the first value from case-2")
min_value=float(input())
print("enter the second value from case-2")
max_value=float(input())
prob2=norm_cdf(max_value,mu,sigma,n)-norm_cdf(min_value,mu,sigma,n)
print(round(prob2,5))
print("enter the value from case-3")
value2=float(input())
prob3=1-norm_cdf(value2,mu,sigma,n)
print(round(prob3,5))