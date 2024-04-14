import sys
fileName = sys.argv[1]


file = open(fileName, 'r')
fileLines = file.readlines()
file.close()

outputFile = open("formatted.csv", "w")
header = "Title,Category,Project Link,Proposer,Student Availability,CM COMP30030 Difficulty,CS COMP30040 Difficulty,PhD Potential\n"
outputFile.write(header)

for line in fileLines[1:]:
    splitLine = line.split(",")[:-1]
    print(splitLine)
    if splitLine[-1].strip() == "No":
        splitLine[-1] = "False"
    elif splitLine[-1].strip() == "Yes":
        splitLine[-1] = "True"
    joinedLine = '","'.join(splitLine)
    newLine = f'"{joinedLine.strip()}"\n'
    print(newLine)
    outputFile.write(newLine)

        
outputFile.close()