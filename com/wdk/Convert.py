# encoding=utf-8
#把所有文章合并到一个文件里.后续进行分词统计
import os
class Convert():
    def __init__(self,filePath,outFile):
        self.filePath = filePath
        self.outFile = outFile

    #以读的形式打开文件
    def read_file_handler(self,fileName):
        """读取文件....."""
        fileObj = open(fileName,'r')
        return fileObj

    def mergeArticle(self):
        """把文件夹里面的所有文件内容 合并到一个文件"""
        out_file = open(self.outFile,"w");
        file_num = 0
        # 遍历文件夹
        for file in os.listdir(self.filePath):
            content_list = []
            fileObj = self.read_file_handler("\\".join([self.filePath,file]))
            for line in fileObj:
                content_list.append(line.strip())
            #把结果输出到文件.
            print >> out_file,'\t'.join([str(file_num),' '.join(content_list)])
            file_num += 1;

# if __name__ == "__main__":
#     convert = Convert()
#     convert.mergeArticle()
