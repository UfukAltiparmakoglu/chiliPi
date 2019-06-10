import os
from skimage import io
import numpy as np
import subprocess

filesTxt = "files.txt"
videoName = "chiliPi"
fps = 7
darkness_value = 50
command = "mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4 -o "+videoName+".mp4 -mf type=jpeg:fps="+str(fps)+" mf://@"+filesTxt
allFiles = sorted(os.listdir("./"))

#delete files.txt if exists
if os.path.isfile(filesTxt):
    os.remove(filesTxt)

f = open(filesTxt, 'a')

#go through all files
for i in allFiles:
    #take only image files
    if ".jpg" in i:
        curr_image = io.imread(i)
        curr_mean = np.mean(curr_image)
        #if image too dark, remove it!
        if curr_mean < darkness_value:
            os.remove(i)
            continue
        #append image to files.txt
        f.write(i+'\n')

#don't forget to close the file
f.close()

#build video
subprocess.run(command.split(" "))
