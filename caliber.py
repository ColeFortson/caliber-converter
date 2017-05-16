#!/usr/bin/python
import os
group = 0
outputName = "caliber_"
outputName += str(group)
outputName += ".mp4"


# file 'input.mp4'

f= open("cat.txt","w+")

for i in range(4):
    f.write("file '%s'\r\n" % (outputName))

os.system("ffmpeg -f image2 -r 12 -i cimg_00_%2d.png -vcodec mpeg4 -y " + str(outputName))
os.system("ffmpeg -f concat -i cat.txt -codec copy output.mp4")
