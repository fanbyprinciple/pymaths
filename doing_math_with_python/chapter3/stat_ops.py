arraylist = [1,2,3,4,5,6,4,3,4,5,6,2,3,1,3,3]

def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s/N

    return mean

def calculate_median(numbers):
    numbers.sort()
    # print(numbers[len(numbers)//2])
    return numbers[len(numbers)//2] 

def calculate_mode(numbers):
    # from collections import Counter
    # c = Counter(numbers)
    # return c.most_common(1)[0][0]

    numbers.sort()
    
    dict = {}
    
    for i in numbers:
        if (i in dict):
            dict[i] += 1
        else:
            dict[i] = 1
    
    for i in dict:
        print(i, " : ", dict[i])

    max = 0
    for j in dict:
        if(dict[j]>max):
            max = dict[j]
        
    return max
    #print(dict.__dict__)

def print_min_max(number):
    print('min', ' : ', min(number))
    print('max', ':', max(number))


print('array: ', str(" ".join(str(arraylist))))
print('mean: ', calculate_mean(arraylist))
print('median: ',calculate_median(arraylist))

print('mode: ',calculate_mode(arraylist))
print_min_max(arraylist)