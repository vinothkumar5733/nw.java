# """Basic Python tuple examples."""

# # Creating tuples
# empty = ()
# single_item = ("apple",)  # The comma makes this a tuple.
# fruits = ("apple", "banana", "cherry")

# # Tuple packing and unpacking
# point = 3, 5
# x, y = point

# # Accessing items and slicing
# first_fruit = fruits[0]
# last_two_fruits = fruits[1:]

# # Tuples are immutable; use a new tuple to add an item.
# more_fruits = fruits + ("orange",)

# # Useful tuple methods
# fruit_count = fruits.count("apple")
# banana_index = fruits.index("banana")

print(fruits)
print(f"Point: ({x}, {y})")
print(last_two_fruits)
print(more_fruits)