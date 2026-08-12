'''6. Write a program to illustrate the use of tuples 
and sets with basic operations. '''

tuple = (10, 50, 30, 110, 60, 80, 56, 99, 10)

print("Tuple:", tuple)
print()

print("Maximum:", max(tuple))
print("Minimum:", min(tuple))
print("Length:", len(tuple))
print("Sorted Tuple:", sorted(tuple))
print("Sum:", sum(tuple))
print("Count of 10:", tuple.count(10))
print("Index of 60:", tuple.index(60))
print("Any:", any(tuple))
print()

# Set Operations
set1 = {10, 50, 30, 110, 60, 80, 56, 99, 10}

print()
print("Set:", set1)

set1.add(200)
print("After adding 200:", set1)

set1.remove(110)
print("After removing 110:", set1)

set1.discard(500)
print("After discard 500:", set1)

# Another Set
set2 = {10, 20, 30, 40, 50}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))