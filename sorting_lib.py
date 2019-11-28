## Counting Sort Algorithm

import pandas as pd
import numpy as np


def countingsort (Istr):
    # Creating a Auxilary Dataframe
    index = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    columns = ['Value']
    df = pd.DataFrame(index = index, columns = columns).fillna(0)

    # Array
    # String entered for Input
    Istr = Istr.lower()   # Making it on a  lower case

    # Creating frequency Table of array on Auxilary Dat frame

    for i in Istr:       # Substituing the count of alphabets (index) in the Value Column
        df.at[i, 'Value']+=1    # adding up the count of alphabets from INPUT String in the Dataframe

    # sorted Dataframe
    filtnonzero = df.Value > 0
    fdf = df[filtnonzero]  # Dataframe for INPUT STRINGs only

    # Result

    Ostr = []
    for l in range (len(fdf)): # length will be the index of Sorted dataframe
        z = fdf.iloc[l][0]
        for m in range (z):
            Ostr.append(fdf.index[l])

    ## Output
    out = ("".join(Ostr))
    return(out)

#_______________________________________________________________
#_______________________________________________________________

def c_sort(arr): #counting Sort
    
    # Creating Auxillary Dataframe for frequency and Commulative frequency
    
    AUXarrindex = ['Frequency', 'Commulative'] #
    Auxarrcolumns = [i for i in range (97,123)]
    Auxarrdf = (pd.DataFrame(index = AUXarrindex, columns = Auxarrcolumns)).fillna(0)
    
    # inserting Commulative Frequency

    for i in arr:   
        Auxarrdf.at['Frequency', i]+=1 
        
    # inserting Commulative Frequency
    
    Auxarrdf.loc['Commulative'] = Auxarrdf.loc['Frequency'].values.cumsum()
    
    # creating a Sorted Dataframe-- pertaining the Sorting and order of Input array
    
    sorteddfind = ["Sorted", "order"]
    sorteddfcol = [c for c in range (0,len(arr))]
    Sorted_df = (pd.DataFrame(index = sorteddfind , columns = sorteddfcol)).fillna(0)
    
    # Inserting sorting from Auxillary Dataframe [Commulative Frequency]
    
    for i,a in enumerate (arr):    
        (Sorted_df.iloc[0][(Auxarrdf.iloc[1][a])-1]) = a
        (Sorted_df.iloc[1][(Auxarrdf.iloc[1][a])-1]) = i
        Auxarrdf.iloc[1][a] = (Auxarrdf.iloc[1][a])-1
        
    # returning the output
    
    return list(Sorted_df.loc['Sorted'].values), list(Sorted_df.loc['order'].values)


##_______________________________________________________________________________
##_______________________________________________________________________________

def alphabetical_sort(Inpstr):
    n = len(max(Inpstr, key=len))# maximum length of the word in a string
    #print(n)
    m = len(Inpstr)
    #print(m)
    df = np.zeros((m,n+1), dtype=int) # dataset in addition of a column for index
    df[:,0] = range(m) # inserint Index of Words
    #print(df)

    for s in range (0,m): # inserting Words in the dataset
        t = len(Inpstr[s])
        for l in range (0,t):
            df[s][l+1] = (ord(str((Inpstr[s])[l])))
    #print(df)
   
    pre_problems = list([list(range(m))]) #Max times of problem
    #print(pre_problems)
    # dividing problem into Sub problems
    
    for i in range(1,n):
        problems = list() #considering the column
        #print (problems)
        for curr_problem in pre_problems:
            #print (curr_problem)
            sorted_arrays, sorted_order = c_sort(df[curr_problem,i])
            df[curr_problem,:] = df[curr_problem,:][sorted_order,:]
            target_ind = list(range(len(sorted_arrays)))
            problems_list = list()
            new_problem = [curr_problem[0]]
            for j in range(1,len(sorted_arrays)):
                if sorted_arrays[j] == sorted_arrays[j-1]:
                    new_problem.append(target_ind[j])
                else:
                    if len(new_problem) > 1:
                        problems_list.append(new_problem)
                    new_problem = [target_ind[j]]
            if len(new_problem) > 1:
                problems_list.append(new_problem)
            problems = problems + problems_list
        pre_problems = problems
    return [Inpstr[i] for i in list(df[:,0])]