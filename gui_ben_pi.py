# Alex Rudolph
# CSUCI ESRM Lab
# GUI for Benthic Mapper Project

# tkinter interface
# WIll start/stop the recording of data (currently altitude only)
# Saves data to file after complete
# *optional: create a graph for collected data, Maybe display more than altitude

import Tkinter
import tkMessageBox
from Tkinter import *
# import subproces
import tkMessageBox
import tkSimpleDialog

## My own files/classes
# This is to grab incoming data from the Arduino/reader
import reader_ben_pi
import exif_stitcher

tki = Tkinter.Tk()
tki.title('Benthic Mapper PI Interface')

##  Button Frame
button_frame = Frame(tki, bg = '#87ceeb', width = 20, height = 40)
button_frame.grid(row = 0, column = 1, sticky = "ne")

# Going with sky blue for bg
text_frame = Frame(tki, bg = '#87ceeb', width = 800, height = 500, pady = 5, padx = 5)
text_frame.grid(row = 0, sticky = "w")

# text frame to display input, possibly tbOutput
tbInput = Text(text_frame, height = 20, width = 40)
tbInput.grid(row = 0, column = 1)
# Display the tkinter interface

## All of the buttons will be listed here
## Used to perform all actions except for direct text input

# tbInput.insert(END, "Test")

def recordCallBack():
    ## messagebox.showinfo("Start the program")
    ## Subprocess command to enter "ctrl + c", which stops the while loop
    ## subprocess.run(["ls", "-l"])
    usbAskStr = "/dev/ttyUSB" + tkSimpleDialog.askstring("INSERT", "Enter usb port number (i.e. 0,1,2 etc. Typically will be /dev/ttyUSB0):" + "\n")
    tbInput.insert(END, usbAskStr + "\n")

    timeAskStr = tkSimpleDialog.askstring("INSERT", "Enter how long you want to collect data in minutes:" + "\n")
    tbInput.insert(END, timeAskStr + "\n")

    reader_ben_pi.readData(str(usbAskStr), str(timeAskStr))

    tbInput.insert(END,"\n")
    tbInput.insert(END, "Data recording complete" "\n")

recordButton = Tkinter.Button(button_frame, text = "RECORD", width = 5, height = 2, command = recordCallBack)
#deleteButton.pack(side=LEFT)
recordButton.grid(row = 1, column = 1)

# def stopCallBack():
#     ##tkMessageBox.showinfo("Stop the program")
#     ## Subprocess command to enter "ctrl + c", which stops the while loop
#     ## subprocess.kill()
#     reader_ben_pi.closeSerial()
#
# stopButton = Tkinter.Button(button_frame, text = "STOP", width = 5, height = 2, command = stopCallBack)
# #deleteButton.pack(side=LEFT)
# stopButton.grid(row = 2, column = 1)

def exifCallBack():
    # tkMessageBox.showinfo("Print results")
    # Might also be used to display graph
    photoAskStr = tkSimpleDialog.askstring("INSERT", "Enter path to photos:" + "\n")
    tbInput.insert(END, "Enter path to photos: " + photoAskStr + "\n")

    altitudeAskStr = tkSimpleDialog.askstring("INSERT", "Enter path to exif(altitude, depth, etc) data \n Along with the filename:" + "\n")
    tbInput.insert(END, "Enter path to altitude data: " + altitudeAskStr + "\n")

    tbInput.insert(END, "\n")
    tbInput.insert(END, "Creating EXIF data..." + "\n")

    tbInput.insert(END, "\n")
    exif_stitcher.EXIF_stitch(str(photoAskStr), str(altitudeAskStr))

    tbInput.insert(END, "\n")
    tbInput.insert(END, "EXIF creation complete!" + "\n")

exifButton = Tkinter.Button(button_frame, text = "EXIF", width = 5, height = 2, command = exifCallBack)
#deleteButton.pack(side=LEFT)
exifButton.grid(row = 2, column = 1)

# def settingsCallBack():
#     tkMessageBox.showinfo("Change settings in program")
#
# settingsButton = tkinter.Button(button_frame, text = "SETTINGS", width = 5, height = 2, command = settingsCallBack)
# #deleteButton.pack(side=LEFT)
# settingsButton.grid(row = 4, column = 1)

def closeCallBack():
    # tkMessageBox.showinfo("Close the program")
    tki.destroy()


closeButton = Tkinter.Button(button_frame, text = "CLOSE", width = 5, height = 2, command = closeCallBack)
#deleteButton.pack(side=LEFT)
closeButton.grid(row = 3, column = 1)



## Begin loop.  All tkinter code must be before this otherwise it won't appear (I think...)
tki.mainloop()
