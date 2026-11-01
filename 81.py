print("CAMPUS EVENT SEATING AND ENTRY VALIDATION")

seats = [
    [None, None, "RESERVED", None],
    [None, None, None, None],
    [None, "RESERVED", None, None]
]

registered_students = ["S101", "S102", "S103", "S104",
                       "S105", "S106", "S107", "S108"]

entered_students = []
allocated = 0

print("\nSEATING ALLOCATION")

for student in registered_students:
    found = False

    for i in range(len(seats)):
        for j in range(len(seats[i])):

            if seats[i][j] is None:
                seats[i][j] = student
                print(student, "allocated to Row", i + 1,
                      "Seat", j + 1)

                allocated += 1
                found = True
                break

        if found:
            break

    if not found:
        print(student, "No seat available")

print("\nSEATING ARRANGEMENT")

for row in seats:
    print(row)

print("\nENTRY VALIDATION")

number = int(input("Enter number of students entering: "))

for i in range(number):
    ticket = input("Enter student ticket ID: ")

    if ticket not in registered_students:
        print("Invalid Ticket")

    elif ticket in entered_students:
        print("Duplicate Entry")

    else:
        entered_students.append(ticket)
        print("Entry Successful")

print("\nEVENT SUMMARY")
print("Total Registered:", len(registered_students))
print("Total Allocated:", allocated)
print("Total Entered:", len(entered_students))

vacant = 0

for row in seats:
    for seat in row:
        if seat is None:
            vacant += 1

print("Vacant Seats:", vacant)
