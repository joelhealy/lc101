# ------------------------------------------------------------------------------
#
#  Weekly Graded Assignment
#  (Taken from Chapter 6 of LaunchCode 101's version of Think Python)
#
#  A year is a leap year if it is divisible by 4, unless it is a century that
#  is not divisible by 400.
#
#  For example:
#
#     1956 is a leap year because 1956 is divisible by 4.
#     1957 is not a leap year, because it is not divisible by 4.
#     1900 is not a leap year, despite the fact that it is divisible by 4,
#          because 1900 is a century and 1900 is not divisible by 400.
#     1600 is a leap year, because 1600 is divisible by 4 and 1600 is
#          divisible by 400.
#
#  Write a function is_leap that takes a year as a parameter and returns
#  True if the year is a leap year, False otherwise.
#
# ------------------------------------------------------------------------------


def is_leap(year):
    is_leap_year = (year % 4 == 0)
    if (year % 100 == 0 and year % 400 != 0):
        is_leap_year = False
    return is_leap_year


print(is_leap(1944), True)
print(is_leap(2011), False)
print(is_leap(1986), False)
print(is_leap(1956), True)
print(is_leap(1957), False)
print(is_leap(1800), False)
print(is_leap(1900), False)
print(is_leap(1600), True)
print(is_leap(2056), True)
