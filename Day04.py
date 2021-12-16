def set(input,board):
    for i in range(5):
        for j in range(5):
            if board[i][j] == input:
                board[i][j] = -1

def bingo(board):
    cc = 0
    rc = 0
    for r in range(5):
        rc = 0
        for c in range(5):
            if board[r][c] == -1:
                rc +=1
        if rc == 5:
            return True
    for c in range(5):
        cc = 0
        for r in range(5):
            if board[r][c] == -1:
                cc += 1
        if cc == 5:
            return True
    return False        
    


def parse_board(lines):
    #print(lines)
    a = len(lines)
    l = []
    for i in range(5):
        a = []
        for j in range(5):
            a.append(None)
        l.append(a)
    r = 0
    for line in lines:
        if line == '':
            continue
        digits = line.split(' ')
        #print(digits)
        c = 0
        for d in digits:
            if d == '':
                continue
            #print(r,c)
            l[r][c] = int(d)
            c+=1
        r+=1
    #print(l)
    return l

def output(b,v):
    sum = 0
    for r in range(5):
        for c in range(5):
            if b[r][c] != -1:
                sum+=b[r][c]
    print(sum*v)

# main header
if __name__ == '__main__':
    # Input Section
    boards = []
    input = []
    lines = open(
        r"C:\Users\ACER\OneDrive\Documents\Git-Lab\AdventOfCode2021\Input\day04.txt", "r").read().split("\n")
    j = 2
    line = lines[0].split(',')
    for i in line:
        input.append(int(i))
    while j < len(lines):
       b = parse_board(lines[j:j+6])
       j = j + 6
       boards.append(b)
    
    win = {}
    for v in input:
        for i,b in enumerate(boards):
            if win.get(i):
                continue
            set(v,b)
            if bingo(b):
                win[i] = True
                if len(win) == len(boards):
                    output(b,v)
                    break
        else:
            continue
        break


    

    
    

