print ("List Remove Duplicates (using sets) \n")
print ("Source: http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html \n")
# Exercise 14 (and Solution)
# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
# Extras:
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.
def gen_list():
  list1=random.choices(range(1,31), k=random.randint(1,20))
  return list1
import random

def unique_list_loop(in_list):
  out_list = []
  for element in in_list:
    if element not in out_list:
      out_list.append(element)
  return out_list

def unique_list_sets(in_list):
  out_list=list(set(in_list))
  return out_list

def common_elements(list1, list2):
  set1 = set(list1)
  set2 = set(list2)
  common = list(set1.intersection(set2))
  return common

a = gen_list()
b = unique_list_loop(a)
c = unique_list_sets(a)
d = gen_list()
e = common_elements(a, b)
print("Original list: ", a,"\n")
print("List cleaned of duplicates by loop method: ",b, "\n")
print("List cleaned of duplicates by set method: ",c, "\n\n")
print ("Two lists for common elements: \n", a, "\n", d, "\n")
print("List of common elements: ",e, "\n")
