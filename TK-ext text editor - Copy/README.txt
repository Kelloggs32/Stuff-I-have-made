/INTRO/

Yo wassup, the Tk-ext text editor was made by Kelloggs in Python 3.8.4rc1 and uses the tkinter module. This readme file will help explain some stuff.

/CHANGING TK-EXT'S SETTINGS (i.e. font)/

this can be done by accessing preferences.py. Tk-ext.py treats this file as a module, so it's variables are imported in - such as pref_font

1. change the varaibles value (i.e. pref_size = 30) in preferences.py
2. run Tk-ext_compile.py to recompile the program into an .exe

now you can customise the program to your liking! ;)

 /CHANGING THE PROGRAM ITSELF/

Since this is an open-source text editor (IM SO KIND! UwU) you can do what you want with it, such as editing the source code or changing the compile flags in Tk-ext.py

Tk-ext_compile.py like all compile scripts using pyinstaller takes flags in the format of:

PyInstaller.__main__.run([
    'script.py',
    '--flag',
     '--flag'	
])

if you add any flags make sure to put a comma after the flag above it - if it's the final one, and after it if it isnt (i.e. '--onefile', or '--onefile')

You can edit the source code however you want really... just credit me if you release a variation of Tk-ext or whatever!

/USING TK-EXT/

Using Tk-ext is pretty self-explanatory, just make sure to type the file extension when saving (README.txt instead of just README, or else it'll just be a file).

/END OF README....?/

Now that i've finished this readme and writing Tk-ext what shall i do? Travel the world? Commit defenestration? Get a Girlfriend?

No, probably not - since I'm already BETTER than everyone! A-hah, a-hah! ;)



~Kelloggs