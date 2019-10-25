import os

listOfDirectories = ['CC', 'NYT', "TW"]
ignoreList = ['â€œthe','itâ€™s','much','trump','president','make','want','thing']
for directory in listOfDirectories:
    print("=========================== Printing for " + directory + " ======================================")
    path = "./" + directory
    files = os.listdir(path)
    listOfWords = []
    listOfCounts = []
    op = open(directory+".txt", "w", encoding='utf-8')
    op.write("word,count\n")
    for file in files:
        outputFile = open("./" + directory + "/" + file, 'r')
        line = outputFile.readline()
        while line != "":
            # print(line)
            entry = line.split(",")
            word = entry[0]
            if word in ignoreList:
                line = outputFile.readline()
                continue
            count = entry[1]
            count = count.replace('\t\n', "")
            listOfWords.append(word)
            listOfCounts.append(int(count))
            line = outputFile.readline()
    print(listOfCounts)
    print(listOfWords)
    print(len(listOfCounts))
    print(len(listOfWords))
    print(max(listOfCounts))
    for i in range(10):
        tempMaxIdx = listOfCounts.index(max(listOfCounts))
        print(listOfWords[tempMaxIdx] + ": " + str(listOfCounts[tempMaxIdx]))
        op.write(listOfWords[tempMaxIdx] + "," + str(listOfCounts[tempMaxIdx])+"\n")
        listOfWords.pop(tempMaxIdx)
        listOfCounts.pop(tempMaxIdx)
