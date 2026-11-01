print("DISASTER RELIEF SUPPLY ALLOCATION")

areas = ["Area A", "Area B", "Area C", "Area D"]

# Required relief kits
demand = [100, 150, 80, 120]

# Priority: 1 = High, 2 = Medium, 3 = Low
priority = [2, 1, 3, 1]

available_stock = int(input("Enter total available relief kits: "))

allocated = [0, 0, 0, 0]
remaining = [0, 0, 0, 0]

print("\nRELIEF SUPPLY ALLOCATION")

# Allocate supplies according to priority
for p in range(1, 4):

    for i in range(len(areas)):

        if priority[i] == p:

            if available_stock >= demand[i]:

                allocated[i] = demand[i]
                available_stock -= demand[i]

            else:

                allocated[i] = available_stock
                available_stock = 0

            remaining[i] = demand[i] - allocated[i]

print("\nFINAL ALLOCATION REPORT")

for i in range(len(areas)):

    print("\nArea:", areas[i])
    print("Priority:", priority[i])
    print("Required Kits:", demand[i])
    print("Allocated Kits:", allocated[i])
    print("Unmet Demand:", remaining[i])

print("\nTOTAL SUMMARY")

total_demand = sum(demand)
total_allocated = sum(allocated)
total_unmet = sum(remaining)

print("Total Demand:", total_demand)
print("Total Allocated:", total_allocated)
print("Total Unmet Demand:", total_unmet)
print("Remaining Stock:", available_stock)

if total_unmet == 0:
    print("All areas received required supplies")
else:
    print("Some areas still require relief supplies")
