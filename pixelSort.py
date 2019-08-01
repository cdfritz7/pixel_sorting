# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 20:19:47 2018

@author: Connor
"""
from PIL import Image

'''main recursive function for mergesort
inputs: ar - PIL pixelMap to be edited
start - start row or column
end - end row or column
hold - row or column that we are sorting along
isCol - boolean saying whether you are sorting along a row or not

outputs: none'''
def mergeSort(ar, start, end, hold, isCol=True):
    if(start >= end):
        return
    middle = int((start+end)/2)
    mergeSort(ar, start, middle, hold, isCol)
    mergeSort(ar, middle+1, end, hold, isCol)
    merge(ar, start, middle, end, hold, isCol)
    
#merges two sections of ar based on which elements are smaller, helper 
#function for mergesort
def merge(ar, start, middle, end, holdi, isCol=True):
    try:
        if(start > middle or start > end):
            return
        idx1 = start
        idx2 = middle+1
        hidx = 0
        holder = [(0,0,0) for i in range(end-start+1)]
        while(idx1 <= middle and idx2 <=end):
            if(isCol):
                if(ar[idx1, holdi]<=ar[idx2, holdi]):
                    holder[hidx] = ar[idx1, holdi]
                    idx1+=1
                else:
                    holder[hidx] = ar[idx2, holdi]
                    idx2+=1
                hidx+=1
            else:
                if(ar[holdi, idx1]<=ar[holdi, idx2]):
                    holder[hidx] = ar[holdi, idx1]
                    idx1+=1
                else:
                    holder[hidx] = ar[holdi, idx2]
                    idx2+=1
                hidx+=1 
                
        if(idx1 <= middle):
            if(isCol):
                while(idx1<=middle):
                    holder[hidx] = ar[idx1, holdi]
                    idx1+=1
                    hidx+=1
            else:
                while(idx1<=middle):
                    holder[hidx] = ar[holdi, idx1]
                    idx1+=1
                    hidx+=1
                    
        if(idx2 <= end):
            if(isCol):
                while(idx2<=end):
                    holder[hidx] = ar[idx2, holdi]
                    idx2 +=1
                    hidx+=1
            else:
                while(idx2<=end):
                    holder[hidx] = ar[holdi, idx2]
                    idx2 +=1
                    hidx+=1
                    
        for i in range(len(holder)):
            if(isCol):
                ar[start+i, holdi] = holder[i]
            else:
                ar[holdi, start+i] = holder[i]
    except:
        print(f"hold: {holdi}, idx1: {idx1}, idx2: {idx2}, end:{end}, middle: {middle}, start:{start}")
        raise IndexError
            
#sort the columns in pixelMap image from start to end
def sortColumns(image, start, end):
    for i in range(end-start+1):
        mergeSort(image, 0, image.height, i, isCol=True)

#sort the rows in the pixelMap image from start to end
def sortRows(image, start, end):
    for i in range(end-start+1):
        mergeSort(image, 0, image.width, i, isCol=False)

'''sort pixels in a rectangle
inputs:
    image: PIL pixelmap to be edited
    row1: row number of top left pixel
    row2: row number of bottom right pixel
    col1: column number of top left pixel
    col2: column number of bottom right pixel
    which: either 'rows' or 'cols' indicates whether the user wants to sort
    the rectangle along rows or columns
outputs:
    none
'''
def sortRect(image, row1, row2, col1, col2, which='rows'):
    if(which == 'cols'):
        for i in range(col1, col2):
            mergeSort(image, row1, row2, i, isCol=False)
    elif(which=='rows'):
        for i in range(row1, row2):
            mergeSort(image, col1, col2, i, isCol=True)
    else:
        raise ValueError("""'which' parameter of 
pixelSort.sortRect must 'rows' or 'cols'""")
        
        
if(__name__=="__main__"):  
    try:
        #open image
        im = Image.open('jellyfish.jpg')
        pixelMap = im.load()
        
        #do some manipulations
        sortRect(pixelMap, 80, 209, 952, 1537, which='cols')
        sortRect(pixelMap, 209, 338, 876, 1614, which='cols')
        sortRect(pixelMap, 338, 467, 846, 1630, which='cols')
        sortRect(pixelMap, 467, 596, 846, 1630, which='cols')
        sortRect(pixelMap, 596, 725, 880, 1580, which='cols')
        sortRect(pixelMap, 596, im.height-1, 1580, 1630, which='rows')
        sortRect(pixelMap, 0, im.height-1, 0, 500, which='cols')
        
        #save
        im.show()
        im.save('jellyfishout.jpg')
    except:
        print("Error when trying to read jellyfish!")
