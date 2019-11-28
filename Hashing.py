#!/usr/bin/env python
# coding: utf-8

import pandas as pd,numpy as np
import math,time

# Reading the file
with open('passwords1.txt','r') as f:
    lines = f.readlines()
    f.close()


# Removing the "\n"s
for i in range(len(lines)):
    lines[i] = lines[i].strip().split('\n')[0]


# making a data frame
pws = pd.DataFrame(lines)


p = 0.09 # prob. of False possitive
n = 100_000_000 # Number of all passwords1
m = round((-(n*math.log(p))/((math.log(2))**2))) # The length of our Bloom filter
k = round((m/n)*(math.log(2)))    # Number of hash functions needed


# Creating an empty bloomfilter(with 0 as a default value)
hash_table = np.zeros(m, dtype = int)


# Hash functions
def hash_func1(s):
    hash = 0
    for i in range(len(s)-1,-1,-1):
        hash += ord(s[i]) * pow(10,i)
    return hash % m

def hash_func2(s):
    hash = 0
    for i in range(len(s)-1,-1,-1):
        ascii_code = ord(s[i])
        hash = 128 * hash + ascii_code
    return hash % m

def hash_func3(s):
    hash = 0
    for i in range(len(s)-1,-1,-1):
        hash += ord(s[i]) * pow(5,i)
    return hash % m      
        

# Here we update the bloom filter by the index we got from hash functions
def hash_table_update():
    for _ in pws[0]:
        res1 = hash_func1(_)
        res2 = hash_func2(_)
        res3 = hash_func3(_)
        
        if hash_table[res1] != 1:
            hash_table[res1] = 1
            
        if hash_table[res2] != 1:
            hash_table[res2] = 1
            
        if hash_table[res3] != 1:
            hash_table[res3] = 1


# Now we need the 2nd dataset to chech the duplicates
with open('passwords2.txt','r') as f2:
    lines2 = f2.readlines()
    f2.close()


for i in range(len(lines2)):
    lines2[i] = lines2[i].strip().split('\n')[0]


pws2 = pd.DataFrame(lines2)


# Here we calculate the number of duplicate passwords we have
def duplicates():
    N = 0
    for _ in pws2[0]:
        res2_1 = hash_func1(_)
        res2_2 = hash_func2(_)
        res2_3 = hash_func3(_)
        if hash_table[res2_1] == 1 and hash_table[res2_2] == 1 and hash_table[res2_3] == 1:
            N += 1
    return N


# The final function for this task



def BloomFilter():
    start = time.time()
    
    hash_table_update()
    n = duplicates()
    
    
    end = time.time()
    
    print('Number of hash function used: ', k)
    print('Number of duplicates detected: ', n)
    print('Probability of false positives: ', p)
    print('Execution time: ', end-start)
    

BloomFilter()

