def dive_aim(path):

    f = open(path, 'r')

    x = 0
    y = 0
    aim = 0

    for line in f:
        if (line.split(" ")[0] == "forward") :

            y = y + int(line.split(" ")[1]) * aim
            
            x = x + int(line.split(" ")[1])

        elif (line.split(" ")[0] == "down"):

            aim = aim + int(line.split(" ")[1])

            # y = y + int(line.split(" ")[1])
        elif (line.split(" ")[0] == "up") :

            aim = aim - int(line.split(" ")[1])

            # y = y - int(line.split(" ")[1])
        else :
            print ("ERROR")
    return x*y

print(dive_aim("input"))
