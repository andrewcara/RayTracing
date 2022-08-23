import sys
image_width = 256
image_height = 256
with open('image.ppm', 'a') as f:
    print("P3\n", image_width , ' ' , image_height , "\n255" ,file=f)

    for j in range(image_width-1, -1, -1):
        sys.stderr.write("Lines remaining {}".format(j)) # Write remaining lines to stderr. Can be very helpful in large rendering procedures
        for i in range(0, image_width):
            r = float(i) / (image_width - 1)
            g = float(j) / (image_height - 1)
            b = 0.25

            ir = int(255.999*r)
            ig = int(255.999*g)
            ib = int(255.999*b)

            print(ir, ' ' , ig, ' ' , ib, file=f) 

sys.stderr.write("Done")
