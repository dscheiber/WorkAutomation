##this is a trivial script but actually serves a purpose! there is currently no way to export the number of tests performed
##by the analytical lab. this script will read an exported sample text file and search for (A) which indicates a testing procedure.
##it will also count up cancelled tests and subtract from the total.

##the txt file is not delimited and cannot be read in as a csv. this makes it necessary to split each line based on spaces and iterate thru every item of every line.

##unfortunately, there is a problem with the conversion from pdf to text to there are 200 missing line items or there is some other incongruence with the main file
##like adobe double counts some values?


f = open('C:\\Users\\DScheiber\\Desktop\\metrics\\analytical\\q3-lab-export-new.txt')
lines = f.readlines()
testCount = 0
cancelledCount = 0

for line in lines:
    lineList = list(line.split(" "))
    print(lineList)
    for item in lineList:
        if item == "(A)":
            testCount += 1
        if item == "Cancelled":
            cancelledCount += 1

print(testCount)
print(cancelledCount)
