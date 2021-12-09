import os
'''
1. os.walk() 方法可以创建一个生成器，用以生成所要查找的目录及其子目录下的所有文件。
根目录下的每一个文件夹(包含它自己), 产生3-元组 (dirpath, dirnames, filenames)【文件夹路径, 文件夹名字, 文件名】
2. os.path.join(path1[, path2[, ...]])，把目录和文件名合成一个路径
3. 查找指定文件后缀名的文件
'''
def get_filelist(source_dir):

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
            readpath.append(fullname)


if __name__ == "__main__":
    # 用于接收所有的文件路径
    readpath = []

    source_dir = input("请输入路径如(D:): ")
    get_filelist(source_dir)
    # get_filelist('D:\\python\\ssh')

    # 判断后缀名为mp3的文件路径
    for i in range(len(readpath)):
        if readpath[i].split(".")[-1] == "mp3":
            print("------------------------------------------------")
            print("后缀名为mp3的文件路径名为：",readpath[i])
