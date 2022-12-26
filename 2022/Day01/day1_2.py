this_elf = 0
max_elves = [0,0,0]

with open('input.txt') as data:
    for line in data:

        max_elves.sort()
        if this_elf > max_elves[0]:
            max_elves[0] = this_elf

        if line == '\n':
            this_elf = 0

        else:
            this_elf += int(line.strip())




print(sum(max_elves))