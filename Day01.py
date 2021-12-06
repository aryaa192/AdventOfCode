# Main Method area.
if __name__ == "__main__":
    count = 0
    lis = []
    fin = open(r"day01.txt","r")
    for i in fin:
        lis.append(i)
    for i in range(1,len(lis)):
        if lis[i] > lis[i-1]:
            count += 1
            break
        else:
            break
    print(count)
    
    

