# Author: Amit Arya
# Date: 20th Dec'23.


# import section.
import sys

# applied logic for given circumstances in part-1
def sum_of_rounds(game_data):
    red_target = 12
    green_target = 13
    blue_target = 14

    total_rounds = 0
    for rounds, info in game_data.items():
        for _ in info.items():
            if info['red'] <= red_target and info['blue'] <= blue_target and info['green'] <= green_target:
                total_rounds += int(''.join(filter(str.isdigit, rounds)))
                break

    return total_rounds

# checking sub-rounds containing the counts of each cubes by evaluating the max value in each round.
def count_cubes(game_str):
    cube_counts = {"red": 0, "blue": 0, "green": 0}
    rounds = game_str.split(';')
    
    for round_info in rounds:
        cubes = round_info.split(', ')
        for cube in cubes:
            count, color = cube.split()
            if cube_counts[color] <= int(count):
                cube_counts[color] = int(count)
    
    return cube_counts

# resturcture of data.
def extract_input(game_str):
    # expecting:
    # input: "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    # output: {"Game 1":{"red": 5, "blue": 9, "green": 4}}
    game_data = {}
    game_name, game_info = game_str.split(":")
    game_data[game_name.strip()] = count_cubes(game_info)
    return game_data


# input data reading
def parse_input(argv):
    file = ""
    if len(argv) < 2:
        file = 'inputs/day02.input'
    else:
        file = argv[1]

    file_input = ''
    with open(file, 'r', encoding='utf-8') as f:
        file_input = f.readlines()

    f.close()
    file = []
    for i in file_input:
        file.extend(i.strip().split("\n"))
    return file


# entry point of program.
if __name__ == "__main__":    
    game_input = parse_input(sys.argv)
    
    game_data = {}
    for game_str in game_input:
        game_data.update(extract_input(game_str))
    
    # Part1 output.
    out_file = open('outputs/day02.output', 'w', encoding='utf-8')
    out_file.write(str(sum_of_rounds(game_data)))
    out_file.close()
    print(sum_of_rounds(game_data))
