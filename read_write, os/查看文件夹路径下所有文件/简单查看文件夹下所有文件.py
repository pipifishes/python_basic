import os
'''
1. os.walk() 方法可以创建一个生成器，用以生成所要查找的目录及其子目录下的所有文件。
根目录下的每一个文件夹(包含它自己), 产生3-元组 (dirpath, dirnames, filenames)【文件夹路径, 文件夹名字, 文件名】
2. os.path.join(path1[, path2[, ...]])，把目录和文件名合成一个路径
'''
source_dir = 'D:\\python\\ssh'
# home,dirs,files= 文件夹路径, 文件夹名字, 文件名
for home, dirs, files in os.walk(source_dir):
    print("----------------------dir list-------------------")
    for source_dir in dirs:
        print("文件夹路径：",source_dir)

    print("---------------------file list-------------------")
    for filename in files:
        print("文件名是：",filename)
        fullname = os.path.join(home, filename)
        print("文件路径是：",fullname)