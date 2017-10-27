# ------------------------------------------------------------------------------
#
#  Weekly Graded Assignment
#  (Taken from Chapter 4 of LaunchCode 101's version of Think Python)
#
#  Assume you have a list of numbers nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]
#
#      Write a loop that prints each of the numbers on a new line, like this:
#
#      12
#      10
#      ...etc
#
#      Write a second loop that prints each number and its square on a new
#      line, precisely like this:
#
#      The square of 12 is 144
#      The square of 10 is 100
#      ...etc
#
# ------------------------------------------------------------------------------

nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# print each of the numbers on a new line
for num in nums:
    print(num)

# print each number and its square on a new line
for num in nums:
    print('The square of', num, 'is', num**2)
