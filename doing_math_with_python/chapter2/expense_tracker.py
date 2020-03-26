# # for manual input
# get  = input('how many categories ? : ')

# expenses = []
# for g in get:
#     cat =  input('Enter category : ')
#     exp = input('Enter expenditure : ')
#     expenses.append([cat, exp])


expenses = [["love", 100 ], ["hate",50], ['study',20], ['play',80]]

'''
Creating a bar chart
'''

import matplotlib.pyplot as plt 
from pylab import savefig
import numpy

print(len(expenses))
# num_bars = len(expenses)
# positions = range(1 , num_bars + 1)
cash = numpy.array(expenses)
print(cash[:,0])
print(cash[:,1])

plt.barh(cash[:,0], cash[:,1], align='center')
plt.yticks(cash[:,0], cash[:,0])
plt.xlabel('category')
plt.ylabel('expenditure')
plt.title('Expense tracker')
plt.grid()
plt.show()
savefig('expensetracker.png')