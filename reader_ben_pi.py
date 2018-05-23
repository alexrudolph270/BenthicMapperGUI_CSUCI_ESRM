
# Python code to take data from the Arduino serial port
# Alex Rudolph
# Benthic Mapper Project

import datetime
import serial
import time

def readData(ardu_port, timeInput):
    ## initialize file with current date/time as filename
    currDT = datetime.datetime.now()
    # print(str(currDT))

    newFile = open(str(currDT) + ".txt", "wb")
    print ("Name of file: " + newFile.name)

    ser = serial.Serial(str(ardu_port), 9600, timeout=1)
    # Note to self, make this editable by user
    #  Add in user_input

    # Maybe add in date and time for orginization purposes
    # try:
    #     while True:
    #         line = ser.readline()   # read a '\n' terminated line
    #         # newFile.write(str(datetime.datetime.now()) + " ")
    #         newFile.write(line)
    #         print(line)
    # except KeyboardInterrupt:
    #     print("Process Ended")

    # Ask for time duration
    # userInput = input("Enter how long to record: ")
    timeout = time.time() + (int(timeInput) * 60) # convert seconds to minutes

    fileWriteSkip = 0

    while True:
            line = ser.readline()   # read a '\n' terminated line

            ## format date and time for output, then write to files
            timeStamp = str(datetime.datetime.now())

            ##--##
            time_to_replace = datetime.datetime.strptime(timeStamp.split()[1][0:8], "%H:%M:%S")
            #            Edit (Seconds, Minutes, Hours)         S      M H
            edit_time = time_to_replace + datetime.timedelta(0,2,0,0,48,11)
            corrected_time = str(edit_time).split()[1][0:8]

            # print corrected_time

            # EDIT YEAR

            date_to_replace = datetime.datetime.strptime(timeStamp.split()[0], "%Y-%m-%d")
            edit_date = date_to_replace + datetime.timedelta(3,0,0,0,0,0,14)
            temp_edit_date = str(edit_date).replace("-",":")
            corrected_date = str(temp_edit_date).split()[0]

            temp_time = timeStamp.replace(timeStamp.split()[1], corrected_time)
            new_time = temp_time.replace(timeStamp.split()[0], corrected_date)

            ##--##
            fileWriteSkip = fileWriteSkip + 1

            if fileWriteSkip > 1:
                newFile.write(new_time)
                newFile.write(" " + line)
                print(line)

            if time.time() > timeout:
                break

    # stop on user uInput
    print("Recording ended")

    ser.close()

    newFile.close()
