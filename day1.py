
with open('input_day1.txt') as f:
    lines = f.readlines()

maxCalories = 0
calories = 0
for line in lines:
    if line == '\n':
        if calories >= maxCalories:
            maxCalories = calories

        calories = 0
    else:
        calories += int(line)

print(maxCalories)


elves = []
calories = 0
for line in lines:
    if line == '\n':
        elves.append(calories)
        calories = 0
    else:
        calories += int(line)

elves.sort()
print(sum(elves[-3:]))
