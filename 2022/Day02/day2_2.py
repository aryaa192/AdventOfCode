
"""
# A , X --> Rock
# B, Y --> Paper
# C, Z --> Scissors

Winning logic:
--> rock :: paper ++ win
--> paper :: rock ++ lose
--> scissors :: scissors ++ draw

probability:
1. A --> X (draw)
2. A --> Y (win)
3. A --> Z  (win)
4. B --> X  (lose)
5. B --> Y  (draw)
6. B --> Z  (win)
7. C --> X  (lose)
8. C --> Y  (lose)
9. C --> Z  (draw)
"""

def game_outcome(input):
    out = ""
    outcome = [] # win, draw or lose
    selection = [] # X, Y or Z
    # A , X --> Rock
    # B, Y --> Paper
    # C, Z --> Scissors
    for v in input:
        #print(v[1])
        for val in input:
            if v[1] == 'X':
                out = "lose"
                
        outcome.append(out)
        selection.append(v[1])
    return outcome, selection


"""
--> Scores Logic:
---> Rock : 1  x
---> Paper : 2  Y
---> Scissors : 3  Z
--> round outcome:
---> lost : 0
---> draw : 3
---> win : 6 
"""
# A Y --> win : 6 + 2 = 8
# B Y --> draw : 3 + 2 =5 
# B Z --> win : 6 + 3 
# B Z
# A Y
# C Y
# A Y
# C Y
# A Y
# B X
def score(result, selection):
    lose, draw, win = 0, 3, 6
    X, Y, Z = 1, 2, 3
    sum = 0
    s1 = 0
    for val in result:
        if val == "win":
            s1 += 6
        elif val == "draw":
            s1 += 3
        else:
            s1 += 0
    s2 = 0
    for s in selection:
        if s == 'X':
            s2 += X
        elif s == 'Y':
            s2 += Y
        else:
            s2 += Z

    sum = s1 + s2
    return sum



if __name__=="__main__":
    data = open(r'input.txt', 'r')
    input = []
    pair_input = [] 
    for line in data:
        pair_input.append(line.strip())

    for i in pair_input:
        input.append(i.split(' '))
    

    gameOutcome, selection = game_outcome(input)
    winningScore = score(gameOutcome, selection)


    print(pair_input)
    print(input)
    print(gameOutcome, selection, winningScore)
    
        