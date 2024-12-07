import sys

# input data reading
def parse_input(argv):
    file = ""
    if len(argv) < 2:
        file = 'inputs/day1.input'
    else:
        file = argv[1]

    file_input = ''
    with open(file, 'r', encoding='utf-8') as f:
        file_input = f.readlines()

    f.close()
    r1 = []
    r2 = []
    for line in file_input:
        v = line.split()
        r1.append(int(v[0]))
        r2.append(int(v[1]))
    return r1 ,r2


def p1(r1,r2):
    r1, r2 = sorted(r1), sorted(r2)
    sum = 0
    for i in range(len(r1)):
        sum += abs(int(r1[i]) - int(r2[i]))

    print(sum)
    # answer : 3714264

def p2(r1,r2):
    similarity_score = []
    c = 0
    for i in range(len(r1)):
        for j in range(len(r2)):
            if r1[i] == r2[j]:
                c += 1
        similarity_score.append(r1[i]*c)
        c = 0
     
    print(sum(similarity_score))
    # ans is 18805872

        

# entry point of program.
if __name__ == "__main__":    
    r1,r2 = parse_input(sys.argv)
    p1(r1,r2)
    p2(r1,r2)
    