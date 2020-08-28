import numpy

class Numpy():
    def __init__(self, my_list, point):
        self.my_list = my_list
        self.point = point
    
    #Finds the value of a polynomial at a specific point
    def find_value_of_p(self):
        print(numpy.polyval(my_list, point))

if __name__ == '__main__':
    my_list = list(map(float, input().split()))
    point = int(input())
    my_object = Numpy(my_list, point)
    my_object.find_value_of_p()