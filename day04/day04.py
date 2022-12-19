f = open('day04/input.txt')

count = 0
for line in f:
    assignments = line.rstrip('\n').split(',')
    first_id_min,first_id_max = assignments[0].split('-')
    second_id_min,second_id_max = assignments[1].split('-')
    if int(second_id_min) >= int(first_id_min) and int(second_id_max) <= int(first_id_max):
        count += 1
    elif int(second_id_min) <= int(first_id_min) and int(second_id_max) >= int(first_id_max):
        count += 1

print(count)

f.close()
f = open('day04/input.txt')

count = 0
for line in f:
    assignments = line.rstrip('\n').split(',')
    first_id_min,first_id_max = assignments[0].split('-')
    second_id_min,second_id_max = assignments[1].split('-')
    if int(second_id_min) < int(first_id_min):
        if int(second_id_max) >= int(first_id_min):
            count += 1
    elif int(second_id_min) in range(int(first_id_min),int(first_id_max)+1):
        count += 1

print(count)
