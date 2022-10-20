import numpy as np #import numpy library
"""
input array- 2,2,2,8
output array-7,7,7,8
Objectives-
          1)replace a repetitive number with another number throughout array.
          2)count the times number is repeating.
"""


class array_problem:
    def __init__(self,array):# Parameterized Constructor- with array as input from user.
        self.array=array #globalize your array 
    
    def array_detail(self):# creation ofarray detail function
        array=np.array(self.array)#localize the array & convert the user input from tuple to array
        print("Input type",type(array))#type of array
        print("length of array-",len(array))#length of array
        print("Array dimension-",array.ndim)#array dimensions
        print("Array Elements-",array)#print elements of array

    def array_updation(self):# Creation of update function
        a=np.array(self.array)#localize the array & convert the user input from tuple to array
        array_len=len(self.array)#array length
        if array_len >1:#update only if length greater than one
            replace=int(input("Repetitive Element To Be Replaced-"))#repititive element to be replaced
            new=eval(input("Enter New Element-"))#new element which replaces
            repeat=0 #to count no. of times your item repeats
            for i in range(0,array_len):#loop from 0 to length of array
                repeat+=1 #increment count of repeat element
                if a[i]==replace: #if element matches
                    a[i]=new #then replace
                else: #if length is less than one.
                    print("Repetitive Element Not found.") 
                    break
        
            print("Repeat count of Number {} is-".format(replace),repeat)       
            print("Updated Array-",a,type(a))
        else:
            print("Only one element in array.")

user=eval(input("Enter Input array="))#taking input from user as expression.
obj=array_problem(user) #create object & pass array as input
obj.array_detail()#call detail function
obj.array_updation()#call updation function
    

