import math

#Factorial 
x = 10
print(math.factorial(x)) # 3628800
print(math.factorial(0)) # 1
print(math.factorial(5)) # 120

#Combinations
n = 5
r = 3
print(math.comb(n, r)) # 10
print(math.comb(10, 0)) # 1
print(math.comb(10, 1)) # 10
print(math.comb(10, 2)) # 45

#Permutations
n = 5
r = 3
print(math.perm(n, r)) # 60
print(math.perm(10, 0)) # 1
print(math.perm(10, 1)) # 10    
print(math.perm(10, 2)) # 90

#Exponential and Logarithmic Functions
print(math.exp(1)) # 2.718281828459045
print(math.log(10)) # 2.302585092994046
print(math.log10(100)) # 2.0
print(math.log2(8)) # 3.0
print(math.exp(10)) # 22026.465794806718

#Scipy Library for advanced statistics
import scipy
from scipy import stats
#Binomial Distribution
x = stats.binom(10, 0.5) 
print(x.pmf(5)) # 0.24609375
print(x.cdf(5)) # 0.623046875
print(x.mean()) # 5.0
print(x.var()) # 2.5
print(x.std()) # 1.5811388300841898
print(x.rvs()) # random sample from the distribution
print(x.rvs(5)) # array([4, 6, 4, 5, 6])
help(x) # list of all methods and attributes

#Poisson Distribution
x = stats.poisson(3) # random variable with mean 3
print(x.pmf(2)) # 0.22404180765538775
print(x.cdf(2)) # 0.42319008112684364
print(x.rvs()) # random sample from the distribution

#geometric Distribution
x = stats.geom(0.5) # random variable with p=0.5
print(x.pmf(3)) # 0.125
print(x.cdf(3)) # 0.875
print(x.rvs()) # random sample from the distribution

#Normal Distribution
x = stats.norm(0, 1) # random variable with mean 0 and std
print(x.pdf(0)) # 0.3989422804014337
print(x.cdf(0)) # 0.5
print(x.rvs()) # random sample from the distribution

#Exponential Distribution
b = stats.expon(scale=1/4)
print(b.pdf(1)) # 0.18393972058572117
print(b.cdf(1)) # 0.6321205588285577
print(b.rvs()) # random sample from the distribution

#Beta Distribution
x = stats.beta(2, 5) # random variable with a=2 and b=5
print(x.pdf(0.5)) # 1.875
print(x.cdf(0.5)) # 0.890625
print(x.rvs()) # random sample from the distribution