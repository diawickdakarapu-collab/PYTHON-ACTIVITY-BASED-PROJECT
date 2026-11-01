print("ENERGY CONSERVATION ANALYSIS")

appliances = ["Fan", "Light", "AC", "TV"]

before = [120, 80, 300, 100]
after = [90, 50, 220, 85]

total_before = 0
total_after = 0

print("\nAPPLIANCE-WISE ANALYSIS")

for i in range(len(appliances)):
    saving = before[i] - after[i]

    percentage = (saving / before[i]) * 100

    total_before += before[i]
    total_after += after[i]

    print("\nAppliance:", appliances[i])
    print("Before:", before[i], "units")
    print("After:", after[i], "units")
    print("Saving:", saving, "units")
    print("Saving Percentage:", round(percentage, 2), "%")

total_saving = total_before - total_after

saving_percentage = (total_saving / total_before) * 100

print("\nTOTAL ANALYSIS")
print("Total Before:", total_before, "units")
print("Total After:", total_after, "units")
print("Total Saving:", total_saving, "units")
print("Overall Saving:", round(saving_percentage, 2), "%")

if total_saving > 0:
    print("Energy Conservation Successful")
else:
    print("No Energy Savings")
