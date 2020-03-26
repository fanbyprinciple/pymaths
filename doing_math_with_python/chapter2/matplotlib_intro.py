# x_numbers = [1,2,3]
# y_numbers = [2,4,6]

# from pylab import plot,show
# plot(x_numbers, y_numbers, marker='o')
# show()

# nyc_temp_1 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 66.0, 57.0]
# nyc_temp_2 = [29.3, 37.5, 47.6, 51.7, 63.5, 71.3, 66.0, 57.0]
# nyc_temp_3 = [31.3, 46.3, 46.2, 54.0, 60.5, 71.3, 63.0, 54.0]


# months = range(1,9)

# print(months)
# print(nyc_temp_1)

# plot(months, nyc_temp_1, nyc_temp_2, nyc_temp_3)

# show()

# plot(months, nyc_temp_1)
# plot(months, nyc_temp_2)
# plot(months, nyc_temp_3)
# show()

# plot(nyc_temp_1, marker='o')

# from pylab import axis
# print(axis())

# print(axis(ymin=0))

# show()

import matplotlib.pyplot 
from pylab import plot, savefig

def create_graph():
    x_numbers = [1,2,3]
    y_numbers = [2,4,10]

    plot(x_numbers, y_numbers)
    savefig('mygraph.png')
    

if __name__ == '__main__':
    create_graph()
