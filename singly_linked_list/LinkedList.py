#!/usr/bin/python

"""
- Author : Kishore D
- Info   : Create a LinkedList class and its methods
            * python
"""

from Node import Node

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
    
  def print_list(self):
    if self.is_empty():
      print("List is empty")
      return
    
    node = self.get_head()
    tempStr = ""
    for i in range(self.get_length()):
      if i > 0 and i < self.get_length():
        tempStr += " -> "
      
      tempStr += str(node.get_data())
      node = node.get_next_node()

    print(tempStr)
      
  def insert_node(self, data, pos):
    newNode = Node(data)

    if self.is_empty() or pos == 1:
      newNode.set_next_node(self.get_head())
      self.set_head(newNode)
      self.incr_length()
      return
    
    if pos > self.get_length():
      pos = self.get_length() + 1
    
    current_node = self.get_head()
    for i in range(pos-2):
      current_node = current_node.get_next_node()

    newNode.set_next_node(current_node.get_next_node())
    current_node.set_next_node(newNode)
    self.incr_length()
