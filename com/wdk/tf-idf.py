# encoding=UTF-8
import Convert
import Map
import os
import Reduce
if __name__ == "__main__":
    # 第一步 合并词料库
    convert_input = "D:\\python_program\\mr-TFIDF\\resource\\input_tfidf_dir"
    convert_output = "output_data.txt";
    convert = Convert.Convert(convert_input,convert_output)
    convert.mergeArticle()
    #第二步 对词料库所有的单词转成tuple
    #判断文件是否存在
    if not os.path.exists(convert_output):
        print ("~~~~~~~~~第一步失败,没有得到输出内容~~~~~~~~~~~")

    map_output = "word_tuple_output.txt"
    map = Map.CountMap()
    map.word2Tuple(convert_output,map_output)

    #第三步 对词料库中所有的词 求idf
    #判断第二步文件是否正确输出
    if not os.path.exists(map_output):
        print ("~~~~~~~~~第二步失败,没有得到输出内容~~~~~~~~~~~")
    docs_num = 508
    reduce_output = "reduce_output.txt"
    reduce = Reduce.IDFReduce(docs_num)
    reduce.calculateIdf(map_output,reduce_output)
