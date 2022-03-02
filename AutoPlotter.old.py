# Fiji Autoplotter by Jon Jay Bemel
# Updated 2/22/2022

import subprocess as sub
import pandas as pd
import matplotlib.pyplot as plt
import tkinter.filedialog as fd

global export
global directory
global concentration
global dir

def CSVgrab():
    global cols
    global dist
    global label
    global file

    howmany = 4

    totaltime = int(input("\nTotal time in experiment (hours): "))
    concentration = float(input("Initial concentration (mol/m^3): "))
    file = [dir+"/export1.csv",dir+"/export2.csv",dir+"/export3.csv",dir+"/export4.csv"]
    cols = [[] for _ in range(int(howmany))]
    label = [[] for _ in range(int(howmany))]
    i = 0
    while i < int(howmany):
        label[i] = "t= "+ str(((totaltime*60) / (howmany-1))*(howmany-1-i))
        data = pd.read_csv(file[i], names=["Distance", "Greyvalue"])
        dist = data.Distance.to_list()
        dist.pop(0)
        dist[:] = [float(each) for each in dist]
        col = data.Greyvalue.to_list()
        col.pop(0)
        col[:] = [float(each) for each in col]
        if i == 0:
            minimum = min(col)
        col[:] = [float(minimum) - float(each) for each in col]
        mag = abs(min(col))
        col[:] = [(((each + 1e-20) / float(mag)) + 1)*concentration for each in col]
        cols[i].append(col)
        i += 1

def plotter():
    k = 0
    for each in cols:
        plt.plot(dist, each[0], label=label[k])
        k += 1
    plt.ylabel('Concentration (mol/m^3)')
    plt.xlabel('Distance (mm)')
    plt.legend()
    if export == "export":
        directory = fd.asksaveasfilename(title="Save Graph")
        plt.savefig(directory, bbox_inches='tight')
    else:
        plt.show()

print("----------------------------------")
print("Fiji Auto Plotter by Jon Jay Bemel")
print("For CHE 482 - Team Brain Project")
print("----------------------------------\n")
needfiji = input("Do you need to run Fiji? (y/n): ")
if needfiji == "y":
    print("Open and follow the Fiji instructions...")
    Fiji = fd.askopenfilename(title="Please select Fiji.exe") + ' -macro AutoFiji'
    sub.run(Fiji)
print("\n*Please select working directory with CSV files in it.*")
dir = fd.askdirectory(title="Please select working directory")
CSVgrab()
export = input("\nDo you want to export or view the graph? (export/view): ")
plotter()
