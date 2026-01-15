names = ["Me", "Lia", "Jake"]

steps = [

  [4500, 5200, 4800, 5000, 5300],

  [4000, 4100, 3900, 4200, 4600],

  [6000, 5800, 5900, 6100, 6200]

]

total_steps = []

for i in range(0, 5):
    daily_steps = [row[i] for row in steps]
    if i == 0:
        print(f"Total steps for Monday: {sum(daily_steps)} steps")
    elif i == 1:
        print(f"Total steps for Tuesday: {sum(daily_steps)} steps")
    elif i == 2:
        print(f"Total steps for Wednesday: {sum(daily_steps)} steps")
    elif i == 3:
        print(f"Total steps for Thursday: {sum(daily_steps)} steps")
    elif i == 4:
        print(f"Total steps for Friday: {sum(daily_steps)} steps")
    else:
        print("ERROR!")
    total_steps.append(sum(daily_steps))

if max(total_steps) == total_steps[0]:
    print(f"The most active day overall is: Monday")
elif max(total_steps) == total_steps[1]:
    print(f"The most active day overall is: Tuesday")
elif max(total_steps) == total_steps[2]:
    print(f"The most active day overall is: Wednesday")
elif max(total_steps) == total_steps[3]:
    print(f"The most active day overall is: Thursday")
elif max(total_steps) == total_steps[4]:
    print(f"The most active day overall is: Friday")
else:
    print("ERROR!")