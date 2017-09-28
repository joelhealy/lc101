#  Starting with the list in Exercise 2, write Python statements to do the
#  following:

l = [76, 92.3, 'hello', True, 4, 76]
print("Prior to a) l =", l)

#   a. Append “apple” and 76 to the list.

l += ["apple", 76]
print("After a) l =", l)

#   b. Insert the value “cat” at position 3.

# l.insert(3, "cat")
l[3:3] = ["cat"]
print("After b) l =", l)

#   c. Insert the value 99 at the start of the list.

# l.insert(0, 99)
l[0:0] = [99]
print("After c) l =", l)

#   d. Find the index of “hello”.

print("The index of 'hello' is", l.index('hello'))

#   e. Count the number of 76s in the list.

print("The count of 76s in the list is", l.count(76))

#   f. Remove the first occurrence of 76 from the list.

l.remove(76)
print("After f) l =", l)

#   g. Remove True from the list using pop and index.

l.pop(l.index(True))
print("After g) l =", l)
