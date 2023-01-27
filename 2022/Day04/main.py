# Author: Amit Arya | github: /aryaa192 | linkedin: /akarya943 |
# Date: 20th Jan'23.


# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# Import Section
import sys

# Global Declaration:



# Problem Descriptions:
# AdventOfCode2022: Day03 --> https://adventofcode.com/2022/day/3

# Part-1

def is_subset_p1(pair_sets):
    p1_start, p1_end = int(pair_sets[0][0]), int(pair_sets[0][1])
    p2_start, p2_end = int(pair_sets[1][0]), int(pair_sets[1][1])
    if p1_start <= p2_start and p1_end >= p2_end or p2_start <= p1_start and p2_end >= p1_end:
        return True
    return False


# This function helps convert given input into appropriate data-structure/datasets for part 1
# Kindly choose the input file accordingly. e.g., s_input.txt is sample input.
def parse_input(argv):
    if len(argv) < 2:
        FILE_INPUT = 'Input/input.txt'
    else:
        FILE_INPUT = argv[1]
    with open(FILE_INPUT, 'r',encoding='utf-8') as file:
        data = file.readlines()
        temp1 = [str.strip() for str in data]
        pair_sections_list= [str.split(',') for str in temp1]
    file.close()
    return pair_sections_list


# Part - 2
def is_subset_p2(pair_sets):
    # ['24-63','57-80']
    #2-4,6-8  --> c1: 2 < 8 and 4 < 6
    #2-3,4-5
    p1_s, p1_e = int(pair_sets[0][0]), int(pair_sets[0][1])
    p2_s, p2_e = int(pair_sets[1][0]), int(pair_sets[1][1])

    #p1_s ------ P1_e   |  p2_s ------ p2_e 
    if p1_s < p2_e and p1_e < p2_s or p2_s < p1_e and p2_e < p1_s:
        return False
    return True

                           




# main section
if __name__ == '__main__':
    input1 = parse_input(sys.argv)
    #print(sys.argv[1])
    #print(input1)
    count = 0
    p2_count = 0
    for pairs in input1:
        set_pairs = [tuple(p.split('-')) for p in pairs]
        isSubset1 = is_subset_p1(set_pairs)
        isSubset2 = is_subset_p2(set_pairs)
        if isSubset1:
            count += 1

        if isSubset2:
            p2_count += 1



    print(count, p2_count)