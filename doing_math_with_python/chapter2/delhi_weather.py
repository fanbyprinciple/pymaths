d_temp = [29,24, 27, 28, 30, 31, 31, 32, 34]
d_days = []



for i in range(27,32):
    d_days.append(str(i) + " Mar 20")

for i in range(1,5):
    d_days.append(str(i) + " Apr 20")

print(len(d_temp),len(d_days))



import matplotlib.pyplot as plt
from pylab import savefig

plt.plot(d_days, d_temp)
plt.xlabel('days')
plt.ylabel('temperature')
plt.show()
savefig('delhi_temprature.png')

