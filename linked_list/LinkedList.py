#!/usr/bin/python

"""
- Author : Kishore D
- Info   : Create a LinkedList class and its methods
            * python
"""

import Node from Node

class LinkedList:
  def __init__(self):
    self._head = None
    
  def get_head(self):
    return self._head
  
  def is_empty(self):
    return [True if self._head is None else False]
  
  def insert_at_head(self, data):
    newNode = Node(Data)
    newNode.set_next_node(self._head)
    self._head = newNode
      
  def insert_at_tail(self, data):
    newNode = Node(data)

    if (is_empty()):
      self._head = newNode
    else:
      current = self._head
      next = self._head.get_next_node()
      
      while next is not None:
        current = next
        next = next.get_next_node()
      
      current.next = node
      
        
      
