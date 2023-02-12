# Advent of Code 2022 day 06 solution in python3.
# getTime: 12-02-2023 19:53 PM IST

# import area
import sys


# global declaration



# function declration
def subroutine_p1(datastream):
    char_count = {}
    unique_chars = []

    for i, char in enumerate(datastream):
        if char in unique_chars:
            char_count= {}
            unique_chars = []
        if char not in char_count :
            char_count[char] = 1
            unique_chars.append(char)
            print(i, " ", unique_chars)
        if len(unique_chars) == 4:
            return i+1
        
            
    return -1

def decoder_p2(datastream):
    char_count = {}
    unique_chars = []

    for i, char in enumerate(datastream):
        if char in unique_chars:
            char_count= {}
            unique_chars = []
        if char not in char_count :
            char_count[char] = 1
            unique_chars.append(char)
            print(i, " ", unique_chars)
        if len(unique_chars) == 14:
            return i+1
        
            
    return -1



# parse input
def parse_input(argv):
    file = ""
    if len(argv) < 2:
        file = 'Input/input.txt'
    else:
        file = argv[1]

    file_input = ''
    with open(file, 'r', encoding='utf-8') as f:
        file_input = f.readlines()

    f.close()
    return file_input[0]


# entry point
if __name__ == '__main__':
    datastream = parse_input(sys.argv)
    output_p1 = subroutine_p1(datastream)
    output_p2 = decoder_p2(datastream)
    print(output_p1, output_p2)
