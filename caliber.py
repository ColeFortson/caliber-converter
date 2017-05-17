#---------------------------------------------------------------#
#                       CALIBER CONVERTER
#
#               BY COLE FORTSON AND PHILLIP TAYLOR
#---------------------------------------------------------------#

#!/usr/bin/python

import os, glob, shutil
from shutil import copyfile
from subprocess import call


prefix = "cimg_"
fileType = "png"
group = 0 # batch number for photos
numGroups = 0
index = 0
allShots = list()

os.chdir("./")
# more pyton BS
for file in glob.glob("*.%s" % fileType):
    allShots.append(str(file))
    index += 1
numGroups = len(allShots)/4

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

# Removed, for now...
#os.system("ffmpeg -f concat -i cat.txt -codec copy output.mp4")


for i in range(numGroups):

    dir = ("caliber_shot_" + str(i))

    if os.path.exists(dir):
        shutil.rmtree(dir)
# Create directory if it doesn't already exist
    os.makedirs(dir)

    outputName = "caliber_" # output prefix- please don't change
    outputName += str(i)
    outputName += ".mp4"

    shutil.copy2(prefix + str(i) + "_" + str(0) + ".png", dir)
    shutil.copy2(prefix + str(i) + "_" + str(1) + ".png", dir)
    shutil.copy2(prefix + str(i) + "_" + str(2) + ".png", dir)
    shutil.copy2(prefix + str(i) + "_" + str(3) + ".png", dir)
    shutil.copy2(prefix + str(i) + "_" + str(2) + ".png", dir + "/" + prefix + str(i) + "_" + str(4) + ".png")
    shutil.copy2(prefix + str(i) + "_" + str(1) + ".png", dir + "/" + prefix + str(i) + "_" + str(5) + ".png")

    # Don't even ask idk either anymore lol. it works so don't fuck with it
    os.system("ffmpeg -f image2 -r 12 -i " + dir + "/cimg_" + str(i) + "_%d.png -vcodec mpeg4 -y " + dir + "/" + str(outputName))
    f = open(dir + "/cat.txt","w+")
    for i in range(4):
        f.write("file '%s'\n" % (outputName))
    f.close()

    command="ffmpeg -safe 0 -f concat -i %s/cat.txt -c copy %s/looped.mp4" %(dir,dir)
    os.system(command)
    

# "IF I CAN'T BE THE BEST, I SURE AS HELL CAN BE THE WOOOOOORSSSTTTTTTT!" - Jon Jafari ( https://www.youtube.com/watch?v=RSKmPP7ckzU )
# Stay inspired <3
