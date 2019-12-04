# encoding=UTF-8
class CountMap():
    """解析convert输出的文件,把单词计数 转出tuple类型"""
    def word2Tuple(self,inputFile,outputFile):
        fileObj = open(inputFile,'r')

        #tuple结果输出到文件
        outputFileObj = open(outputFile,'w');

        all_word_list = [];
        for line in fileObj:
            ss = line.strip().split('\t')
            if len(ss) != 2:
                continue
            #第一列是文件编号,第二列是文件内容 上一步处理得到的
            fileNum,fileContent = ss
            wordList = fileContent.strip().split(' ')
            #把list转为set 达到去重的效果
            wordSet = set(wordList);

            for word in wordSet:
                all_word_list.append(word);

        all_word_list.sort();
        for sw in all_word_list:
            print >> outputFileObj, ('\t'.join([sw, '1']))