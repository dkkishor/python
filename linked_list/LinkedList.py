#!/usr/bin/python

"""
- Author : Kishore D
- Info   : Create a LinkedList class and its methods
            * python
"""

import Node from Node

class LinkedList:
  def __init__(self):
    self.head = None
    
  def get_head(self):
    return self.head
  
  def is_empty(self):
    return [True if self.head is None else False]
  
  def insert_at_head(self, node):
    if (is_empty()):
      self.head = Node
    else:
      node.next = self.head
      self.head = node
      
  def insert_at_tail(self, node):
    if (is_empty()):
      self.head = node
    else:
      current = self.head
      next = self.head.get_next_node()
      
      while next is not None:
        current = next
        next = next.get_next_node()
      
      current.next = node
      
        
      
