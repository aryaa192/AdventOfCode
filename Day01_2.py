# Main Method area.
if __name__ == "__main__":
    c = 0
    lis = []
    fin = open(r"C:\Users\ACER\OneDrive\Documents\Python-Workspace\BASICS\day1_input.txt","r")
    print("Input: ")
    for i in fin:
        print(type(i))
        lis.append(int(i))
        
    l = len(lis)
    print("size of input",l)
    output = []
    for i in range(0,l-2):
        sum = 0
        # 1 2 3 4
        # 0 1 2 3
        sum = lis[i] + lis[i+1] + lis[i+2]
        print("Sum at &i",i,sum)
        output.append(sum)
    for i in range(1,len(output)):
        if output[i] > output[i-1]:
            c = c + 1
    print(c) 