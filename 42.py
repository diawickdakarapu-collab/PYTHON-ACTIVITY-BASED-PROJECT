students = ["Akhil", "Bharath", "Charan", "Divya"]
subjects = ["Python", "Maths", "English"]

marks = [
    [85, 90, 78],
    [76, 82, 88],
    [92, 95, 89],
    [68, 74, 80]
]

print("STUDENT MARKS ANALYSIS")

for i in range(len(students)):
    total = sum(marks[i])
    average = total / len(subjects)

    print("\nStudent:", students[i])
    print("Marks:", marks[i])
    print("Total:", total)
    print("Average:", average)

print("\nSUBJECT-WISE AVERAGES")

for j in range(len(subjects)):
    total = 0

    for i in range(len(students)):
        total += marks[i][j]

    average = total / len(students)
    print(subjects[j], "Average:", average)

print("\nTOPPER")

highest = -1
topper = ""

for i in range(len(students)):
    total = sum(marks[i])

    if total > highest:
        highest = total
        topper = students[i]

print("Topper:", topper)
print("Highest Total:", highest)
