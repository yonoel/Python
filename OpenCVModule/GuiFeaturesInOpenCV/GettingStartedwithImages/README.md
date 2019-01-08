#Goals
+ Here, you will learn how to read an image, how to display it and how to save it back
+ You will learn these functions : cv.imread(), cv.imshow() , cv.imwrite()
+ Optionally, you will learn how to display images with Matplotlib

#Using OpenCV
## Read an image
Use the function cv.imread() to read an image. The image should be in the working directory or a full path of image should be given.<br>
Second argument is a flag which specifies the way image should be read.
+ cv.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
+ cv.IMREAD_GRAYSCALE : Loads image in grayscale mode
+ cv.IMREAD_UNCHANGED : Loads image as such including alpha channel
- note:Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.
## Display an image
Use the function cv.imshow() to display an image in a window. The window automatically fits to the image size.<br>
First argument is a window name which is a string. second argument is our image. You can create as many windows as you wish, but with different window names.
```
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
```
cv.waitKey() is a keyboard binding function.Its argument is the time in milliseconds. The function waits for specified milliseconds for any keyboard event.<br>
cv.destroyAllWindows() simply destroys all the windows we created. If you want to destroy any specific window, use the function cv.destroyWindow() where you pass the exact window name as the argument.<br>
`See the code below:
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
`
##Write an image
Use the function cv.imwrite() to save an image.
<br>
First argument is the file name, second argument is the image you want to save.
`cv.imwrite('messigray.png',img)
`
warning:
<br>
If you are using a 64-bit machine, you will have to modify k = cv.waitKey(0) line as follows : k = cv.waitKey(0) & 0xFF
<br>
##Using Matplotlib
warning:
<br>
OpenCV follows BGR order, while matplotlib likely follows RGB order.











