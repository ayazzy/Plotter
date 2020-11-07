'''
This module has 6 functions.
Each of the functions operate connected to a sorting or a searching technique.
creates text files according to the method selected by the user.
Written by: Ayaz Vural
Student number: 20105817
Date: March 22nd 2019
'''
import list_maker
import searches
import sorts

def data_maker_lin(liste):
    lin_search = open("linear_search.txt","w") # created the text file here.
    for i in range(len(liste)): # a loop to go over the slices of the original list.
        newList = liste[0:i]
        x = searches.linearSearch(newList,2000)
        lin_search.write(str(x[1]) + "\n") # writing the counts to the text file line by line
    lin_search.close()
    return print("Text file created")

def data_maker_binary(liste):
    bin_search = open("binary_search.txt","w") # created the text file here.
    for i in range(len(liste)): # a loop to go over the slices of the original list.
        newList = liste[0:i]
        x = searches.binarySearch(liste,2000)
        bin_search.write(str(x[1]) + "\n") # writing the counts to the text file line by line
    bin_search.close()
    return print("Text file created")


def data_maker_bubble(liste):
    bubble_sort = open("bubble_sort.txt","w") # created the text file here.
    for i in range(len(liste)): # a loop to go over the slices of the original list.
        newList = liste[0:i]
        a = sorts.bubble_sort(newList)
        bubble_sort.write(str(a) + "\n") # writing the counts to the text file line by line
    bubble_sort.close()
    return print("Text file created")

def data_maker_bubble_opt(liste):
    bubble_sort_opt = open("optimized_bubble_sort.txt","w") # created the text file here.
    for i in range(len(liste)): # a loop to go over the slices of the original list.
        newList = liste[0:i]
        a = sorts.bubble_sort_opt(newList)
        bubble_sort_opt.write(str(a) + "\n") # writing the counts to the text file line by line
    bubble_sort_opt.close()
    return print("Text file created")

def data_maker_selection(liste):
    selection_sort = open("selection_sort.txt","w") # created the text file here.
    for i in range(len(liste)): # a loop to go over the slices of the original list.
        newList = liste[0:i]
        a = sorts.selection_sort(newList)
        selection_sort.write(str(a) + "\n") # writing the counts to the text file line by line
    selection_sort.close()
    return print("Text file created")

def data_maker_insertion(liste):
    insertion_sort = open("insertion_sort.txt","w") # created the text file here.
    for i in range(len(liste)): # a loop to go over the slices of the original list.
        newList = liste[0:i]
        a = sorts.insertion_sort(newList)
        insertion_sort.write(str(a) + "\n") # writing the counts to the text file line by line
    insertion_sort.close()
    return print("Text file created")









   

  

