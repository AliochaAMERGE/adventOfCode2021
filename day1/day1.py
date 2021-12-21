def sonar(path : str) :
    f = open(path, 'r')
    
    cpt = 1
    boolean = False
    
    for line in f :

        if (boolean and (line > temp)):
            print(line +" (increaded)")
            cpt = cpt + 1
        else :
            print(line +" (decreaded)")

        temp = line
        boolean = True

    return cpt

print(sonar("input"))