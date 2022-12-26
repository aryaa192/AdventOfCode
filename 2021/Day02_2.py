# Main Method area.
if __name__ == "__main__":
    # Submarine moving command problems using dictonary in python.
    # X variable indicates moving forward
    # Y variable indicates moving up/down from it's initial sea level.
    X = 0
    Y = 0
    Aim = 0
    data =  open(r"day2.txt", 'r')
    for line in data:
        items = line.rstrip('\n').split(' ')
        key = items[0]
        values = items[1]
        if key == "forward":
            X += int(values)
            Y += int(values)*Aim
        elif key == "down":
            Aim += int(values)
        elif key == "up":
            Aim -= int(values)    
    output = X*Y
    print(output)
