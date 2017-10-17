#  A student has a name and student ID number. A student can record grades
#  and will track how many credits they have taken as well as their GPA.
#  A student can also report what their class standing is (Freshman,
#  Sophomore, Junior, Senior, Graduated) based on the number of credits they
#  have taken.


class Student():

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grades = []

    def record_grade(self, grade, credit_hrs):
        self.grades.append((grade, credit_hrs))

    def report_credits(self):
        total_credits = 0
        for grade in self.grades:
            total_credits += grade[1]
        return total_credits

    def report_gpa(self):
        total_credits = 0
        weighted_grade = 0
        for grade in self.grades:
            total_credits += grade[1]
            weighted_grade += grade[0] * grade[1]
        if total_credits > 0:
            gpa = weighted_grade / total_credits
        else:
            gpa = 0.0
        return gpa

    def __repr__(self):
        __repr = '{"_Student__name": "' + \
                 str(self.name) + '",' + \
                 ' "_Student__id": "' + \
                 str(self.id) + '",' + \
                 ' "_Student__grades": ' + \
                 str(self.grades) + \
                 '}'
        return __repr


def my_test_equal(a, b):
    """ Home-rolled version of testEqual(a, b) """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of Baseball_player Class """

    s1 = Student("Albert Einstein", "AE123456789")
    s2 = Student("Barney Miller", "BM2468013579")
    print(s1)
    print(s2)
    s1.record_grade(3.0, 3)
    s1.record_grade(3.5, 2)
    s1.record_grade(4.0, 3)
    print(s1)
    my_test_equal(s1.report_credits(), 8)
    my_test_equal(s1.report_gpa(), 3.5)


if __name__ == "__main__":
    main()
