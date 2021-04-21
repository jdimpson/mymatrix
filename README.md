# mymatrix
Simple python wrapper around https://github.com/hzeller/rpi-rgb-led-matrix

This wrapper elects to use python PIL to generate text bitmaps, then passes the bitmap to the matrix library to draw. 

I decided that was easier than figuring out how to use the native text handling of the library, and should also be 
easier to mix text and images should I ever choose to do that.


