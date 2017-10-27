#  The following sample file called studentdata.txt contains one line for each
#  student in an imaginary class. The student’s name is the first thing on each
#  line, followed by some exam scores. The number of scores might be different
#  for each student.
#
#  joe 10 15 20 30 40
#  bill 23 16 19 22
#  sue 8 22 17 14 32 17 24 21 2 9 11 17
#  grace 12 28 21 45 26 10
#  john 14 32 25 16 89
#
#  Using the text file studentdata.txt write a program that prints out the
#  names of students that have more than six quiz scores.


def average(lst):
    return sum(lst) / len(lst)


def main():
    file_ref = open('w:\lc101\Hacker Chapter - Files\studentdata.txt', 'r')
    line = file_ref.readline()
    while line:
        words = line.split()
        exam_score_count = len(words) - 1  # Don't count student name
        if exam_score_count >= 1:
            student = words[0]
            exam_scores = [int(word) for word in words[1:]]
            average_grade = average(exam_scores)
            print("Student: {} - Avg Grade: {:.1f}".format(student,
                                                           average_grade))
        line = file_ref.readline()
    file_ref.close()


if __name__ == "__main__":
    main()
