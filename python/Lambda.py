def square(num1):
    return num1**2
if __name__=='__main__':
    my_arr=[1,2,3,4,5]
    for num in map (square,my_arr):
        print(num)
        list