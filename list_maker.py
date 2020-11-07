'''
This module has 6 functions.
Each of the functions are for creating a list.
1. to create an unordered list of integers ( 3 parameters )
2. to create an ascending list of randomly  generated integers ( 3 parameters )
3. to create a descending list of randomly generated integers. ( 3 parameters )
4. to create an unordered list of floats ( 1 parameter ) 
5. to create an ascending list of randomly generated floats ( 1 parameter )
6. to create a descending list of randomly generated floats. ( 1 parameter )
Each function returns a list after they are executed.
Written by: Ayaz Vural
Student number: 20105817
Date: March 22nd 2019
'''
import random
def unordered_int_list(small,big,length):
    list1 = []
    list1 = random.sample(range(small,big+1),length) # +1 is to include the maximum value.
    return list1

def ordered_ascending_list(small,big,length):
    list2 = []
    list2 = random.sample(range(small,big+1),length) # +1 is to include the maximum value.
    list2.sort() # sorts to change the order to ascending.
    return list2
    
def ordered_descending_list(small,big,length):
    list3 = []
    list3 = random.sample(range(small,big+1),length) # +1 is to include the maximum value.
    list3.sort() 
    list3.reverse() # reverses to make the sorted list descending.
    return list3
 
def unordered_floats(length):
    list4 = []
    for  x in range(length):
        list4.append(random.uniform(0.0,1.0)) 
    return list4

def ordered_ascending_floats(length):
    list5 = []
    for  x in range(length):
        list5.append(random.uniform(0.0,1.0))
        list5.sort()
    return list5
    
def ordered_descending_floats(length):
    list6 = []
    for  x in range(length):
        list6.append(random.uniform(0.0,1.0))
        list6.sort()
        list6.reverse()
    return list6

if __name__ == "__main__":
    print("~~TESTING~~")
    print("\n")
    
    print("Testing unordered_int_list function")
    print("Expected output is a random list")
    print(unordered_int_list(12,100,40))
    print("\n")
    
    print("Testing ordered_ascending_list function")
    print("Expected output is an ordered ascending list")
    print(ordered_ascending_list(34,1000,12))
    print("\n")
    
    print("Testing ordered_descending_list function")
    print("Expected output is an ordered descending list")
    print(ordered_descending_list(1,1000,50))
    print("\n")
    
    print("Testing unordered_floats function")
    print("Expected output is unordered floats list")
    print(unordered_floats(11))
    print("\n")
    
    print("Testing ordered_ascending_floats function")
    print("Expected output is an ordered ascending floats list")
    print(ordered_ascending_floats(22))
    print("\n")
    
    print("Testing ordered_descending_floats function")
    print("Expected output is an ordered descending floats list")
    print(ordered_descending_floats(22))
