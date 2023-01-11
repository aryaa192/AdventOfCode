
# Author: Amit Arya
# Date: 11th Jan'23.


# Describe problems
# --> Rock, Paper, Scissors
# --> Input given opponents as A,B,and C | yours : X,Y, and Z as move defined in short.
# --> need to find the sum of score using provided conditions applicaple based on input parsed.
# --> follow the logic for part1 and part2 respectvely. understand the logic miss interpreted and required to solve it again in part-2.
################################################################################################






# Part - 1 # Logic-explained
# This strategy guide predicts and recommends the following:
# In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). 
# This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
# In the second round, your opponent will choose Paper (B), and you should choose Rock (X). 
# This ends in a loss for you with a score of 1 (1 + 0).
# The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).
# Possiblities:
# --> {
    # WIN-WIN
#  opp_move: 'Rock' --> win-win | --> your_move: 'Paper'
#  opp_move: 'Paper' --> win-win | --> your_move: 'Scissors'
#  opp_move: 'Scissors' --> win-win | --> your_move: 'Rock'
#  # DRAW_DRAW
#  opp_move: 'Rock' | your_move: 'Rock'
#  opp_move: 'Paper' | your_move: 'Paper'
#  opp_move: 'Scissors' | your_move: 'Scissors'
# }


def get_score1(opp_move, your_move):
    score = 0   
    map_input = {'A': 'Rock', 'B': 'Paper', 'C':'Scissors', 'X': 'Rock', 'Y':'Paper','Z':'Scissors'}
    map_points = {'X':1,'Y':2,'Z':3}
    outcome_points = {'win':6,'lose':0,'draw':3}
    if opp_move == 'A' and your_move == 'Y' or opp_move == 'B' and  your_move == 'Z' or opp_move == 'C' and your_move == 'X':
        return int(map_points[your_move]) + int(outcome_points['win'])
    elif opp_move == 'A' and your_move == 'X' or opp_move == 'Y' and your_move == 'Y' or opp_move == 'C' and your_move == 'Z':
        return int(map_points[your_move]) + int(outcome_points['draw'])
    else:
        return int(map_points[your_move]) + int(outcome_points['lose'])



def p1(rounds_string):
    sum = 0
    for moves in rounds_string:
        opp_move = moves[0]
        your_move = moves[2]
        sum += get_score1(opp_move, your_move)
    return sum

def get_score2(opp_move, your_move):
    score = 0   
    map_input = {'A': 'Rock', 'B': 'Paper', 'C':'Scissors', 'X': 'lose', 'Y':'draw','Z':'win'}
    map_points = {'Rock':1,'Paper':2,'Scissors':3}
    outcome_points = {'win':6,'lose':0,'draw':3}
    if map_input[your_move] == 'draw':
        if map_input[opp_move] == 'Rock':
            return map_points['Rock'] + outcome_points[map_input[your_move]]
        elif map_input[opp_move] == 'Paper':
            return map_points['Paper'] + outcome_points[map_input[your_move]]
        elif map_input[opp_move] == 'Scissors':
            return map_points['Scissors'] + outcome_points[map_input[your_move]]
    elif map_input[your_move] == 'lose':
        if map_input[opp_move] == 'Rock':
            return map_points['Scissors'] + outcome_points[map_input[your_move]]
        elif map_input[opp_move] == 'Paper':
            return map_points['Rock'] + outcome_points[map_input[your_move]]
        elif map_input[opp_move] == 'Scissors':
            return map_points['Paper'] + outcome_points[map_input[your_move]]
    elif map_input[your_move] == 'win':
        if map_input[opp_move] == 'Rock':
            return map_points['Paper'] + outcome_points[map_input[your_move]]
        elif map_input[opp_move] == 'Paper':
            return map_points['Scissors'] + outcome_points[map_input[your_move]]
        elif map_input[opp_move] == 'Scissors':
            return map_points['Rock'] + outcome_points[map_input[your_move]]


# Part - 2 # Logic-explained
def p2(rounds_string):
    sum = 0
    for moves in rounds_string:
        opp_move = moves[0]
        your_move = moves[2]
        sum += get_score2(opp_move, your_move)
    return sum





if __name__ == '__main__':
    with open(r'input.txt', 'r') as f:
        file = f.readlines()
        rounds = [ round_string.strip() for round_string in file]

    
    getScoreP1 = p1(rounds)
    getScoreP2 = p2(rounds)

    print("The sum of score from part1:", getScoreP1)
    print("The sum of score from part2:", getScoreP2)

    

