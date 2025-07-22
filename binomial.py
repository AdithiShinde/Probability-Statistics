import numpy as np
import math
import matplotlib.pyplot as plt
print('Enter the n value')
n=int(input())
p=0.25
def binomial_pmf(n,p,x):
  comb=math.factorial(n)/(math.factorial(x)*(math.factorial(n-x)))
  return comb*p**x*(1-p)**(n-x)
def binomial_cdf(n,p,x):
    cdf=0
    for i in range(0,x+1):
        cdf=cdf+binomial_pmf(n,p,i)
        return cdf
print('\n (i) {:4f}'.format(binomial_pmf(n,p,40)))
print('\n (ii) {:4f}'.format(1-binomial_cdf(n,p,59)))
print('\n (iii) {:.4f}'.format(n*p))
random_variable=list(range(n+1))
binom_prob=[binomial_pmf(n,p,x)for x in range(n+1)]
plt.bar(random_variable,binom_prob)
plt.show()
    