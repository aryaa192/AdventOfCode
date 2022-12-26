# Main Method area.
def first_bit_checker(bit,j):
    c_1 = []
    c_0 = []
    for i in range(len(bit)):  # 00100
        if bit[i].startswith('1', j):
            c_1.append(bit[i])
        if bit[i].startswith('0', j):
            c_0.append(bit[i])
    if len(c_1) >= len(c_0):
        return c_1
    else:
        return c_0


def co2_first_bit_checker(bit, j):
    c_1 = []
    c_0 = []
    for i in range(len(bit)):  # 00100
        if bit[i].startswith('1', j):
            c_1.append(bit[i])
        if bit[i].startswith('0', j):
            c_0.append(bit[i])
    if len(c_0) <= len(c_1):
        return c_0
    else:
        return c_1

def oxygen_generator_rating(input):
    for i in range(len(input[0])):
        input = first_bit_checker(input,i)
        if len(input) == 1:
            break
    return input[0]        
    

def CO2_scrubber_rating(input):
    for i in range(len(input[0])):
        input = co2_first_bit_checker(input, i)
        if len(input) == 1:
            break
    return input[0]



if __name__ == "__main__":
    lis = []
    lis = open(
        r"C:\Users\ACER\OneDrive\Documents\Git-Lab\AdventOfCode2021\Input\Day03.txt", "r").read().split("\n")
    
    OGR = oxygen_generator_rating(lis)
    print(OGR)
    CSR = CO2_scrubber_rating(lis)
    print(CSR)
    output = int(OGR,2)*int(CSR,2)
    print(output)
