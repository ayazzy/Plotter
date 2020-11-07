'''
This is a module called plot_results.
It basically acts as the main() function of this whole project.
This module makes calls to the plotter to create a graph using the appropriate text file selected
by the user.
Written by: Ayaz Vural
Student number: 20105817
Date: March 22nd 2019
'''
import menu
import sorts
import searches
import plotter
import math
import list_maker
import data_files_maker
from math import sqrt,log
def lin(x): #the mathematical function for linear search
     if x <= 0:
          return None
     return x
def ins(x): #the mathematical function for insertion sort
     if x <= 0:
          return None
     return log(x)
def sel(x): # the mathematical function for slection sort
     if x <= 0:
          return None
     return log(x) - 1
def squared(x): #mathematical function for bubble sort
     if x<= 0:
          return None
     return x**2
def opti_squared(x): #mathematical function for optimized bubble sort
     if x<= 0:
          return None
     return 2**x

def square_root(x): # mathematical function for binary seach
     if x<= 0:
          return None
     return sqrt(x)

def plot_results_menu():
     m = ['Linear Search', 'Binary Search', 'Bubble Sort', 'Optimized Bubble Sort','Selection Sort', 'Insertion Sort']
     (draw_axes, plot_point, plot_function, put_text, destroy, mainloop) = \
                 plotter.plot(title='Linear Search Plot',
                              origin_x=0, origin_y=0,
                              bg='tomato')
     while True:#keeps the menu going until the user decides to stop
          c = menu.do_menu("Plot Results Menu",m)
          if c is None:
               break
          print("\nValid choice:", c)
          
          if c == 1: #choice for optimized bubble sort
               min_val = int(input("Choose a minimum value for your list: "))
               max_val = int(input("Choose a maximum value for your list: "))
               size = int(input("Choose a size for your list(minimum 100): "))
               aList = list_maker.ordered_ascending_list(min_val,max_val,size) #creates a list
               data_files_maker.data_maker_lin(aList) #appends the list to a text file
               lin_search = open("linear_search.txt", 'r')
               count = 0
               draw_axes(tick_length=8, colour='goldenrod1')
               for line in lin_search.readlines():
                    plot_point(x=count, y=int(line), diam=6, colour='blue')
                    count +=1
               plot_function(lin, point_diam=4, colour='SeaGreen1')
               for i in range(1,20):
                    put_text(i, x=.25, y=i, colour='yellow')
               for i in range(1,20):
                    put_text(i, x=i, y = 0.20, colour = 'yellow')
               mainloop()
         
               
               
          if c == 2: #choice for binary search
               min_val = int(input("Choose a minimum value for your list: "))
               max_val = int(input("Choose a maximum value for your list: "))
               size = int(input("Choose a size for your list(minimum 100): "))
               aList = list_maker.ordered_ascending_list(min_val,max_val,size)
               data_files_maker.data_maker_binary(aList)
               bin_search = open("binary_search.txt", 'r')
               count = 0
               draw_axes(tick_length=8, colour='goldenrod1')
               for line in bin_search.readlines():
                    plot_point(x=count, y=int(line), diam=6, colour='blue')
                    count +=1
               plot_function(square_root, point_diam=4, colour='SeaGreen1')
               for i in range(1,20):
                    put_text(i, x=.25, y=i, colour='yellow')
               for i in range(1,20):
                    put_text(i, x=i, y = 0.20, colour = 'yellow')
               mainloop()
               
          if c == 3: #choice for bubble sort
               min_val = int(input("Choose a minimum value for your list: "))
               max_val = int(input("Choose a maximum value for your list: "))
               size = int(input("Choose a size for your list(minimum 100): "))
               aList = list_maker.unordered_int_list(min_val,max_val,size)
               data_files_maker.data_maker_bubble(aList)
               bubble_sort = open("bubble_sort.txt", 'r')
               count = 0
               draw_axes(tick_length=8, colour='goldenrod1')
               for line in bubble_sort.readlines():
                    plot_point(x=count, y=int(line), diam=6, colour='blue')
                    count +=1
               plot_function(squared, point_diam=4, colour='SeaGreen1')
               for i in range(1,20):
                    put_text(i, x=.25, y=i, colour='yellow')
               for i in range(1,20):
                    put_text(i, x=i, y = 0.20, colour = 'yellow')
               mainloop()
               

          if c == 4: #choice for optimized bubble sort
               min_val = int(input("Choose a minimum value for your list: "))
               max_val = int(input("Choose a maximum value for your list: "))
               size = int(input("Choose a size for your list(minimum 100): "))
               aList = list_maker.unordered_int_list(min_val,max_val,size)
               data_files_maker.data_maker_bubble_opt(aList)
               bubble_sort_opt = open("optimized_bubble_sort.txt", 'r')
               count = 0
               draw_axes(tick_length=8, colour='goldenrod1')
               for line in bubble_sort_opt.readlines():
                    plot_point(x=count, y=int(line), diam=6, colour='blue')
                    count +=1
               plot_function(opti_squared, point_diam=4, colour='SeaGreen1')
               for i in range(1,20):
                    put_text(i, x=.25, y=i, colour='yellow')
               for i in range(1,20):
                    put_text(i, x=i, y = 0.20, colour = 'yellow')
               mainloop()

          if c == 5: #choice for selection sort
               min_val = int(input("Choose a minimum value for your list: "))
               max_val = int(input("Choose a maximum value for your list: "))
               size = int(input("Choose a size for your list(minimum 100): "))
               aList = list_maker.unordered_int_list(min_val,max_val,size)
               data_files_maker.data_maker_selection(aList)
               selection_sort = open("selection_sort.txt", 'r')
               count = 0
               draw_axes(tick_length=8, colour='goldenrod1')
               for line in selection_sort.readlines():
                    plot_point(x=count, y=int(line), diam=6, colour='blue')
                    count +=1
               plot_function(sel, point_diam=4, colour='SeaGreen1')
               for i in range(1,20):
                    put_text(i, x=.25, y=i, colour='yellow')
               for i in range(1,20):
                    put_text(i, x=i, y = 0.20, colour = 'yellow')
               mainloop()

          if c ==6: #choice for insertion sort
               min_val = int(input("Choose a minimum value for your list: "))
               max_val = int(input("Choose a maximum value for your list: "))
               size = int(input("Choose a size for your list(minimum 100): "))
               aList = list_maker.unordered_int_list(min_val,max_val,size)
               data_files_maker.data_maker_insertion(aList)
               insertion_sort = open("insertion_sort.txt", 'r')
               count = 0
               draw_axes(tick_length=8, colour='goldenrod1')
               for line in insertion_sort.readlines():
                    plot_point(x=count, y=int(line), diam=6, colour='blue')
                    count +=1
               plot_function(ins, point_diam=4, colour='SeaGreen1')
               for i in range(1,20):
                    put_text(i, x=.25, y=i, colour='yellow')
               for i in range(1,20):
                    put_text(i, x=i, y = 0.20, colour = 'yellow')
               mainloop()
               
          if c == None:
               break
          
plot_results_menu()
