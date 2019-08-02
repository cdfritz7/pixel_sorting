This is a simple script to do pixel sorting on an image.
The user can specify rectangles within an image to sort,
and can sort row wise or column wise.

The main function is 'sortRect(image, row1, row2, col1, col2, which='rows')'

Which takes the following parameters:
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

The user can also download the file and edit the code inside the
'if __name__ =='__main__':' block to change the path of the image being edited.
