def check_global(fileName):
    #checks to see if the global header is present.
    readfile = open(fileName,'r')
    linecount = 0
    for line in readfile:
        if '[global]' in line:
            readfile.close()
            return True, linecount
        linecount+=1
    readfile.close()
    return False, -1
