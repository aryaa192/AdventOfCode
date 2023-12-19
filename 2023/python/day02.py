

import sys


def sum_of_rounds(game_data):
    red_target = 12
    green_target = 13
    blue_target = 14

    total_rounds = 0
    for rounds, info in game_data.items():
        #print(rounds, info)
        for _ in info.items():
            if info['red'] <= red_target and info['blue'] <= blue_target and info['green'] <= green_target:
                print(rounds)
                total_rounds += int(''.join(filter(str.isdigit, rounds)))
                break

    return total_rounds


def count_cubes(game_str):
    cube_counts = {"red": 0, "blue": 0, "green": 0}
    rounds = game_str.split(';')
    
    for round_info in rounds:
        cubes = round_info.split(', ')
        for cube in cubes:
            count, color = cube.split()
            cube_counts[color] += int(count)
    
    return cube_counts

def extract_input(game_str):
    # expecting:
    # input: "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    # output: {"Game 1":{"red": 5, "blue": 9, "green": 4}}
    game_data = {}
    game_name, game_info = game_str.split(":")
    game_data[game_name.strip()] = count_cubes(game_info)
    return game_data


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


if __name__ == "__main__":
    
    # game_input = [
    # "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    # "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    # "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    # "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    # "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green" 
    # ]
    
    game_input = parse_input(sys.argv)
    
    game_data = {}
    for game_str in game_input:
        game_data.update(extract_input(game_str))

    print(sum_of_rounds(game_data))
