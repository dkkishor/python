#!/usr/bin/python

'''
- Author : Kishore D
- Info   : Class definition of a Node in a Linked List
            * python
'''

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None # pointer to the next Node
  
  def get_next_node(self):
    return self.next
