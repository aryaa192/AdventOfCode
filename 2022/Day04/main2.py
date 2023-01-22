import sys


class Pairs:
    def __init__(self, start, end):
        self.start = start
        self.end = end   




class Inputs:
    def parse_input(self, argv):
        if len(argv) < 2:
            FILE_INPUT = 'Input/input.txt'
        else:
            FILE_INPUT = argv[1]
        with open(FILE_INPUT, 'r',encoding='utf-8') as file:
            data = file.readlines()
            pair_sections_list = [str.strip() for str in data]
            # = [str.split(',') for str in temp1]
        file.close()
        
        return pair_sections_list

    
    def parsePair(self, p):
        ss = p.split('-')
        start, end = int(ss[0]), int(ss[1])
        return start, end


if __name__ == '__main__':
    inputs = Inputs()
    input1 = inputs.parse_input(sys.argv)
    pairs = Pairs()
    print(input1)
    for line in input1:
        if line == "":
            continue
        for _, v in line.split(','):
            pairs.start, pairs.end = inputs.parsePair(v)

    
    print(pairs.start, pairs.end)
    
    
