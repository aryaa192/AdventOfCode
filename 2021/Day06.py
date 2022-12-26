# Lenternfish after 80 days
def P1(fishes):
    for i in range(80):
        temp = []
        babies = 0
        for cntr in fishes:
            new_cntr = cntr - 1
            if new_cntr < 0:
                new_cntr = 6
                babies += 1
            temp.append(new_cntr)
        fishes = temp + [8]*babies
    return fishes

# Lentern Fish after 256 days
def P2(fishes):
    temp = {}
    #print(fishes)
    days = [0,0,0,0,0,0,0,0,0]
    for fish in fishes:
        days[fish] += 1
    
    #print(days)
    for i in range(256):
        Days = list(days)
        for j,v in enumerate(Days):
            if j == 0:
                days[6] += v
                days[8] += v
                days[0] -= v
            else:
                days[j-1] += v
                days[j] -= v
        #print("After day[{i}]",days)
    sum = 0
    for d in days:
        sum +=d
    return sum


# Main Header
if __name__ == '__main__':
    Fish = []
    input = open(r'C:\Users\ACER\OneDrive\Documents\Git-Lab\AdventOfCode2021\INPUT\day06.txt','r').read().split(',')
    for d in input:
        Fish.append(int(d))
    #print(Fish)    
    p1 = P1(Fish)
    p2 = P2(Fish)
    print("The size of lentern fish family after 18 days:",len(p1),p2)