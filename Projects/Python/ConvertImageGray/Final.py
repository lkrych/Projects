from scipy import misc
import numpy as np
from Tkinter import * #import tkinter library which produces gui
import tkFileDialog as filedialog # import tkFileDialog which presents GUI for selecting file

def select_filename():
    root = Tk() #opens a window
    #saving the results of askopenfilename to root.filename
    root.fileNames = filedialog.askopenfilenames()  #select file names, produces a tuple

    files = []
    files += root.fileNames #save files selected into list

    return files

def makeGray(im):
    address = im #save address of image so that you can resave the image later
    image = misc.imread(im) #saves image as image

    grey = np.zeros((image.shape[0],image.shape[1])) #initialize an empty array with the dimensions of the image
    for row in range(image.shape[0]): #cycle through each row
        for col in range(image.shape[1]): #cycle through each column
            grey[row][col]= np.average(image[row][col]) #save the average color to the array
    file_path = address[:address.find('.')] + '-gray' + '.png' #use string method to find file suffix and add -gray to path
    misc.imsave(file_path, grey ) #save file

def testGray():
    '''
    Allows the user to select files, and then iterates through each file  and makes them gray.
    '''
    files = select_filename()
    for file in files:
        makeGray(file)
    print 'done'

testGray()

