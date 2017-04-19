from tkinter.filedialog import *

import shutil

import os



# Function to select a folder.
def directory(event):

    global open_dir
    open_dir = askdirectory()+'/'
    os.chdir(open_dir)
    print(open_dir)

def click(event):

    if 'open_dir' not in globals():
        print('Please specify the path!')
        global open_dir
        open_dir = askdirectory() + '/'
        os.chdir(open_dir)
        print(open_dir)
    else:
        pass

    files_list = os.listdir(str(open_dir))
    print('This is your files in '+str(open_dir)+': '+str(files_list))

    # Create folders.
    if 'doc' not in files_list:
        os.mkdir('doc')
    if 'img' not in files_list:
        os.mkdir('img')

    # Change path.
    open_dir_doc = open_dir + 'doc/'
    open_dir_img = open_dir + 'img/'

    i = 0
    for _ in files_list:
        a = os.path.splitext(files_list[i])
        print(files_list[i])
        print(a)

        # Two variables with formats.
        docs = ['.txt', '.doc', '.pdf', '.pptx', '.docx']
        images = ['.png', '.jpg', '.bmp', '.jpeg']

        if a[1] in docs:
            shutil.move(files_list[i], open_dir_doc)
        elif a[1] in images:
            shutil.move(files_list[i], open_dir_img)
        i += 1
    print('*** End script ***')
    exit()

# Interface.
root = Tk()

root.wm_title('DesktopCleaner')
root.minsize(width = 265, height = 250)

button_dir = Button(root, text = 'Select Directory \"Desktop\"', width = 25, bg = 'grey', fg = 'white', font="Arial 18")
button_dir.pack()
button_dir.bind('<Button-1>', directory)

button_run = Button(root, text = 'Run program now', width = 25, bg = 'grey', fg = 'white', font="Arial 18")
button_run.pack()
button_run.bind('<Button-1>', click)

root.mainloop()