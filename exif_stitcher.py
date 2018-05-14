import datetime
import time
import PIL
from PIL import Image
## open file location of altitdue data
import os, sys


def EXIF_stitch(photo_string, alti_string):
    photo_list = []
    alti_list = []

    newFile = open("new_EXIF.txt", "w+")

    ## Include ability to enter in user data
    alti_path = open(str(alti_string), "r+")
    for line in alti_path:
        alti_list.append(line)

    ## Get path to photos and iterate through directory
    photo_path = str(photo_string)

    photo_dir = os.listdir(photo_path)

    # f_count = 0
    # p_count = 0
    quality_check = 0
    for file in photo_dir:
        image_temp = str(Image.open(str(photo_string) + "/" + file + "")._getexif()[36867])
        # print image_temp, file
        check = True
        i = 0
        while check:
            if image_temp.split()[1] == str(alti_list[i]).split()[1]:
                # Tie data to image, write to new file
                newFile.write(file + "," + "-" + "," + "-" + "," + alti_list[i].split()[2] + "\n")
                check = False
            else:
                i = i + 1
        quality_check = quality_check + 1

    # attempt to get exif data from camera
    # image_temp = str(Image.open("/home/alex/Documents/BenthicMapper/PI/Scorpion_Bay/G0062796.JPG")._getexif()[36867])
    # print test_alti
    # print image_temp
    #
    # test_temp_alti = test_alti.split()[0] + " " + test_alti.split()[1]
    # print test_temp_alti
    # #
    # if image_temp == test_temp_alti:
    #     print "True"
    # else:
    #     print "FALSE"

    print quality_check
