x_values = [2,4,5,3,3,1,4,3,6,3]

y_values = []
for x in x_values:
    y = x ** 2 + 2 ** x + 1
    y_values.append(y)

print(x_values, y_values)

import matplotlib.pyplot as plt 
from pylab import savefig

plt.plot(x_values, y_values)
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Solutions to x**2 + 2**x + 1')
plt.show()
savefig('quad_graph.png')