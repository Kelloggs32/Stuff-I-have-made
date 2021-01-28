#TK-ext by Kaylem Madden - TK-ext is a text editor coded in Python using the Tkinter module.


#imports

from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox
import os
from preferences import *


#main window

root = Tk(className = " TK-ext ")
root.wm_iconbitmap(r'C:\Coding\Python\TK-ext text editor\Tk-ext.ico')
root.geometry("640x480") 
root.resizable(True,True)

textarea = scrolledtext.ScrolledText(width=640, height=480)

#User settings

textarea.config(wrap=text_wrap)
textarea.config(fg=foreground_colour)
textarea.configure(bg=background_colour, insertbackground=insert_background_colour)
textarea.config(font=(pref_font, pref_size))
textarea.config(cursor=pref_cursor)

textarea.pack()

#Functions

def newfile():
    #checks for content
    if len(textarea.get('1.0', END+'-1c')) > 0:
        if messagebox.askyesno("Save", "Do you want to save?"):
            saveFile()
    textarea.delete('1.0', END)
    textarea.update()
    
    

   

def openfile():
    file = filedialog.askopenfile(parent=root, title='Select a text file', filetype=(("Text file", ".txt"), ("All files", "*.*")))                            

    root.title(os.path.basename(file.name) + " - TK-ext")

    if file!= None:
        textarea.delete('1.0', END)
        contents = file.read()
        textarea.insert('1.0', contents)
        textarea.update()
        file.close()

    if file == None:
        contents = file.read()
        textarea.insert('1.0', contents)
        textarea.delete('1.0', END)
        textarea.update()
        file.close()

def savefile():
    file = filedialog.asksaveasfile(parent=root, title='Select a file type', filetype=(("Text file", ".txt"), ("All files", "*.*")))
    if file != None:
        #slice off the last character from get, as an extra return is added
        data = textarea.get('1.0', END+'-1c')
        file.write(data)
        file.close()
        
def Exit():
    if messagebox.askyesno("Exit", "Do you want to quit?"):
        root.destroy()

def about():
    Label = messagebox.showinfo("About", "Made using Python 3.8.4 & tkinter\n by Kelloggs A.K.A. Kaylem Madden")

def Help():
    Label = messagebox.showinfo("Help", "Just check the readme if you need help...")


      
    
        
#menu options
menu = Menu(root)
root.config(menu=menu)
Filemenu=Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=Filemenu)
Filemenu.add_command(label="New", command=newfile)
Filemenu.add_command(label="Open", command=openfile)
Filemenu.add_command(label="Save", command=savefile)
Filemenu.add_separator()
Filemenu.add_command(label="Exit", command=Exit)

#Help menu options
Helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=Helpmenu)
Helpmenu.add_command(label="Help", command=Help)
#Helpmenu.add_command(label="Colour", command=bgcolour)
Helpmenu.add_separator()
Helpmenu.add_command(label="About", command=about)


#keeps the window open
root.mainloop()
