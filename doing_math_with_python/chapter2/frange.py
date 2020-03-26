'''
Generating equally spaced floating points
'''

def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment
    
    return numbers
