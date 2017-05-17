#---------------------------------------------------------------#
#                       CALIBER CONVERTER
#
#               BY COLE FORTSON AND PHILLIP TAYLOR
#---------------------------------------------------------------#

#!/usr/bin/python
import os, glob, shutil
from shutil import copyfile

prefix = "cimg_"
fileType = "png"
group = 0 # batch number for photos
maxGroup = 0
numGroups = 0
index = 0
allShots = list()

os.chdir("/Users/colefortson/Desktop/caliber-converter/")
for file in glob.glob("*.%s" % fileType):
    allShots.append(str(file))
    index += 1

numGroups = len(allShots)/4

for i in range(numGroups):
    dir = ("caliber_shot_" + str(i))
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.makedirs(dir)
    shutil.copy2(prefix + str(i) + "_" + str(0) + ".png", dir)
    shutil.copy2(prefix + str(i) + "_" + str(1) + ".png", dir)
    shutil.copy2(prefix + str(i) + "_" + str(2) + ".png", dir)
    shutil.copy2(prefix + str(i) + "_" + str(3) + ".png", dir)
    shutil.copy2(prefix + str(i) + "_" + str(2) + ".png", dir + "/" + prefix + str(i) + "_" + str(4) + ".png")
    shutil.copy2(prefix + str(i) + "_" + str(1) + ".png", dir + "/" + prefix + str(i) + "_" + str(5) + ".png")

print allShots
# Set up filename
outputName = "caliber_" # output prefix- please don't change
outputName += str(group)
outputName += ".mp4"

# write to txt for concatenation
# f = open("cat.txt","w+")

# for i in range(4):
#    f.write("file '%s'\r\n" % (outputName))

# Runs a batch command to make those images into a quick video
# !!! Framerate needs to be a multiple of 6 !!!
#for i in range():
os.system("ffmpeg -f image2 -r 12 -i cimg_0_%d.png -vcodec mpeg4 -y " + str(outputName))

# Removed, for now...
#os.system("ffmpeg -f concat -i cat.txt -codec copy output.mp4")
