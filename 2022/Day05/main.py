


# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=missing-final-newline
# pylint: disable=trailing-whitespace


# import section
import sys
from string import ascii_uppercase
import copy

# Global declaration 
CRATES = list(ascii_uppercase)


# Sample Input:
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2

# Part 1 
def crate_mover_9000(stacks, moves):
    # moves = [[count, src, dest], ..., [count,src,dest]]
    #print(moves)
    count, src, dest = int(moves[1]), int(moves[3])-1, int(moves[5])-1
    for _ in range(count):
        v = stacks[src].pop()
        stacks[dest].append(v)

    
        
    return stacks

# Part 2
def crate_mover_9001(stacks, moves):
    count, src, dest = int(moves[1]), int(moves[3])-1, int(moves[5])-1
    #   move 1 from 2 to 1
    temp = []
    for _ in range(count):
        temp.append(stacks[src].pop())
    temp = reversed(temp)
    stacks[dest].extend(temp)
    print(stacks[dest])
    return stacks


def get_crates(crates, stacks_dic):
    key, value = 0, []
    for crate in crates:
        for index, char in enumerate(crate):
            if char in CRATES:
                value.append(char)
                # index --> value
                # 5 --> D
                # 1 --> N
                # 5 --> C
                # 1 --> Z
                # 5 --> N
                # 9 --> P
                key = index//4
                stacks_dic[key].extend(value)
                value.pop()
    
    return stacks_dic

def parse_input(argv):
    if len(argv) < 2:
        FILE_INPUT = 'Input/input.txt'
    else:
        FILE_INPUT = argv[1]

    return FILE_INPUT

if __name__ == '__main__':
    # Parse Input.
    FILE_INPUT = parse_input(sys.argv)
    
    # Read input file.
    with open(FILE_INPUT, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        size_of_stacks = len(lines[0])//4
    file.close()
    print(size_of_stacks)
    # Create stack dictionary to store crates to respective stack positions.
    stacks_dic = {i: [] for i in range(int(size_of_stacks))}
    
    # get all the crates using function get_crates().
    stacks = get_crates(lines[:size_of_stacks], stacks_dic)
    

    # reverse the order of crates as per the condition given.
    for key in stacks:
        stacks[key] = list(reversed(stacks[key]))

    stacks_2 = copy.deepcopy(stacks)
    # fetch the moves and parse to get last stack by each
    move_list = lines[size_of_stacks+2:]
    for move in move_list:
        m = move.strip("\n").split(" ")
        getLastStacks_p1 = crate_mover_9000(stacks, m)
        getLastStacks_p2 = crate_mover_9001(stacks_2, m)

    
    # Get the last crates from each stacks available after re-arrangement.
    last_crates_in_stack_p1 = ""
    last_crates_in_stack_p2 = ""
    for key in getLastStacks_p1:
        last_crates_in_stack_p1 += getLastStacks_p1[key][-1]
    
    for key in getLastStacks_p2:
        last_crates_in_stack_p2 += getLastStacks_p2[key][-1]
    # Print the outcome.
    print(last_crates_in_stack_p1, last_crates_in_stack_p2)