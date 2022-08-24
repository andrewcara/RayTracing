import numpy as np
import math

image_width = 300
image_height = 200

camera_position = np.array([0,0,0]) # X, Y, Z coordinates of the camera position 

top_left_screen = np.array([-1.5,1,-2]) # Orientation defined by looking at supposed screen
top_right_screen = np.array([1.5,1,-2]) # Negative z direction is into the screen, right is positive X and up is positive Y
bottom_left_screen = np.array([-1.5,-1,-2])
bottom_right_screen = np.array([1.5,-1,-2])
maximum_distance = math.sqrt(1.5**2 + 1**2 + 2**2)
minimum_distance = 2


with open('camera_inclusion.ppm', 'a') as f:
    print("P3\n", image_width , ' ' , image_height , "\n255" ,file=f)
    #Now to calculate the distance from each pixel to the camera lense
    position_from_camera = np.array([])
    #iterate through pixels and normalize based on distance from camera to screen
    for j in range(0, image_height):
        
        height_tracker = j*2/image_height + bottom_left_screen[1] #coordinate of the bottom of the screen
        
        
        for i in range(0,image_width):
            width_trakcer = i*3/image_width + top_left_screen[0] # coordinate at the furthest left of the screen
            
            
            pixel_distance = float(np.sqrt
            (np.sum
            (np.array((([width_trakcer,height_tracker,-2]) - camera_position)**2))))
            
            position_from_camera = np.append(position_from_camera, pixel_distance )  # finding the 3D distance from the camera to each pixel on the screen
            
            pixel_distance = (pixel_distance - minimum_distance) / (maximum_distance-minimum_distance)
            ir = int(255*pixel_distance)
            ig = int(255*pixel_distance)
            ib = int(255*pixel_distance)

            print(ir, ' ' , ig, ' ' , ib, file=f) 


    #position_from_camera = position_from_camera - min(position_from_camera) / max(position_from_camera) - min(position_from_camera)

    #print(position_from_camera)

