import jieba
import re
import math
import profile # 模块定义

vector_a=[]
vector_b=[] # 向量定义


def Read_Original(): # 读入原本文件
        try:
                original_txt=open("C:/Users/叶昊明/Desktop/个人编程作业样例数据/sim_0.8/orig.txt",encoding="utf-8") # 打开文件
        except OSError:
                print('指定文件不存在！') # 文件不存在则抛出异常处理
        original_list=original_txt.read() # 文件读取
        original_list=re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+","",original_list) # 文本处理
        original_list=jieba.cut(original_list,cut_all=True) # 文本分词
        original_list=list(original_list) # 分词后的结果转换成列表
        original_txt.close() # 文件关闭
        return original_list # 返回分词后的列表

def Read_Copy1():# 读入抄袭文件
        try:
                copy_txt=open("C:/Users/叶昊明/Desktop/个人编程作业样例数据/sim_0.8/blank.txt",encoding="utf-8") # 打开文件
        except OSError:
                print('指定文件不存在！') # 文件不存在则抛出异常处理
        copy_list=copy_txt.read() # 文件读取
        copy_list=re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+","",copy_list) # 文本处理
        copy_list=jieba.cut(copy_list,cut_all=True) # 文本分词
        copy_list=list(copy_list) # 分词后的结果转换成列表
        copy_txt.close() # 文件关闭
        return copy_list # 返回分词后的列表
def Read_Copy2():# 读入抄袭文件
        try:
                copy_txt=open("C:/Users/叶昊明/Desktop/个人编程作业样例数据/sim_0.8/orig_0.8_add.txt",encoding="utf-8") # 打开文件
        except OSError:
                print('指定文件不存在！') # 文件不存在则抛出异常处理
        copy_list=copy_txt.read() # 文件读取
        copy_list=re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+","",copy_list) # 文本处理
        copy_list=jieba.cut(copy_list,cut_all=True) # 文本分词
        copy_list=list(copy_list) # 分词后的结果转换成列表
        copy_txt.close() # 文件关闭
        return copy_list # 返回分词后的列表
def Read_Copy3():# 读入抄袭文件
        try:
                copy_txt=open("C:/Users/叶昊明/Desktop/个人编程作业样例数据/sim_0.8/orig_0.8_del.txt",encoding="utf-8") # 打开文件
        except OSError:
                print('指定文件不存在！') # 文件不存在则抛出异常处理
        copy_list=copy_txt.read() # 文件读取
        copy_list=re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+","",copy_list) # 文本处理
        copy_list=jieba.cut(copy_list,cut_all=True) # 文本分词
        copy_list=list(copy_list) # 分词后的结果转换成列表
        copy_txt.close() # 文件关闭
        return copy_list # 返回分词后的列表
def Read_Copy4():# 读入抄袭文件
        try:
                copy_txt=open("C:/Users/叶昊明/Desktop/个人编程作业样例数据/sim_0.8/orig_0.8_dis_1.txt",encoding="utf-8") # 打开文件
        except OSError:
                print('指定文件不存在！') # 文件不存在则抛出异常处理
        copy_list=copy_txt.read() # 文件读取
        copy_list=re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+","",copy_list) # 文本处理
        copy_list=jieba.cut(copy_list,cut_all=True) # 文本分词
        copy_list=list(copy_list) # 分词后的结果转换成列表
        copy_txt.close() # 文件关闭
        return copy_list # 返回分词后的列表
def Read_Copy5():# 读入抄袭文件
        try:
                copy_txt=open("C:/Users/叶昊明/Desktop/个人编程作业样例数据/sim_0.8/orig_0.8_dis_3.txt",encoding="utf-8") # 打开文件
        except OSError:
                print('指定文件不存在！') # 文件不存在则抛出异常处理
        copy_list=copy_txt.read() # 文件读取
        copy_list=re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+","",copy_list) # 文本处理
        copy_list=jieba.cut(copy_list,cut_all=True) # 文本分词
        copy_list=list(copy_list) # 分词后的结果转换成列表
        copy_txt.close() # 文件关闭
        return copy_list # 返回分词后的列表
def Read_Copy6():# 读入抄袭文件
        try:
                copy_txt=open("C:/Users/叶昊明/Desktop/个人编程作业样例数据/sim_0.8/orig_0.8_dis_7.txt",encoding="utf-8") # 打开文件
        except OSError:
                print('指定文件不存在！') # 文件不存在则抛出异常处理
        copy_list=copy_txt.read() # 文件读取
        copy_list=re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+","",copy_list) # 文本处理
        copy_list=jieba.cut(copy_list,cut_all=True) # 文本分词
        copy_list=list(copy_list) # 分词后的结果转换成列表
        copy_txt.close() # 文件关闭
        return copy_list # 返回分词后的列表
def Read_Copy7():# 读入抄袭文件
        try:
                copy_txt=open("C:/Users/叶昊明/Desktop/个人编程作业样例数据/sim_0.8/orig_0.8_dis_10.txt",encoding="utf-8") # 打开文件
        except OSError:
                print('指定文件不存在！') # 文件不存在则抛出异常处理
        copy_list=copy_txt.read() # 文件读取
        copy_list=re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+","",copy_list) # 文本处理
        copy_list=jieba.cut(copy_list,cut_all=True) # 文本分词
        copy_list=list(copy_list) # 分词后的结果转换成列表
        copy_txt.close() # 文件关闭
        return copy_list # 返回分词后的列表
def Read_Copy8():# 读入抄袭文件
        try:
                copy_txt=open("C:/Users/叶昊明/Desktop/个人编程作业样例数据/sim_0.8/orig_0.8_dis_15.txt",encoding="utf-8") # 打开文件
        except OSError:
                print('指定文件不存在！') # 文件不存在则抛出异常处理
        copy_list=copy_txt.read() # 文件读取
        copy_list=re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+","",copy_list) # 文本处理
        copy_list=jieba.cut(copy_list,cut_all=True) # 文本分词
        copy_list=list(copy_list) # 分词后的结果转换成列表
        copy_txt.close() # 文件关闭
        return copy_list # 返回分词后的列表
def Read_Copy9():# 读入抄袭文件
        try:
                copy_txt=open("C:/Users/叶昊明/Desktop/个人编程作业样例数据/sim_0.8/orig_0.8_mix.txt",encoding="utf-8") # 打开文件
        except OSError:
                print('指定文件不存在！') # 文件不存在则抛出异常处理
        copy_list=copy_txt.read() # 文件读取
        copy_list=re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+","",copy_list) # 文本处理
        copy_list=jieba.cut(copy_list,cut_all=True) # 文本分词
        copy_list=list(copy_list) # 分词后的结果转换成列表
        copy_txt.close() # 文件关闭
        return copy_list # 返回分词后的列表
def Read_Copy10():# 读入抄袭文件
        try:
                copy_txt=open("C:/Users/叶昊明/Desktop/个人编程作业样例数据/sim_0.8/orig_0.8_rep.txt",encoding="utf-8") # 打开文件
        except OSError:
                print('指定文件不存在！') # 文件不存在则抛出异常处理
        copy_list=copy_txt.read() # 文件读取
        copy_list=re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+","",copy_list) # 文本处理
        copy_list=jieba.cut(copy_list,cut_all=True) # 文本分词
        copy_list=list(copy_list) # 分词后的结果转换成列表
        copy_txt.close() # 文件关闭
        return copy_list # 返回分词后的列表
def Read_Copy11():# 读入抄袭文件
        try:
                copy_txt=open("C:/Users/叶昊明/Desktop/个人编程作业样例数据/sim_0.8/000.txt",encoding="utf-8") # 打开文件
        except OSError:
                print('指定文件不存在！') # 文件不存在则抛出异常处理
        copy_list=copy_txt.read() # 文件读取
        copy_list=re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+","",copy_list) # 文本处理
        copy_list=jieba.cut(copy_list,cut_all=True) # 文本分词
        copy_list=list(copy_list) # 分词后的结果转换成列表
        copy_txt.close() # 文件关闭
        return copy_list # 返回分词后的列表
def Caculator_Cos(original_list,copy_list): # 计算向量余弦
        Together=copy_list+original_list # 合并两个文本列表
        Together=list(set(Together)) # 利用集合进行去重
        for i in Together:
                vector_a.append(original_list.count(i))
                vector_b.append(copy_list.count(i)) # 计算两个文本向量
        Sum_vector_a=0
        Sum_vector_b=0 # 计算向量的内积定义
        Sum=0
        for i in range(0,len(vector_a)): # 计算夹角余弦值的循环
                Sum_vector_a+=vector_a[i]*vector_a[i]
                Sum_vector_b+=vector_b[i]*vector_b[i]
                Sum+=vector_a[i]*vector_b[i]
        try:
                ans=Sum/math.sqrt(Sum_vector_b)/math.sqrt(Sum_vector_a)
        except ZeroDivisionError:
                print('文本经过处理后为空！') # 文件处理后为空则抛出异常，利用计算时分母为0的转义
        return ans  # 返回答案值



def Print_Answer(ans): # 将答案输出到指定文件
        print(ans)

original_list=Read_Original()

copy_list=Read_Copy2()
ans=Caculator_Cos(original_list,copy_list)
Print_Answer(ans)

copy_list=Read_Copy3()
ans=Caculator_Cos(original_list,copy_list)
Print_Answer(ans)

copy_list=Read_Copy4()
ans=Caculator_Cos(original_list,copy_list)
Print_Answer(ans)

copy_list=Read_Copy5()
ans=Caculator_Cos(original_list,copy_list)
Print_Answer(ans)

copy_list=Read_Copy6()
ans=Caculator_Cos(original_list,copy_list)
Print_Answer(ans)

copy_list=Read_Copy7()
ans=Caculator_Cos(original_list,copy_list)
Print_Answer(ans)

copy_list=Read_Copy8()
ans=Caculator_Cos(original_list,copy_list)
Print_Answer(ans)

copy_list=Read_Copy9()
ans=Caculator_Cos(original_list,copy_list)
Print_Answer(ans)

copy_list=Read_Copy10()
ans=Caculator_Cos(original_list,copy_list)
Print_Answer(ans)

copy_list=Read_Copy11()
ans=Caculator_Cos(original_list,copy_list)
Print_Answer(ans)

copy_list=Read_Copy1()
ans=Caculator_Cos(original_list,copy_list)
Print_Answer(ans)
