#!/bin/python3

import os
import cv2
import matplotlib.pyplot
import numpy as np
import subprocess as sub
import pandas as pd
import matplotlib.pyplot as plt
import tkinter.filedialog as fd
from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


PicExtension = [".bmp", ".jpg", ".jpeg", ".jp2", ".png", ".webp",
                ".pbm", ".pgm", ".ppm", ".pxm", ".pnm", ".pfm",
                ".tiff", ".tif", ".exr"]


def TimedDir():
    VarDir3.set(fd.askdirectory(title="Please Select Timed Photos Folder"))

def SliceDir():
    VarDir4.set(fd.askdirectory(title="Please Select Slice Photos Folder"))

def runFijiTimed():
    cwd = os.getcwd()
    Fiji = cwd+'/Fiji.app/ImageJ-win64.exe -macro AutoCalibTimed'
    sub.run(Fiji)

def runFijiSlice():
    cwd = os.getcwd()
    Fiji = cwd+'/Fiji.app/ImageJ-win64.exe -macro AutoCalibSlice'
    sub.run(Fiji)

def runTimed():
    fig = plt.figure()
    a = fig.add_subplot(111)
    indexnum = 0
    for name in reversed(os.listdir(VarDir3.get())):
        filename, extension = os.path.splitext(name)
        fullpath = VarDir3.get()+"/"+filename+extension
        if extension in PicExtension:
            # print(fullpath) # DEBUG FOR FILE READ ORDERING
            img = cv2.imread(fullpath,0)
            minimum = min(img.flatten())
            i, j = np.where(img == minimum)
            row = i[0]
            with open('pixlenTimed.txt') as f:
                length = f.readline()
                length = length.rstrip('\n')
                length = float(length) / 5
            xTimed= np.arange(img.shape[1])/length
            yTimed = img[row][:]
            if indexnum == 0:
                smallest = min(yTimed)
            yTimed = [float(smallest)-float(each) for each in yTimed]
            yTimed = [(((each + 1e-20) / float(abs(min(yTimed)))) + 1) for each in yTimed]
            # if concCheck == 1:
            #     yTimed = yTimed * concentration
            # print(yTimed) # DEBUG TO READ GRAY VALUES
            a.plot(xTimed,yTimed,linewidth=1)
            indexnum += 1
    a.set_xlabel('Distance (mm)')
    a.set_ylabel('Intensity')
    canvas = FigureCanvasTkAgg(fig, master=topRFrame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0)
    toolbarFrame = Frame(master=botLFrame)
    toolbarFrame.grid(row=0, column=0)
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

def runSlice():
    # NOT COMPLETED YET
    return

def runfunc():
    if VarTimed.get() == 1:
        runFijiTimed()
        runTimed()
    if VarSlice.get() == 1:
        runFijiSlice()
        runSlice()





########## TKINTER GUI BUILDER ##########

root = Tk()
root.title("Fiji Auto Plotter | CHE 482 Team Brain")
#root.state('zoomed')

### Top Frame ###
topFrame = LabelFrame(root,bd=3)
topFrame.grid(row=0,column=0,padx=5,sticky=W)

# Top Frame
# Required
top1Frame = LabelFrame(topFrame, text="Required",bd=3)
top1Frame.grid(row=0,column=0,padx=5,ipady=30)
concLabel = Label(top1Frame, text="Concentration (mol/m^3):").grid(row=0,column=0)
concentration = Entry(top1Frame, width=10)
concentration.grid(row=1,column=1,sticky=W)
concentration.insert(0,"1.25")

# Top Frame
# Timed Photos
top3Frame = LabelFrame(topFrame, text="Timed Photos",bd=3)
top3Frame.grid(row=1,column=0,padx=5,ipady=50)
VarTimed = IntVar()
NeedTimed = Checkbutton(top3Frame, text="Plot Timed Photos?",variable=VarTimed).grid()
dirButton3 = Button(top3Frame, text="Select Timed Folder", command=TimedDir).grid(row=1,column=0)
VarDir3 = StringVar()
dir3 = Label(top3Frame, textvariable=VarDir3).grid(row=1,column=1)
timeLabel = Label(top3Frame, text="Total Experiment Time (hrs):").grid(row=2,column=0)
totTime = Entry(top3Frame, width=10)
totTime.grid(row=2,column=1,sticky=W)
totTime.insert(0,"6")

# Top Frame
# Slices
top4Frame = LabelFrame(topFrame, text="Slice Photos",bd=3)
top4Frame.grid(row=2,column=0,padx=5,ipady=50)
VarSlice = IntVar()
NeedSlice = Checkbutton(top4Frame, text="Plot Sliced Photos?",variable=VarSlice).grid()
dirButton4 = Button(top4Frame, text="Select Slice Folder", command=SliceDir).grid(row=1,column=0)
VarDir4 = StringVar()
dir4 = Label(top4Frame, textvariable=VarDir4).grid(row=1,column=1)
emptyLabel1 = Label(top4Frame,text=" ").grid(row=2,column=0)
cutsLabel = Label(top4Frame, text= "Select the number of slices:").grid(row=3,column=0)
r = IntVar()
Radiobutton(top4Frame, text="3 Cuts (4 photos)",variable=r,value=1).grid(row=4,column=0)
Radiobutton(top4Frame, text="5 Cuts (6 photos)",variable=r,value=2).grid(row=5,column=0)

# Top Right Frame
# Plots?
topRFrame = LabelFrame(topFrame, text="Plots",bd=3)
topRFrame.grid(row=0,column=1,rowspan=3)
canvas = Canvas(topRFrame).grid()


### Bottom Frame ###
botFrame = LabelFrame(root,text="",bd=3)
botFrame.grid(row=1,column=0,padx=5,ipady=20)

# Bottom Left Frame
# Console, Run, Close
botLFrame = LabelFrame(botFrame, text="Functions",bd=3)
botLFrame.grid(row=0,column=0,padx=5,ipady=10)
ConsoleButton = Label(botLFrame, text="Console").grid(row=0,column=0,padx=150)
emptyLabel2 = Label(botLFrame,text=" ").grid(row=1,column=0)
RunButton = Button(botLFrame, text="Run", command= runfunc).grid(row=2,column=0)
emptyLabel3 = Label(botLFrame,text=" ").grid(row=3,column=0)
CloseButton = Button(botLFrame, text="Close",command=root.quit).grid(row=4,column=0)

# Bot Right Frame
# Credits
botRFrame = LabelFrame(botFrame, text="Credits",bd=3)
botRFrame.grid(row=0,column=1,padx=5,ipady=20)
testLabelbr1 = Label(botRFrame, text="CHE 482 Team Brain").grid()
testLabelbr2 = Label(botRFrame, text="Python 3.10.2 | Java 1.9.0_172 (64-bit) | ImageJ 1.53o").grid()
testLabelbr3 = Label(botRFrame, text="Python Libraries:").grid()
testLabelbr4 = Label(botRFrame, text="OpenCV, Matplotlib, Tkinter, Numpy, Pandas").grid()

root.mainloop()
