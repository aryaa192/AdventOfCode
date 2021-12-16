# Main Method area.
if __name__ == "__main__":
    lis = []
    fin = open(r"C:\Users\ACER\OneDrive\Documents\Git-Lab\AdventOfCode2021\Input\Day03.txt", "r")
    for i in fin:
        lis.append(i)
    
    #def function check for 0s and 1s
    gamma_rate = ''
    for i in range(len(lis[0])-1): # len(lis[m]) = 5
        c_1 = 0
        c_0 = 0
        for j in range(len(lis)): # len(lis) = 10
            if lis[j][i] == '0':
                c_0 +=1
            elif lis[j][i] == '1':
                c_1 +=1
        if c_1 > c_0:
            gamma_rate += '1'
        else:
            gamma_rate +='0'
    
    
    epsilon = ''.join(['1' if i == '0' else '0'for i in gamma_rate])
    # Final output
    output = int(gamma_rate,2)*int(epsilon,2)
    print(output)
        
    
            
    