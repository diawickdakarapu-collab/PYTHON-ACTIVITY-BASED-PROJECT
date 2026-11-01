print("SMART PARKING FEE MANAGEMENT")

vehicles = {
    "car": 30,
    "bike": 15,
    "bus": 50
}

vehicle = input("Enter vehicle type (car/bike/bus): ").lower()

if vehicle not in vehicles:
    print("Invalid vehicle type")

else:
    entry_hour = int(input("Enter entry hour (0-23): "))
    entry_min = int(input("Enter entry minute (0-59): "))

    exit_hour = int(input("Enter exit hour (0-23): "))
    exit_min = int(input("Enter exit minute (0-59): "))

    if (entry_hour < 0 or entry_hour > 23 or
        exit_hour < 0 or exit_hour > 23 or
        entry_min < 0 or entry_min > 59 or
        exit_min < 0 or exit_min > 59):

        print("Invalid time")

    else:
        entry = entry_hour * 60 + entry_min
        exit = exit_hour * 60 + exit_min

        if exit <= entry:
            exit += 24 * 60

        duration = exit - entry
        hours = (duration + 59) // 60

        rate = vehicles[vehicle]
        amount = hours * rate

        if hours > 12:
            amount += 100

        print("\nPARKING BILL")
        print("Vehicle:", vehicle)
        print("Parking Duration:", hours, "hours")
        print("Hourly Rate:", rate)
        print("Total Amount: Rs.", amount)
