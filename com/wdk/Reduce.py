# encoding=UTF-8
import math

class IDFReduce():
    """计算IDF"""

    def __init__(self,docs_cnt):
        """初始化Reduce,docs_cnt是词料库文档数"""
        self.docs_cnt = docs_cnt

    def calculateIdf(self,inputFile,outputFile):
        outputFile = open(outputFile,'w')
        inputFileObj = open(inputFile,'r')

        current_word = None
        current_num = 0

        for lines in inputFileObj:
            word_count = lines.strip().split('\t')
            if len(word_count)!=2:
                continue
            word,count = word_count
            if current_word == None:
                current_word = word
            if current_word != word:
                idf = math.log(float(self.docs_cnt)/(float(current_num)+1.0))
                print >> outputFile,'\t'.join([current_word,str(idf)])
                current_word = word
                current_num = 0
            current_num += int(count)
        idf = math.log(float(self.docs_cnt)/(float(current_num)+1.0))
        print >> outputFile, '\t'.join([current_word, str(idf)])