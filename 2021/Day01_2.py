# Main Method area.
if __name__ == "__main__":
    count = 0
    lis = []
    fin = open(r"day1.txt","r")
    for i in fin:
        lis.append(int(i))
        
    l = len(lis)
    output = []
    for i in range(0,l-2):
        sum = 0
        sum = lis[i] + lis[i+1] + lis[i+2]
        output.append(sum)
    for i in range(1,len(output)):
        if output[i] > output[i-1]:
            count = count + 1
    print(count) 
