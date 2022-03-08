open(File.openDialog("Pick Calibration Photo"));
while (selectionType() < 0) {
	setTool("line");
	waitForUser("Draw a 5mm calibration line, and press OK when done.");
}
getValue("Length");
DIR = getDirectory("startup");
Output = DIR + "pixlenSlice.txt";
saveAs("Text",Output);
run("Quit");
