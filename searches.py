'''
This module has two functions.
Linear Search --> does a linear search when given a collection and a target.
Binary Search --> does a binary search when given a collection and a target.
output for both functions are two element tuples.
Written by: Ayaz Vural
Student Number: 20105817
Date: March 22nd 2019
'''
def linearSearch(collection,target):
    count = 0
    
    for item in collection:
        count +=1
        if target== item:
            return target,count
    return None, count

def binarySearch(collection,target):
    low = 0
    high = len(collection) - 1
    count = 0
    
    while high >= low:
        count = count + 1 
        mid = (high + low) // 2
        
        if target == collection[mid]:
            return target, count
        if target < collection[mid]:
            high = mid - 1
        else:
            low = mid + 1       
    return None, count

if __name__ == "__main__":
    print("~~TESTING~~")
    aList = [1,2,3,4,5,6,7,8,9]
    print(aList)
    print("\n")
    
    print("Testing the binarySearch function")
    print("input is aList and target is 9. Expected output is 9 and 4 in a tuple")
    print(binarySearch(aList,9 ))
    print("\n")
    print("input is the aList and target is 12. Since 12 is not in the list expected output is None and 4")
    print(binarySearch(aList,12 ))
    print("\n")
    
    print("Testing the linearSearch function")
    print("input is aList and target is 9. Expected output is 9 and 9 in a tuple")
    print(linearSearch(aList,9))
    print("\n")
    print("input is aList and target is 11. Expected output is none and 9 in a tuple")
    print(linearSearch(aList,11))
          


    
