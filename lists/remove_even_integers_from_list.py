#!/usr/bin/python

"""
- Author : Kishore D
- Info   : Remove Even Integers from List
            * python
"""

"""
Simple Solution
Complexity : Time = O(n), Space = O(n)
"""
def remove_even(lst):
  output = []

  for elem in lst:
      # If the reminder is not zero, add the element to output list
      if(elem % 2 != 0):
        output.append(elem)
    
  return output


"""
Using List Comprehension
Complexity : Time = O(n), Space = O(n)
"""
def remove_even_using_list_comprehension(lst):
  # [expression(i) for i in oldList if filter(i)]
  return [number for number in lst if number % 2 != 0]


if __name__ == "__main__":
  list1 = [125, -171, -34, 13, 195, 58, -1, -2, -161, -4, 11]
  print(remove_even(list1))
  print(remove_even_using_list_comprehension(list1))
  
"""
OUTPUT:
[125, -171, 13, 195, -1, -161, 11]
[125, -171, 13, 195, -1, -161, 11]
"""
