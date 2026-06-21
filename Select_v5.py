import os
from os.path import splitext
from tkinter import *
from tkinter import filedialog
import shutil
import csv

names = []

latestPath = '.'

sourcePath = ''
csvFile = ''
destinationPath = ''


# ---------------- GUI FUNCTIONS ----------------

def sourceFolder():
    global sourcePath, latestPath

    sourcePath = filedialog.askdirectory(
        initialdir=latestPath,
        title="Select the source directory"
    )

    latestPath = sourcePath
    label_displaySelected.configure(text="Folder Selected: " + sourcePath)


def selectCsvFile():
    global csvFile, latestPath

    csvFile = filedialog.askopenfilename(
        initialdir=latestPath,
        title="Select the CSV file",
        filetypes=(("CSV files", "*.csv*"), ("TXT files", "*.txt*"))
    )

    latestPath = csvFile
    label_displaySelected.configure(text="File Selected: " + csvFile)


def target():
    global destinationPath, latestPath

    destinationPath = filedialog.askdirectory(
        initialdir=latestPath,
        title="Select the target directory"
    )

    latestPath = destinationPath
    label_displaySelected.configure(text="Folder Selected: " + destinationPath)


# ---------------- CORE LOGIC ----------------

def runCopy():
    global names

    if not sourcePath or not csvFile or not destinationPath:
        label_displaySelected.configure(text="Please select all folders + CSV first")
        return

    names.clear()

    # ---------- READ CSV PROPERLY ----------
    header_index = None

    with open(csvFile, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)

        for row in reader:
            if not row:
                continue

            # find header row dynamically
            if header_index is None:
                if "Name" in row:
                    header_index = row.index("Name")
                continue

            if header_index >= len(row):
                continue

            filename = row[header_index].strip()
            if filename:
                names.append(filename)

    # ---------- SOURCE FILES ----------
    directory = os.listdir(sourcePath)

    # map filename WITHOUT extension -> full file
    directory_map = {splitext(f)[0]: f for f in directory}

    copied = 0

    # ---------- COPY ----------
    for name in names:
        key = splitext(name)[0]  # remove extension if CSV includes it

        if key in directory_map:
            src_file = os.path.join(sourcePath, directory_map[key])
            dst_file = os.path.join(destinationPath, directory_map[key])

            shutil.copyfile(src_file, dst_file)

            copied += 1
            label_displaySelected.configure(text=f"Copied: {directory_map[key]}")
            rootWindow.update()

    label_displaySelected.configure(text=f"Done! Copied {copied} files.")


# ---------------- UI ----------------

rootWindow = Tk()

rootWindow_height = 300
rootWindow_width = 300

screen_width = rootWindow.winfo_screenwidth()
screen_height = rootWindow.winfo_screenheight()

center_x = int(screen_width / 2 - rootWindow_width / 2)
center_y = int(screen_height / 2 - rootWindow_height / 2)

rootWindow.title('Select and Copy')
rootWindow.geometry(f'{rootWindow_height}x{rootWindow_width}+{center_x}+{center_y}')
rootWindow.config(background="white")

label_displaySelected = Label(
    rootWindow,
    text="Select and Copy",
    width=40,
    height=4,
    fg="black"
)

button_source = Button(rootWindow, text="Set source directory", command=sourceFolder)
button_file = Button(rootWindow, text="Choose CSV file", command=selectCsvFile)
button_destination = Button(rootWindow, text="Choose target directory", command=target)
button_runCopy = Button(rootWindow, text="Select and copy files", command=runCopy)

label_displaySelected.place(relx=0.5, rely=0.1, anchor=CENTER)
button_source.place(relx=0.5, rely=0.4, anchor=CENTER)
button_file.place(relx=0.5, rely=0.5, anchor=CENTER)
button_destination.place(relx=0.5, rely=0.6, anchor=CENTER)
button_runCopy.place(relx=0.5, rely=0.8, anchor=CENTER)

rootWindow.mainloop()