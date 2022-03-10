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
    self._len = 0
    
  def get_head(self):
    return self._head
  
  def set_head(self, node):
    self._head = node

  def is_empty(self):
    # return True if self._len == 0 else False
    return True if self.get_head() is None else False
  
  def get_length(self):
    return self._len
  
  def incr_length(self):
    self._len += 1
    
  def insert_node(self, data, pos):
    newNode = Node(data)

    if self.is_empty() or pos == 1:
      newNode.set_next_node(self.get_head())
      self.set_head(newNode)
      self.incr_length()
      return
    
    if pos > self.get_length():
      pos = self.get_length()
    
    current_node = self.get_head()
    for i in range(pos-2):
      current_node = current_node.get_next_node()

    newNode.set_next_node(current_node.get_next_node())
    current_node.set_next_node(newNode)
    self.incr_length()     
