import jieba

jieba.load_userdict("dict_ext.txt")

def splitSentence(inputFile, outputFile):
    fin = open(inputFile, 'r', encoding='UTF-8')
    fout = open(outputFile, 'w', encoding='UTF-8')

    for eachLine in fin:
        line = eachLine.strip()
        wordList = list(jieba.cut(line))
        outStr = ''
        for word in wordList:
            outStr += word
            outStr += ' '
        fout.write(outStr.strip() + '\n')
    fin.close()
    fout.close()


splitSentence('input.txt', 'output.txt')
