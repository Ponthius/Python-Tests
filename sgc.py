import statistics
def get_grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"
def get_remark(grade):
    if grade == "A":
        return "Excellent"
    elif grade == "B":
        return "Very Good"
    elif grade == "C":
        return "Good"
    elif grade == "D":
        return "Needs Improvement"
    else:
        return "Fail"
def main():
    name = input("Enter your name: ")

    marks = []

    for i in range(5):
        mark = int(input(f"Enter mark for subject {i + 1}: "))
        marks.append(mark)

    total = sum(marks)
    average = statistics.mean(marks)

    grade = get_grade(average)
    remark = get_remark(grade)

    print()
    print(f"Student: {name}")
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Grade: {grade}")
    print(f"Remark: {remark}")


main()
