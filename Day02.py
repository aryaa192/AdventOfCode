# Main Method area.
if __name__ == "__main__":
    # Submarine moving command problems using dictonary in python.
    # X variable indicates moving forward
    # Y variable indicates moving up/down from it's initial sea level.
    X = 0
    Y = 0
    data =  open(r"C:\Users\ACER\OneDrive\Documents\Python-Workspace\BASICS\day2.txt", 'r')
    for line in data:
        items = line.rstrip('\n').split(' ')
        key = items[0]
        values = items[1]
        if key == "forward":
            X += int(values)
        elif key == "down":
            Y += int(values)
        elif key == "up":
            Y -= int(values)    
    output = X*Y
    print(output)
