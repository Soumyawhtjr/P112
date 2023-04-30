import os
import shutil
from_dir='C:/Users/dell/Desktop/Snips'
to_dir="C:/Users/dell/Download/idk"
list_of_files=os.listdir(from_dir)
###print(list_of_files)

for i in list_of_files:
    root,extension=os.path.splitext(i)
    print("Root:",root,"Ext:",extension)

    if extension=="":
      continue
    if extension in['.gif','.png','.jpeg','.jpg','.jfif']:
       path1=from_dir+"/"+i
       path2=to_dir+"/"+"Image"
       path3=to_dir+"/"+"Image"+"/"+i

       if os.path.exists(path2): 
          print("Moving " + i +"....")
          shutil.move(path1, path3)

       else:
            os.makedirs(path2)
            print("Moving " + i)
            shutil.move(path1, path3)

