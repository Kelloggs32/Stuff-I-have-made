#Tk-ext_compile

import PyInstaller.__main__

PyInstaller.__main__.run([
    'Tk-ext.py',
    '--onefile',
    '--icon=Tk-ext.ico',
    '--windowed'
])
