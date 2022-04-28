import os
import shutil
path1 = "./stophand"

listing = os.listdir(path1)
i = 0
for file in listing:
    source = path1 + "/" + file
    destination = path1 + "/" + "s"+file
    shutil.copy(source,destination)
    i+=1

