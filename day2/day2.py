def dive(path):

    f = open(path, 'r')

    x = 0
    y = 0

    for line in f:
        if (line.split(" ")[0] == "forward") :
            x = x + int(line.split(" ")[1])
        elif (line.split(" ")[0] == "down"):
            y = y + int(line.split(" ")[1])
        elif (line.split(" ")[0] == "up") :
            y = y - int(line.split(" ")[1])
        else :
            print ("ERROR")
    return x*y

print(dive("input"))
