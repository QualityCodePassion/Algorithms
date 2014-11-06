

def FileIntegerArray( fileName ):
    fo = open(fileName)
    print "Name of the file: ", fo.name
    lines = fo.readlines()
    unsortedList = [ int(lines) for lines in lines ]
    fo.close()
    return unsortedList
