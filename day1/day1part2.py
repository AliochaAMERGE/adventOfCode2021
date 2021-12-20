def sonar_three_mesurements(path):

    file = open(path, 'r')

    b1 = False
    b2 = False
    b3 = False

    cpt = 0

    for line in file:

        line = int(line)

        if not b1:
            temp1 = line
            b1 = True
        elif not b2:
            temp2 = line
            b2 = True
        elif not b3:
            temp3 = line
            b3 = True
        else : 
            if((temp1+temp2+temp3) < (temp2 + temp3 + line)):
                cpt = cpt + 1
                
                print(str(temp2+temp3+line) + " increaded")
                temp1 = temp2
                temp2 = temp3
                temp3 = line
            else : 
                print(str(temp2+temp3+line) + " decreased")
                temp1 = temp2
                temp2 = temp3
                temp3 = line


    return cpt

print(sonar_three_mesurements("input"))