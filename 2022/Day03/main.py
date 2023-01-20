# Author: Amit Arya | github: /aryaa192 | linkedin: /akarya943 |
# Date: 20th Jan'23.


# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# Import Section
import string

# Global Declaration:
priorities = {}

# Problem Descriptions:
# AdventOfCode2022: Day03 --> https://adventofcode.com/2022/day/3

# Part-1
def get_priorities_sum_p1(rucksucks):
    priortiesSum = 0
    for items in rucksucks:
        compartment_1, compartment_2 = get_sliced(items)
        for item in compartment_1:
            if item in compartment_2:
                priortiesSum += priorities[item]
                break
    return priortiesSum


def get_sliced(items):
    compartment_1, compartment_2 = [], []
    compartment_1, compartment_2 = items[:len(items)//2], items[len(items)//2:]
    # print(c1,c2)
    return compartment_1, compartment_2


# This function helps convert given input into appropriate data-structure/datasets for part 1
# Kindly choose the input file accordingly. e.g., s_input.txt is sample input.
def parse_input():
    with open(r'Input/input.txt', 'r', encoding="utf-8") as f:
        data = f.readlines()
        rucksucks = [data_s.strip() for data_s in data]
    f.close()
    return rucksucks


# Part - 2
def get_unique(items):
    set_out = set(items[0]) & set(items[1]) & set(items[2])
    return  list(set_out)


def get_priorities_sum_p2(g_rucksucks):
    priortiesSum = 0
    for g_rucksuck in g_rucksucks:
        getBadge = get_unique(g_rucksuck)
        priortiesSum += priorities[getBadge[0]] 
    return priortiesSum


# This function helps convert given input into appropriate data-structure/datasets for part 2.
# Kindly choose the input file accordingly. e.g., s_input.txt is sample input.
def parse_input2():
    with open(r'Input/input2.txt', 'r', encoding="utf-8") as file:
        data = file.readlines()
        rucksucks = [str.strip() for str in data]
    file.close()
    g_rucksucks = [[]]
    g_rucksucks = [rucksucks[i:i+3] for i in range(0, len(rucksucks), 3)]
    return g_rucksucks


# main section
if __name__ == '__main__':

    input1 = parse_input()
    input2 = parse_input2()
    v = 1
    lowers = list(string.ascii_lowercase)
    uppers = list(string.ascii_uppercase)
    for i in lowers:
        priorities[i] = v
        v += 1
    for i in uppers:
        priorities[i] = v
        v += 1
    prioritySum = get_priorities_sum_p1(input1)
    prioritySum2 = get_priorities_sum_p2(input2)
    print(prioritySum, prioritySum2)