def my_sum(x, y):
    '''
    Takes in two numbers and returns its sum
    '''

    if type(x) != int or type(y) != int:
        return "Invalid input"
    else:
        return x + y

def super_sum(*args):
    
    sum_item = 0

    for i in range(len(args)):
        sum_item += args[i]

    return sum_item
