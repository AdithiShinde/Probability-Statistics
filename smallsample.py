import numpy as np
from scipy.stats import t
group1=np.array([42,39,38,60,41])
group2=np.array([38,42,56,64,68,69,62])
def Hypothesis_Test_mul2(group1,group2,alpha):
    n1=np.size(group1)
    n2=np.size(group2)
    x1_bar=np.mean(group1)
    x2_bar=np.mean(group2)
    s1_square=np.var(group1,ddof=1)
    s2_square=np.var(group2,ddof=1)
    s_square=((n1-1)*s1_square+(n2-1)*s2_square)/(n1+n2-2)
    s=np.sqrt(s_square)
    t_value=abs((x1_bar-x2_bar)/(s*np.sqrt((1/n1)+(1/n2))))
    df=n1+n2-2
    critical_value=t.ppf(1-(alpha/2),df)
    print('t_value=',t_value)
    print('critical_value',critical_value)
    if t_value>critical_value:
        print('''Reject the null hypothesis H_0;
there is a significant difference between the medicines\n''')
    else:
            print('''We fall  to reject the null hypothesis
H_0;there is no significant difference between medicines\n''')
print('enter the alpha from case 1')
alpha1=float(input())
Hypothesis_Test_mul2(group1,group2,alpha1)
print('enter the alpha from case 2')
alpha2=float(input())
Hypothesis_Test_mul2(group1,group2,alpha2)
print('enter the alpha from case 3')
alpha3=float(input())
Hypothesis_Test_mul2(group1,group2,alpha3)