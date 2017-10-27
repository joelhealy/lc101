#  Write a course_grader function that takes a list of test scores as its
#  parameter. It will add up these test scores and calculate an average score.
#  It should then return a message of "pass" or "fail" depending on these two
#  conditions:
#
#     If the average score is greater than or equal to 70 and no single test
#     score is below 50, then return a message of "pass".
#     If the average score is lower than 70 or at least one test score is
#     below 50, then return a message of "fail".


def average(seq):
    """Return the average of the values in <seq>"""

    total = 0
    for n in seq:
        total += n
    return total / len(seq)


def any_below_50(seq):
    """Are any of the elements in <seq> less than 50?"""
    result = False
    for s in seq:
        if s < 50:
            result = True
    return result


def course_grader(test_scores):
    """Average test score >= 70 and no score below 50 earns a passing grade"""

    grade = 'pass'
    if average(test_scores) < 70 or any_below_50(test_scores):
        grade = 'fail'
    return grade


def main():
    print(course_grader([100, 75, 45]))     # "fail"
    print(course_grader([100, 70, 85]))     # "pass"
    print(course_grader([80, 60, 60]))      # "fail"
    print(course_grader([80, 80, 90, 30, 80]))  # "fail"
    print(course_grader([70, 70, 70, 70, 70]))  # "pass"


if __name__ == "__main__":
    main()
