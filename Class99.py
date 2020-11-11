import os
import shutil

#os.system("time")
#os.mkdir("D:/WHJ/Class99/TestFolderOf_C99")
#print(os.getcwd())
path=""
exist=os.path.exists(path)
#print(exist)

filePath="C:/Users/Smaran/Pictures/Saved Pictures/rapunzel.tif"
bbc=os.path.splitext(filePath)
#print(bbc)

#print(os.listdir("D:/WHJ/Class99"))

src="D:/WHJ/Class99/TestFolderOf_C99 - 1"
dest="D:/WHJ/Class99/TestFolderOf_C99 - 2"
#destination=shutil.move(src, dest)
#print(os.listdir("D:/WHJ/Class99"))

path2="D:/WHJ/Class99/ExtensionSampleFolder"
files=os.listdir(path2)
for i in files:
    name, ext=os.path.splitext(i)
    ext=ext[1:]
    if ext=="":
        continue
    if os.path.exists(path2+"/"+ext):
        shutil.move(path2+"/"+i,path2+"/"+ext+"/"+i)
    else:
        os.makedirs(path2+"/"+ext)
        shutil.move(path2+"/"+i,path2+"/"+ext+"/"+i)
