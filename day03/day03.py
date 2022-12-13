f = open('day03/input.txt')
# f = open('dummy.txt')

priority = 0

for line in f:
    rucksack = line.rstrip('\n')
    n = len(rucksack)
    found = False
    i = 0
    while not found:
        item = rucksack[i]
        if item in rucksack[n//2:]:
            if item.islower():
                priority += ord(item) - ord('a') + 1
            else:
                priority += ord(item) - ord('A') + 27
            found = True
        else:
            i += 1

print(priority)

f.close()

# second part

f = open('day03/input.txt')
# f = open('dummy.txt')

lines = f.readlines()
priority = 0
N = len(lines)

for i in range(0,N//3):
    rucksacks = [line.rstrip('\n') for line in lines[i*3:i*3+3]]

    # match all characters in rs1 and rs2
    matches = []

    for item in rucksacks[0]:
        if item in rucksacks[1]:
            if item not in matches:
                matches.append(item)

    found = False
    k = 0
    while not found:
        item = matches[k]
        if item in rucksacks[2]:
            if item.islower():
                priority += ord(item) - ord('a') + 1
            else:
                priority += ord(item) - ord('A') + 27
            found = True
        k += 1


print(priority)

f.close()
