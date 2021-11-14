#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# first make the function to store the last value of tuple.
# make  another function for sorting the value.


def last(num):
    return num[-1]
def sort(my_list_num):
    return sorted(my_list_num, key=last)

my_list_num= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("sorted_num:") 
print sorted(my_list_num)


# In[ ]:




