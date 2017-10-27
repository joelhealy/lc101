#  Write a program that will function as a grade book, allowing a user (a
#  professor or teacher) to enter the class roster for a course, along with
#  each student’s cumulative grade. It then prints the class roster along with
#  the average cumulative grade. Grades are on a 0-100 percentage scale. Use 2
#  lists (grades and students) and the enumerate function in your solution.
#
#  Implement the functionality of the above program using a dictionary instead
#  of a list.
#
#  A test run of this program would yield the following:
#
#  # this is the first batch of input the user would enter
#  Chris
#  Jesse
#  Sally
#
#  # this is the second batch of input the user would enter
#  Grade for Chris: 90
#  Grade for Jesse: 80
#  Grade for Sally: 70
#
#  # below is what your program should output
#  Class roster:
#  Chris (90.0)
#  Jesse (80.0)
#  Sally (70.0)
#
#  Average grade: 80.0


def print_gradebook(gradebook):
    total = 0
    print("Class roster:")
    for student, grade in gradebook.items():
        print("{0} ({1:.1f})".format(student, grade))
        total += grade
    print("Average grade:", total / len(gradebook))


def testEqual(a, b):
    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of print_gradebook(gradebook) """

    gradebook = {"Chris": 90, "Jesse": 80, "Sally": 70}
    print_gradebook(gradebook)


if __name__ == "__main__":
    main()
