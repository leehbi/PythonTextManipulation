def openFile():
    fname = raw_input("Enter file name: ")
    if len(fname) < 1 : fname = "mbox-short.txt"
    try:
        fh = open(fname, 'r')
    except:
        print "Error opening file", fname
        quit()
    return fh

def startsWith():
    sw = raw_input("Enter line prefix to use: ")
    if len(sw) < 1 : sw = "From"
    return sw

def doCount(lines,s):
    counts = dict()
    for line in lines:
        if line.startswith(s) and not line.startswith(s+':'):
            line = ((line.rstrip()).lstrip()).split()
	    counts[line[1]] = counts.get(line[1],0) + 1
    return counts

def max(dictionary):
    max = None 
    highest = None
    #print dictionary
    for key in dictionary:
        if max < dictionary[key]:
	    max = dictionary[key]
	    #print "new max is", max
	    highest = key
    return highest

fh = openFile()
sw = startsWith()

dictionary = doCount(fh,sw)
key = max(dictionary)
print key, dictionary[key]
