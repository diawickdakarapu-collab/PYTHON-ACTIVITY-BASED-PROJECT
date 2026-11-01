print("COURIER CHARGE OPTIMIZATION")

weight = float(input("Enter parcel weight in kg: "))
distance = float(input("Enter delivery distance in km: "))

if weight <= 0 or distance <= 0:
    print("Invalid parcel details")

else:
    print("\nDELIVERY TYPE")
    print("1. Normal")
    print("2. Express")

    choice = int(input("Enter delivery type: "))

    if choice == 1:
        extra = 0
    elif choice == 2:
        extra = 100
    else:
        extra = -1

    if extra == -1:
        print("Invalid delivery type")

    else:
        services = ["Courier A", "Courier B", "Courier C"]
        base_rates = [40, 50, 35]
        weight_rates = [20, 15, 25]
        distance_rates = [2, 3, 1.5]
        max_weights = [10, 20, 5]

        charges = []

        for i in range(len(services)):

            if weight <= max_weights[i]:

                charge = (base_rates[i] +
                          weight * weight_rates[i] +
                          distance * distance_rates[i] +
                          extra)

                charges.append(charge)

                print("\n", services[i])
                print("Courier Charge: Rs.", round(charge, 2))

            else:
                charges.append(-1)
                print("\n", services[i], "Not Eligible")

        minimum = -1
        best_service = ""

        for i in range(len(charges)):

            if charges[i] != -1:

                if minimum == -1 or charges[i] < minimum:
                    minimum = charges[i]
                    best_service = services[i]

        print("\nBEST COURIER SERVICE")

        if minimum == -1:
            print("No eligible courier service available")
        else:
            print("Service:", best_service)
            print("Minimum Charge: Rs.", round(minimum, 2))
