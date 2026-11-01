print("EMPLOYEE SHIFT CONFLICT DETECTION")

shifts = [
    ("E101", 9, 13),
    ("E102", 10, 14),
    ("E103", 14, 18),
    ("E104", 11, 15),
    ("E105", 16, 20)
]

print("\nEMPLOYEE SHIFT DETAILS")

for employee, start, end in shifts:
    print("Employee:", employee)
    print("Start Time:", start)
    print("End Time:", end)
    print()

print("SHIFT CONFLICTS")

conflicts = 0

for i in range(len(shifts)):
    for j in range(i + 1, len(shifts)):

        emp1, start1, end1 = shifts[i]
        emp2, start2, end2 = shifts[j]

        if start1 < end2 and start2 < end1:

            print(emp1, "and", emp2,
                  "have overlapping shifts")

            conflicts += 1

if conflicts == 0:
    print("No shift conflicts found")

print("\nTOTAL CONFLICTS:", conflicts)
