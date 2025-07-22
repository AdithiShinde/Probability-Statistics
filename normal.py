from scipy.stats import norm
mu=50000
sigma=20000
def norm_cdf(a,mu,sigma):
    z_score=(a-mu)/sigma
    cdf_prob=norm.cdf(z_score)
    return cdf_prob
print("enter the value from case-1")
value1=float(input())
prob1=norm_cdf(value1,mu,sigma)
print(round(prob1*100,3))

print("enter the first value from case-2")
min_value=float(input())
print("enter the second value from case-2")
max_value=float(input())
prob2=norm_cdf(max_value,mu,sigma)-norm_cdf(min_value,mu,sigma)
print(round(prob2*100,3))
print("enter the value from case-3")
value2=float(input())
prob3=1-norm_cdf(value2,mu,sigma)
print(round(prob3*100,3))