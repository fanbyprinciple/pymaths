
def fibo(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    
    a = 1
    b = 1
    series = [a, b]
    for _ in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c
    
    return series

series = fibo(100)
list = list(range(1,102))

print(len(series))
print(len(list))

ratio = []
for i in range(1, len(series)):
    ratio.append(series[i]/series[i-1])

print(len(ratio))

import matplotlib.pyplot as plt 
from pylab import savefig

plt.plot(list, ratio)
plt.xlabel('n')
plt.ylabel('ratio')
plt.title('golden ratio demonstration')
plt.show()
savefig('fibo.png')
