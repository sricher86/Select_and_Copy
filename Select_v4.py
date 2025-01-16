import os
from os.path import splitext
from tkinter import *
from tkinter import filedialog
import shutil


#create an empty list that will store filenames from csv
names = []

global latestPath  

#function to call file explorer dialog boxes
def sourceFolder():
    #call file explorer window for source directory
    global sourcePath 
    latestPath = '.'
    sourcePath = filedialog.askdirectory(initialdir = latestPath,
                                         title = "Select the source directory")
    latestPath = sourcePath
    label_displaySelected.configure(text="Folder Selected: "+sourcePath)
    
def csv():
    #call file explorer window for CSV file
    global csvFile
    csvFile = filedialog.askopenfilename(initialdir = '{latestPath}',
                                         title = "Select the CSV or txt file",
                                         filetypes = (("CSV files",
                                                        "*.csv*"),
                                                       ("TXT files",
                                                        "*.txt*")))
    latestPath = csvFile
    label_displaySelected.configure(text="File Selected: "+csvFile)

def target():
    #call file explorer window for target directory
    global destinationPath
    destinationPath = filedialog.askdirectory(initialdir = '{latestPath}',
                                              title = "Select the target directory")
    latestPath = destinationPath
    label_displaySelected.configure(text="Folder Selected: "+destinationPath)

def runCopy():
    global directory
    global directorySplit
    global namesSplit
    # open the file, make a list of all filenames, close the file
    with open(csvFile) as names_file:
        for row in names_file:
            names.append(row)
            
    directory = os.listdir(sourcePath)
    
    for name in names:
        nameSplit = os.path.splitext(name)[0]
        for filename in directory:
            filenameSplit = os.path.splitext(filename)[0]
            print(nameSplit)
            if (nameSplit == filenameSplit):
                extension = os.path.splitext(filename)[1]
                label_displaySelected.configure(text="Current File : "+ filenameSplit)
                # shutil.copyfile(os.path.join(sourcePath + '/', filenameSplit + extension), os.path.join(destinationPath + '/', filenameSplit + extension))
#create Tkinter root window
rootWindow = Tk()

#rootWindow dimensions
rootWindow_height = 300
rootWindow_width = 300

#find screen dimension and calculate center
screen_width = rootWindow.winfo_screenwidth()
screen_height = rootWindow.winfo_screenheight()
center_x = int(screen_width/2 - rootWindow_width / 2)
center_y = int(screen_height/2 - rootWindow_height / 2)

#window properties
rootWindow.title('Select and Copy')
rootWindow.geometry(f'{rootWindow_height}x{rootWindow_width}+{center_x}+{center_y}')
rootWindow.config(background = "white")

label_displaySelected = Label(rootWindow,
                              text = "Select and Copy",
                              width=100, height=4,
                              fg="black")

#Button for calling fileExplorer function
button_source = Button(rootWindow, 
                        text = "Set source directory",
                        command = sourceFolder) 
button_file = Button(rootWindow, 
                        text = "Choose CSV file",
                        command = csv) 
button_destination = Button(rootWindow, 
                        text = "Choose target directory",
                        command = target) 
button_runCopy = Button(rootWindow, 
                        text = "Select and copy files",
                        command = runCopy) 

button_exit = Button(rootWindow, 
                     text="Exit", 
                     command=rootWindow.destroy) 
button_exit.pack(pady=20) 

label_displaySelected.place(relx=0.5, rely=0.1, anchor=CENTER)
button_source.place(relx=0.5, rely=0.3, anchor=CENTER)
button_file.place(relx=0.5, rely=0.4, anchor=CENTER)
button_destination.place(relx=0.5, rely=0.5, anchor=CENTER)
button_runCopy.place(relx=0.5, rely=0.7, anchor=CENTER)
button_exit.place(relx=0.5, rely=0.8, anchor=CENTER)


rootWindow.mainloop()

