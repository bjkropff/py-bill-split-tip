#!/usr/bin/env python3.7.6
print("Welcome To The Bill Split Calculator")

total_bill=float(input("What is the total of the bill?: "))

tip_percent=int(input("What is the tip percentage to give?: "))

total_party=int(input("How many people are splitting?: "))

per_person=(round(float(((tip_percent / 100 +1) * total_bill) / total_party), 2))

print(f"For ${total_party} people,\n with a ${tip_percent}% tip,\n and a total bill of ${total_bill}\n the total per person cost is: ")
print(f"${per_person}")

