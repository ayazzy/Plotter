'''
This module contains five function.
Swap --> exchanges the values of different elements.
Bubble sort --> sorts list by ascending order by their value.
Bubble sort optimized --> sorts list into ascending order but this version passes over already sorted elements.
Insertion sort --> sorts lists into ascending order by value.
Selection sort --> sorts lists into asending order by value.
Written by: Ayaz Vural
Student number: 20105817
Date: March 22nd 2019
'''
def swap(a, x, y):#created for use in the other functions.
    a[x], a[y] = a[y], a[x]
    
def bubble_sort(x):
    swapped = True
    count = 0 
    while swapped:
        swapped = False
        for i in range(1,len(x)):
            if x[i-1] > x[i]:
                swap(x, i-1, i)
                swapped = True
                count += 1 #increases every iteration
    return count
  
def bubble_sort_opt(a):
    count = 0 
    n = len(a)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1,n):
            if a[i-1] > a[i]:
                swap(a, i-1, i)
                swapped = True
                count += 1 # count increases every iteration.
        n -= 1
    return count
 
def insertion_sort(aList):
    count = 0
    for i in range(1, len(aList)):
        j = i
        while (j > 0) and (aList[j-1] > aList[j]):
            aList[j-1], aList[j] = aList[j], aList[j-1]
            j = j - 1
        count = count + 1   
    return count

def selection_sort(a):
    n = len(a)
    count = 0 
    for i in range(n-1):
        min = i;
        for j in range(i + 1,n):
            if (a[j] < a[min]):
                min = j;
            count += 1 
        if (min != i):
            swap(a, i, min)
    return count

if __name__ == "__main__":
    print("~~TESTING~~")
    liste = [3,6,4,1,9,8,2,5,7]
    liste1 = [4,7,1,8,9,3,2]
    liste2 = [9,7,8,5,6,3,2,4,1]
    my_list = [6, 3, 5, 1, 7, 8, 2, 4]
    print("\n")
    print("Testing bubble_sort function")
    print(liste)
    print("Testing the count")
    print(bubble_sort(liste))
    print("testing the ascending order")
    print(liste)
    print("\n")
    
    print("Testing bubble_sort_opt function")
    print(liste1)
    print("Testing the count")
    print(bubble_sort_opt(liste1))
    print("Testing the ascending order")
    print(liste1)
    print("\n")
    
    print("Testing selection_sort function")
    print(my_list)
    print("Testing the count")
    print(selection_sort(my_list))
    print("Testing the ascending order")
    print(my_list)
    print("\n")

    print("Testing instertion_sort function")
    print(liste2)
    print("Testing the count")
    print(insertion_sort(liste2))
    print("Testing the ascending order")
    print(liste2)
        

