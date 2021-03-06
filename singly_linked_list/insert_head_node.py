#!/usr/bin/python

'''
- Author : Kishore D
- Info   : Inserting Node at the Head and printing the Linked List
            * python
'''

from LinkedList import LinkedList

if __name__ == "__main__":
  ll = LinkedList()

  '''
  First Parameter is Data.
  Second Parameter is Node position
  Node position is always 1 indicating Head Node.
  '''
  
  ll.insert_node(0, 1)
  ll.print_list()
  
  ll.insert_node(1, 1)
  ll.print_list()
  
  ll.insert_node(2, 1)
  ll.print_list()
  
'''
Output:
0
1 -> 0
2 -> 1 -> 0
'''
