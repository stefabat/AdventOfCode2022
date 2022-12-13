f = open('input.txt')
# f = open('dummy.txt')

score = 0
count = 0
for line in f:
    count += 1
    opponent,me = line.split()
    match me:
        case 'X':
            score += 1
            match opponent:
                case 'A':
                    score += 3
                case 'B':
                    score += 0
                case 'C':
                    score += 6
        case 'Y':
            score += 2
            match opponent:
                case 'A':
                    score += 6
                case 'B':
                    score += 3
                case 'C':
                    score += 0
        case 'Z':
            score += 3
            match opponent:
                case 'A':
                    score += 0
                case 'B':
                    score += 6
                case 'C':
                    score += 3

print('processed %i lines' % count)
print(score)

f.close()

# part 2
# X = lose
# Y = draw
# Z = win
# A = rock     = 1 point
# B = paper    = 2 points
# C = scissors = 3 points

f = open('input.txt')

score = 0
count = 0
for line in f:
    count += 1
    opponent,me = line.split()
    match me:
        case 'X':
            score += 0
            match opponent:
                case 'A':
                    score += 3
                case 'B':
                    score += 1
                case 'C':
                    score += 2
        case 'Y':
            score += 3
            match opponent:
                case 'A':
                    score += 1
                case 'B':
                    score += 2
                case 'C':
                    score += 3
        case 'Z':
            score += 6
            match opponent:
                case 'A':
                    score += 2
                case 'B':
                    score += 3
                case 'C':
                    score += 1

print('processed %i lines' % count)
print(score)

f.close()
