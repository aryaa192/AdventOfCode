# Main Method area.
if __name__ == "__main__":
    c = 0
    lis = []
    fin = open(r"C:\Users\ACER\OneDrive\Documents\Python-Workspace\BASICS\day1_input.txt","r")
    for i in fin:
        lis.append(i)
    print(len(lis))
    for i in range(len(lis)):
        for j in range(i+1,len(lis)):
            if lis[j] > lis[i]:
                c += 1
                break
            else:
                break
    print(c)
    
    

