def textfile():
#在D盘创建10个文本文件，以数字给它们命名
    for i in range(1,11):
        with open('d:/'+str(i)+'.txt','w') as text:
            text.write(str(i))
            text.close()
            print('done!')
textfile()

