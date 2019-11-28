from sorting_lib import countingsort, c_sort, alphabetical_sort
import pandas as pd
import numpy as np


## 1. Algorithm of Counting Sort is available in Sorting_lib.py


## 2. Alphabetic String Sorting

strinput = input("Enter a string of alphabets :")
d = countingsort(strinput)
print ("Sorted string is: ",d)


## 3. String Words Sorting

Inpstr = []
Inpstr = input(" Enter the string (non nemeric words) :").lower().split()
print ("Sorted word in this string are :",alphabetical_sort(Inpstr))


