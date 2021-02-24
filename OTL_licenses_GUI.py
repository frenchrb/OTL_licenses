#!/usr/bin/env python

from tkinter import *
from tkinter import filedialog
import OTL_licenses

openpath = ''
savepath = ''

def open():
    global openpath
    openpath = filedialog.askopenfilename()
    #print('openpath: ' + openpath)

def save():
    global savepath
    savepath = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV (Comma Delimited)', '.csv')])
    #print('savepath: ' + savepath)

def run():
    OTL_licenses.main(openpath, savepath)
    root.destroy()

root = Tk()
root.wm_title('OTL Licenses')

inButton = Button(root, text='Select Input File (.csv)...', height=2, width=25, command=open)
inButton.grid(row=2)

outButton = Button(root, text='Save As...', height=2, width=25, command=save)
outButton.grid(row=3)

runButton = Button(root, text='Run', height=2, width=25, command=run)
runButton.grid(row=5)

root.mainloop()
