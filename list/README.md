# List
* data structures that group sequences of elements
* can have elements of several types
* can also mix different types within the same list

### Accessing elements of List
```
list1 = [1, 2, 3, 4]
list2 = [8, 9]

print(list2)
8
9

print(list1 + list2)
1
2
3
4
8
9

print(list1[0:3])
1
2
3
```

### Iterating over list

#### for loop
```
for elem in list1:
  print(elem)
```

```
for i in range(len(list1)):
  print(list1[i])
```
#### while loop
```
i = 0
while i < len(list1):
  print(list1[i])
  i += 1
```

#### list comprehension
```
[print(x) for x in list1]
```
