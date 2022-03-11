# Linked List
* There is no Linked List data type
* can be implemented through Classes & Lists

## Singly Linked List

HEAD [Data | Pointer] --> NODE1 [Data | Pointer] --> NODE2 [Data | Pointer] --> ... --> TAIL [DATA | None]

* There is no backward pointer which makes it a Singly Linked List.
* Time Complexity at the head is O(1)

```
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None # Pointer to the next Node
```
```

class LinkedList:
  def __init__(self):
    self.head = None # Pointer to Head Node
  
  def get_head(self):
    return self.head
    
  def is_empty(self):
    return True if self.head is None else False
  
```
```
ll = LinkedList()
print(ll.is_empty())

Output:
True
```
