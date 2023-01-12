# Author: Amit Arya 
# Date: 

# Problem Descriptions
def get_sliced(items):
    c1, c2 = [], []
    c1, c2 = items[:len(items)//2], items[len(items)//2:]

    return c1, c2

def get_priorityItems(rucksucks):
    priorities = []
    for items in rucksucks:
        c1, c2 = get_sliced(items)
        for i in c1:
            if i in c2 and not in priorities:
                priorities.append(i)
    
    return priorities

def parse_input():
    with open(r's_input.txt', 'r') as f:
        data = f.readlines()
        rucksucks = [data_s.strip() for data_s in data]
    
    f.close()
    return rucksucks


# main section
if __name__ == '__main__':

    input = parse_input()
    getPriorityItems = get_priorityItems(input)
    v = 0
    priorities
    for i = 'a'; i<='z'

    

