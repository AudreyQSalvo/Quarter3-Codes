names = ["Me", "Lia", "Jake"]

steps = [

  [4500, 5200, 4800, 5000, 5300],

  [4000, 4100, 3900, 4200, 4600],

  [6000, 5800, 5900, 6100, 6200]

]

total_steps = []

for s in steps:
    total_steps.append(sum(s))

max_totsteps = max(total_steps)
min_totsteps = min(total_steps)

max_index = total_steps.index(max_totsteps)
name_moststeps = names[max_index]

difference = max_totsteps - min_totsteps

for i in range(len(names)):
    if names[i] == "Me":
        print(f"My total steps: {total_steps[i]} steps")
    else:
        print(f"{names[i]}'s total steps: {total_steps[i]} steps")

print(f"The person with the highest total of steps is: {name_moststeps}, with {max_totsteps} steps.")
print(f"The difference between the highest and lowest total is: {difference} steps.")