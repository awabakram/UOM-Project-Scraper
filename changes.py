import sys

oldFileName = sys.argv[1]
newFileName = sys.argv[2]

oldFile = open(oldFileName, 'r')
oldAllLines = oldFile.readlines()
oldFile.close()

newFile = open(newFileName, 'r')
newAllLines = newFile.readlines()
newFile.close()

outputFile = open("changes.csv", "w")
header = "Title,Category,Project Link,Proposer,Student Availability,CM COMP30030 Difficulty,CS COMP30040 Difficulty,PhD Potential\n"
outputFile.write(header)

for line in newAllLines:
    if line not in oldAllLines:
        outputFile.write(line)
    else:
        oldAllLines.remove(line)
        
outputFile.close()