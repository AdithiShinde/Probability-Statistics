import numpy as np
import math
import matplotlib.pyplot as plt
print('enter the N value')
lambd=int(input())
def poisson_pmf(Lambd,x):
    return((math.e)**(-Lambd)*Lambd*x)/math.factorial(x)
def poisson_cdf(Lamdf,x):
    cdf=0
    for i in range(0,x+1):
        cdf=cdf+poisson_pmf(lambd,i)
        return cdf
print('\n i) {:.4f}'.format(poisson_pmf(8*lambd,10)))
print('\n ii) {:.4f}'.format(1-poisson_cdf(8*lambd,14)))
print('\n iii) {:.4f}'.format(1-poisson_cdf(8*lambd,20)))
B=100
random_variable=list(range(B+1))
pois_prob=[poisson_pmf(8*lambd,x)for x in range(B+1)]
plt.bar(random_variable,pois_prob)
plt.show()
