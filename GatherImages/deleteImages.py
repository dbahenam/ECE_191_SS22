# This will delete all jpg files in Images Folder!
import os
filelist = [ f for f in os.listdir("Images") if f.endswith(".jpg") ]
for f in filelist:
    os.remove(os.path.join("Images", f))