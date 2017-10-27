
def grader(score):
    """Return the letter grade for a given test score"""

    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return grade


def main():
    print("A score of 100 gets a grade of", grader(100))
    print("A score of 90 gets a grade of", grader(90))
    print("A score of 89.99 gets a grade of", grader(89.99))
    print("A score of 85 gets a grade of", grader(85))
    print("A score of 80 gets a grade of", grader(80))
    print("A score of 79.99 gets a grade of", grader(79.99))
    print("A score of 75 gets a grade of", grader(75))
    print("A score of 70 gets a grade of", grader(70))
    print("A score of 69.99 gets a grade of", grader(69.99))
    print("A score of 60 gets a grade of", grader(60))
    print("A score of 59.99 gets a grade of", grader(59.99))
    print("A score of 30 gets a grade of", grader(30))


if __name__ == '__main__':
    main()
