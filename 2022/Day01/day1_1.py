this_elf = 0
max_elf = 0

data = open(r'input.txt', 'r')

for line in data:

    if this_elf > max_elf:
        max_elf = this_elf

    if line == "\n":
        this_elf = 0
    else:
        this_elf += int(line.strip())



print(max_elf)