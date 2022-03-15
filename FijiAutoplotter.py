#!/bin/python3

#Package imports
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

# functions for tkinter button actions

def TimedDir():
    VarDir3.set(fd.askdirectory(title="Please Select Timed Photos Folder"))

def SliceDir():
    VarDir4.set(fd.askdirectory(title="Please Select Slice Photos Folder"))

def runFijiTimed(): #get program working directory & launch Fiji w/ Timed photo calibration
    cwd = os.getcwd()
    Fiji = cwd+'/Fiji.app/ImageJ-win64.exe -macro AutoCalibTimed'
    sub.run(Fiji)

def runFijiSlice(): #get program working directory & launch Fiji w/ Slice photo calibration
    cwd = os.getcwd()
    Fiji = cwd+'/Fiji.app/ImageJ-win64.exe -macro AutoCalibSlice'
    sub.run(Fiji)

def runTimed(): #run timed photo function for plotting intensity over distance at 4 time intervals
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
            with open('Fiji.app/pixlenTimed.txt') as f:
                length = f.readline()
                length = length.rstrip('\n')
                length = float(length) / 5
            xTimed= np.arange(img.shape[1])/length
            yTimed = img[row][:]
            if indexnum == 0:
                smallest = min(yTimed)
            yTimed = [float(smallest)-float(each) for each in yTimed]
            yTimed = [(((each + 1e-20) / float(abs(min(yTimed)))) + 1) for each in yTimed]
            if VarConc.get() == 1:
                yTimed = [each * float(concentration.get()) for each in yTimed]
            # print(yTimed) # DEBUG TO READ GRAY VALUES
            a.plot(xTimed,yTimed,linewidth=1)
            indexnum += 1
    a.set_xlabel('Distance (mm)')
    if VarConc.get() == 1:
        a.set_ylabel('Concentration (mol/m^3')
    else:
        a.set_ylabel('Intensity')
    canvas = FigureCanvasTkAgg(fig, master=topRFrame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0)
    toolbarFrame = Frame(master=botLFrame)
    toolbarFrame.grid(row=0, column=0)
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

def runSlice():
    # NOT COMPLETED YET
    #with open('/Fiji.app/pixlenSlice.txt') as f:
        #length = f.readline()
        #length = length.rstrip('\n')
        #length = float(length) / 5
    return

def runfunc(): #run button, condition based command execution
    if VarTimed.get() == 1:
        if VarFijiT.get() ==1:
            runFijiTimed()
        runTimed()
    if VarSlice.get() == 1:
        if VarFijiS.get() ==1:
            runFijiSlice()
        runSlice()

# Variables
# only accept picture file types
PicExtension = [".bmp", ".jpg", ".jpeg", ".jp2", ".png", ".webp",
                ".pbm", ".pgm", ".ppm", ".pxm", ".pnm", ".pfm",
                ".tiff", ".tif", ".exr"]


########## TKINTER GUI BUILDER ##########

root = Tk()
root.title("Diffusion Photos Auto Plotter v0.8 | CHE 482 Team Brain") #title of window
#root.state('zoomed')

### Top Frame ###
topFrame = LabelFrame(root,bd=3)
topFrame.grid(row=0,column=0,padx=5,sticky=W)

# Top Frame
# Required
top1Frame = LabelFrame(topFrame, text="Required",bd=3, font='Helvetica 12 bold')
top1Frame.grid(row=0,column=0,padx=5,ipady=30,stick=E+W)
VarTimed = IntVar()
NeedTimed = Checkbutton(top1Frame, text="Plot Timed Photos?",variable=VarTimed).grid(row=0,column=0,stick=W)
VarSlice = IntVar()
NeedSlice = Checkbutton(top1Frame, text="Plot Sliced Photos?",variable=VarSlice).grid(row=1,column=0,stick=W)
VarConc = IntVar()
NeedConc = Checkbutton(top1Frame, text="Use concentration instead of intensity",variable=VarConc).grid(row=2,column=0)
concLabel = Label(top1Frame, text="Concentration (mol/m^3):").grid(row=3,column=0)
concentration = Entry(top1Frame, width=10)
concentration.grid(row=3,column=1)
concentration.insert(0,"1.25")


# Top Frame
# Timed Photos
top3Frame = LabelFrame(topFrame, text="Timed Photos",bd=3, font='Helvetica 12 bold')
top3Frame.grid(row=1,column=0,padx=5,ipady=50,sticky=E+W)
dirButton3 = Button(top3Frame, text="Select Timed Photos Folder", command=TimedDir).grid(row=0,column=0,sticky=W)
VarDir3 = StringVar()
dir3 = Label(top3Frame, textvariable=VarDir3).grid(row=0,column=1)
VarFijiT = IntVar()
NeedFijiT = Checkbutton(top3Frame, text="Run Timed Photos Fiji Calibration?",variable=VarFijiT).grid(row=1,column=0,stick=W)
timeLabel = Label(top3Frame, text="Total Experiment Time (hrs):").grid(row=2,column=0)
totTime = Entry(top3Frame, width=10)
totTime.grid(row=2,column=1,sticky=W)
totTime.insert(0,"6")

# Top Frame
# Slices
top4Frame = LabelFrame(topFrame, text="Slice Photos",bd=3, font='Helvetica 12 bold')
top4Frame.grid(row=2,column=0,padx=5,ipady=50,sticky=E+W)
dirButton4 = Button(top4Frame, text="Select Slice Photos Folder", command=SliceDir).grid(row=0,column=0,sticky=W)
VarDir4 = StringVar()
dir4 = Label(top4Frame, textvariable=VarDir4).grid(row=1,column=0)
VarFijiS = IntVar()
NeedFijiS = Checkbutton(top4Frame, text="Run Slice Photos Fiji Calibration?",variable=VarFijiS).grid(row=1,column=0,stick=W)
emptyLabel1 = Label(top4Frame,text=" ").grid(row=2,column=0)
cutsLabel = Label(top4Frame, text= "Select the number of slices:").grid(row=3,column=0)
r = IntVar()
Radiobutton(top4Frame, text="3 Cuts (4 photos)",variable=r,value=1).grid(row=4,column=0)
Radiobutton(top4Frame, text="5 Cuts (6 photos)",variable=r,value=2).grid(row=5,column=0)
ConstructionLabel = Label(top4Frame, text="Section Not Implemented", font='Helvetica 12 bold').grid(row=6,column=0)

# Top Right Frame
# Plots
topRFrame = LabelFrame(topFrame, text="Plot",bd=3, font='Helvetica 12 bold')
topRFrame.grid(row=0,column=1,rowspan=3)
canvas = Canvas(topRFrame).grid()

### Bottom Frame ###
botFrame = LabelFrame(root,text="",bd=3)
botFrame.grid(row=1,column=0,padx=5,ipady=20)

# Bottom Left Frame
# Console, Run, Close
botLFrame = LabelFrame(botFrame, text="Functions",bd=3, font='Helvetica 10 bold')
botLFrame.grid(row=0,column=0,padx=5,ipady=10)
ConsoleButton = Label(botLFrame, text="Console").grid(row=0,column=0,padx=150)
emptyLabel2 = Label(botLFrame,text=" ").grid(row=1,column=0)
RunButton = Button(botLFrame, text="Run", command= runfunc).grid(row=2,column=0)
emptyLabel3 = Label(botLFrame,text=" ").grid(row=3,column=0)
CloseButton = Button(botLFrame, text="Close",command=root.quit).grid(row=4,column=0)

# Bot Right Frame
# Credits
botRFrame = LabelFrame(botFrame, text="Credits",bd=3, font='Helvetica 10 bold')
botRFrame.grid(row=0,column=1,padx=5,ipady=20)
testLabelbr1 = Label(botRFrame, text="CHE 482 Team Brain  |  Last Updated: 03/06/2022").grid()
testLabelbr2 = Label(botRFrame, text="").grid()
testLabelbr3 = Label(botRFrame, text="Python 3.10.2 | Java 1.9.0_172 (64-bit) | ImageJ 1.53o").grid()
testLabelbr4 = Label(botRFrame, text="Python Libraries:").grid()
testLabelbr5 = Label(botRFrame, text="OpenCV, Matplotlib, Tkinter, Numpy, Pandas").grid()

root.mainloop()
