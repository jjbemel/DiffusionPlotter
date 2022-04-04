# DiffusionPlotter v0.9.0
Latest release: 04/04/22

Reads a timed sequence of photos to plot color concentration over distance to map diffusion

### Prepackaged
A prepackaged distribution file is available with Python3, imports, Fiji, and macros all included.

https://drive.google.com/file/d/1gZplh6--yVFVtfwImEBzn34hL514XvHI/view?usp=sharing

### Requires: 
- Fiji folder in DiffusionPlotter.py file's directory
- In /Fiji/macros/ place the AutoCalibSlice.ijm and AutoCalibTimed.ijm files
- Mapped photos are in a seperate folder
- Photos listed alphabetically in folder, in chronological order (i.e. photo1, photo2; A, B, C; etc.)

### Checklist
- [x] Fiji Auto Calibrate
- [x] Tkinter GUI
- [x] Timed Photo Reader
- [ ] Slice Photo Reader
- [x] Commented Code
- [ ] Distance mapper (Timed Photos)
- [x] Prepackage executable
- [x] Moving Average Button
- [ ] Diffusivity Calculation
- [x] Subtract Noise Floor (remove noise checkbox)
- [x] Show Photo with OpenCV Line Selection drawn
- [ ] Cut down prepackage size (import specific modules rather than total)
