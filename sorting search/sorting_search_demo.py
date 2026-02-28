import arrays
import random
import time

"""Function for insertion sort to be applied on an array with user defined size, containing randomly generated values """
def generate_sorted_data(size):
    array = arrays.Array(size)                                      # Creating array of user input size
    for i in range(size):
       array[i] = random.randint(1, 100)                           # Inserting random generated values into the array
    print ("Original Array (Insertion Sort):",array)

    for i in range(1, len(array)):
       j = array[i]                                                # Current element to be placed in the sorted section
       position = i                                                # Temporary variable that keeps track of where 'j' should go

       while position > 0 and array[position - 1] > j:             #Shifting elements to the right
           array[position] = array[position - 1]
           position -= 1

       array[position] = j                                         # Place 'j' at the correct position

    return array 

#Function call
size = int(input("Enter the size of the array: "))
sorted_array = generate_sorted_data(size)
print("Sorted Array (Insertion Sort):",sorted_array)

""""Binary search function"""
def binary_search(sorted_array, target):
    left = 0
    right = len(sorted_array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_array[mid] == target:
            return mid  # Target found, return index
        elif sorted_array[mid] < target:
            left = mid + 1  # Move to the right half
        else:
            right = mid - 1  # Move to the left half
            
    return None  # Target not found

"""Calling the function with sample targets"""
target = 29
result = binary_search(sorted_array, target)
if result is not None:
    print(f"Target {target} found at index: {result}")
else:
    print(f"Target {target} not found: NONE")

target = 100
result = binary_search(sorted_array, target)

if result is not None:
    print(f"Target {target} found at index: {result}")
else:
    print(f"Target {target} not found: NONE")


""" This code uses mergesort method to sort through a randomized array from 1-100 consisting of 10 integers"""

import array as arr


#Generates an array of random integers

def generate_random_data(size):
    data = arr.array('i', [random.randint(1, 100) for i in range(size)])
    return data

    
#Merge sort method is used where two  halves of an array are sorted then merged

def merge_sort(arr):
    def merge_sort2(arr, left, right):
        # Base case: if the array has one element, it is already sorted
        if left >= right:
            return 0
        
        else:
            #Find the midpoint to split the array
            mid = (left + right) // 2
            #Recursively sort the left half
            merge_sort2(arr, left, mid)
            # Recursively sort the right half
            merge_sort2(arr, mid + 1, right)
            # Merge the sorted halves
            merge(arr, left, mid, right)
    
    merge_sort2(arr, 0, len(arr) - 1)
    return arr

def merge(arr, left, mid, right):
    #Create temporary arrays for the left and right halves
    left_half = arr[left:mid + 1]
    right_half = arr[mid + 1:right + 1]

    i = j = 0 #Pointers for left_half and right_half
    k = left #Pointer for main array
#Merge the two halves back into the main array
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
#Copy any remaining elements from left_half 
    while i < len(left_half):
        arr[k] = left_half[i]
        i = i + 1
        k = k + 1
#Copy any remaining elements from right_half 
    while j < len(right_half):
        arr[k] = right_half[j]
        j = j + 1
        k = k + 1


#generate an array of 10 random integers
randomlist = generate_random_data(10)
print("Original array (Merge Sort):", list(randomlist)) #convert to list for printing
#perform merge sort on a copy of the random array
sorted_data_merge = merge_sort(randomlist[:])  
print("Sorted array (Merge Sort):", list(sorted_data_merge))#convert to list for printing


""": Search Performance Comparison
This phase compares the merge sort sorted data using linear and binary search"""

#Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None

#Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

target = 72  #target as mentioned 
sorted_data_merge = merge_sort(randomlist[:])  #data from phase 3

#measure time for linear search
start_time = time.perf_counter()
linear_result = linear_search(sorted_data_merge, target)
linear_search_time = time.perf_counter() - start_time

#measure time for binary search
start_time = time.perf_counter()
binary_result = binary_search(sorted_data_merge, target)
binary_search_time = time.perf_counter() - start_time

#results
print(f"Linear search time: {linear_search_time:} seconds, Result: {linear_result}")
print(f"Binary search time: {binary_search_time:} seconds, Result: {binary_result}")
print("Binary search > Linear search")

"""
ADDITIONAL QUESTION REFLECTION
The sorting algorithm you choose really impacts how quick searches work, 
binary needs sorted data and is very quick on big data sets with O(logn), 
while linear is slower at O(n) especially if the data grows in size.
merge sort is quicker with O(nlogn) help binary search to work 
more efficiently but slower sorts like insertion with O(n^2) adds delays and 
slows the overall performance. biary search is faster and more efficient compare to linear.
"""