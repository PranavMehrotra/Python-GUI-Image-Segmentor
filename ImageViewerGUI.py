####### REQUIRED IMPORTS FROM THE PREVIOUS ASSIGNMENT #######
from my_package.data import dataset
from my_package.model import InstanceSegmentationModel
from my_package.data import Dataset
from my_package.analysis import plot_visualization
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
import PIL.Image
import numpy as np

####### ADD THE ADDITIONAL IMPORTS FOR THIS ASSIGNMENT HERE #######
from tkinter import *
from tkinter import filedialog
import PIL.ImageTk as itk
import os

class pm:
    boundimg=""
    segmentimg=""
# Define the function you want to call when the filebrowser button is clicked.
def fileClick(clicked, segmentor):
	####### CODE REQUIRED (START) #######
    filetypes = (
        ('JPG files', '*.jpg'),
        ('PNG files', '*.png')
    )
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=filetypes)
    if(type(file_path)==type(" ") and file_path!=""):
        file_lab.config(text=os.path.basename(file_path))
    else:
        root.deiconify()
        return
    root.deiconify()
    data = Dataset(file_path,transforms)
    img_arr = data.__getitem__(0)["image"]
    h,w,r = img_arr.shape
    ncopy = np.empty((3,h,w))
    for j in range(h):
        for k in range(w):
            ncopy[0][j][k] = img_arr[j][k][0]
            ncopy[1][j][k] = img_arr[j][k][1]
            ncopy[2][j][k] = img_arr[j][k][2]
    pred_boxes, pred_masks, pred_class, pred_score = segmentor.__call__(ncopy)
    pred_masks = np.array(pred_masks)
    nimg = PIL.Image.fromarray(np.uint8(img_arr*255))
    copied = PIL.Image.fromarray(np.uint8(img_arr*255))
    pm.segmentimg, pm.boundimg = plot_visualization(pred_boxes, pred_masks, pred_class, pred_score,nimg,copied,h,w)
    mainimg = itk.PhotoImage(PIL.Image.fromarray(np.uint8(img_arr*255)))
    if(clicked.get()=="Bounding-box"):
        neximg = itk.PhotoImage(pm.boundimg)
    else:
        neximg = itk.PhotoImage(pm.segmentimg)
    mainimage.config(image=mainimg)
    mainimage.image=mainimg
    nextimage.config(image=neximg)
    nextimage.image=neximg
    nextimage.place(x=40+w,y=130)
	####### CODE REQUIRED (END) #######

# `process` function definition starts from here.
# will process the output when clicked.
def process(clicked):
	####### CODE REQUIRED (START) #######
    if(type(pm.boundimg)==type("")):
        file_lab.config(text="Select an Image first.")
        return
    if(clicked.get()=="Bounding-box"):
        neximg = itk.PhotoImage(pm.boundimg)
    else:
        neximg = itk.PhotoImage(pm.segmentimg)
    nextimage.config(image=neximg)
    nextimage.image=neximg
	####### CODE REQUIRED (END) #######

# `main` function definition starts from here.
if __name__ == '__main__':
	####### CODE REQUIRED (START) ####### (2 lines)
	# Instantiate the root window.
	# Provide a title to the root window.
    root = Tk()
    root.geometry("1600x900")
    root.title("Hello!")
	####### CODE REQUIRED (END) #######

	# Setting up the segmentor model
    annotation_file = './data/annotations.jsonl'
    transforms = []
	# Instantiate the segmentor model.
    segmentor = InstanceSegmentationModel()
	# Declare the options.
    options = ["Segmentation", "Bounding-box"]
    clicked = StringVar()
    clicked.set(options[0])
	####### CODE REQUIRED (START) #######
	# Declare the file browsing button
    mainimage = Label(root, text="")
    nextimage = Label(root, text="")
    mainimage.place(x=20,y=130)
    lab = Label(root, text="Click on the button to select a file.")
    lab.grid(row=0,column=0)
    file_lab = Label(root,text="")
    file_lab.grid(row=1,column=1)
    sel = Button(root, text="Select a file",command=lambda: fileClick(clicked,segmentor))
    sel.grid(row=1, column=0)
	# Declare the drop-down button
    drop = OptionMenu( root , clicked , *options )
    drop.place(x=20,y=80)
	####### CODE REQUIRED (END) #######
	# This is a `Process` button, check out the sample video to know about its functionality
    myButton = Button(root, text="Process", command=lambda: process(clicked))
    myButton.place(x=200,y=80)
	####### CODE REQUIRED (START) ####### (1 line)
	# Execute with mainloop()
    root.mainloop()
	####### CODE REQUIRED (END) ######