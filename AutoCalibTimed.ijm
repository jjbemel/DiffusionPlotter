#!/bin/java

open(File.openDialog("Pick Calibration Photo"));
while (selectionType() < 0) {
	setTool("line");
	waitForUser("Draw a 5mm calibration line, and press OK when done.");
}
getValue("Length");
saveAs("Text","C:/Users/jjbem/PycharmProjects/DesignProj/pixlenTimed.txt");
run("Quit");
