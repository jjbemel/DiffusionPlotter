DIR = getDir("Choose a Working Directory");

open(File.openDialog("Pick Calibration Photo"));

while (selectionType() < 0) {
	setTool("line");
	waitForUser("Draw a calibration line, and press OK when done.");
}
run("Set Scale...");
close("*");
//Open file 1
open(File.openDialog("Pick Final Photo (4/4) | *Selecting Photos in Reverse Order*"));
while (selectionType() < 0) {
	setTool("line");
	waitForUser("Draw a line to plot values across, and press OK when done.");
}
run("Plot Profile");
Plot.showValues();
path1 = DIR+"Export1.csv";
saveAs("results", path1);
close("*");

//Open file 2
open(File.openDialog("Pick In-Progress Photo 3/4"));
run("Restore Selection");
run("Plot Profile");
Plot.showValues();
path2 = DIR+"Export2.csv";
saveAs("results", path2);
close("*");

//Open file 3
open(File.openDialog("Pick In-Progress Photo 2/4"));
run("Restore Selection");
run("Plot Profile");
Plot.showValues();
path3 = DIR+"Export3.csv";
saveAs("results", path3);
close("*");

//Open file 4
open(File.openDialog("Pick In-Progress Photo 1/4"));
run("Restore Selection");
run("Plot Profile");
Plot.showValues();
path4 = DIR+"Export4.csv";
saveAs("results", path4);
close("*");
run("Quit");
