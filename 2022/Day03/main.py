# Author: Amit Arya 
# Date: 

# Import Section
import string


# Problem Descriptions
def get_sliced(items):
    c1, c2 = [], []
    c1, c2 = items[:len(items)//2], items[len(items)//2:]

    return c1, c2


def get_priority_items(rucksucks):
    priorities = []
    for items in rucksucks:
        c1, c2 = get_sliced(items)
        for i in c1:
            if i in c2 and i not in priorities:
                priorities.append(i)
    return priorities


def get_priorities_sum(priorities_items):
    v = 1
    priorities_value = {}
    lowers = list(string.ascii_lowercase)
    uppers = list(string.ascii_uppercase)
    for i in lowers:
        priorities_value[i] = v
        v += 1
    for i in uppers:
        priorities_value[i] = v
        v += 1
    sum = 0
    for item in priorities_items:
        sum += priorities_value[item]
    return sum


def parse_input():
    with open(r'input.txt', 'r') as f:
        data = f.readlines()
        rucksucks = [data_s.strip() for data_s in data]
    
    f.close()
    return rucksucks


# main section
if __name__ == '__main__':

    input = parse_input()
    PriorityItems = get_priority_items(input)
    prioritySum = get_priorities_sum(PriorityItems)
    print(prioritySum)



    

