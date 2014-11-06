

fo = open("DummyTextInput.txt")
print "Name of the file: ", fo.name


# This is not currently implemented

lines = fo.readlines()
#print "Read Line: %s" % (lines)
#print "Read lines: %s" % (lines[0])

#floatValues = [ float(lines) for lines in lines ]
intValues = [ int(lines) for lines in lines ]

#for n in floatValues

test = 5
for i in xrange(5):
  print intValues[i]
  #print int(lines[i])

#lines = fo.readlines(2)
#print "Read lines: %s" % (lines)

# Close opend file
fo.close()