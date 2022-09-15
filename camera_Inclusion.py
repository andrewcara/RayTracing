from locale import normalize
import numpy as np
import math
import rayClass as sphere

image_width = 300
image_height = 200

camera_position = np.array([0,0,2.5]) # X, Y, Z coordinates of the camera position 
light_position = np.array([5,5,5])


top_left_screen = np.array([-1.5,1,-2]) # Orientation defined by looking at supposed screen
top_right_screen = np.array([1.5,1,-2]) # Negative z direction is into the screen, right is positive X and up is positive Y
bottom_left_screen = np.array([-1.5,-1,-2])
bottom_right_screen = np.array([1.5,-1,-2])


sphere1 = sphere.intersection_sphere(0.7, np.array([0,0,-2]))
sphere2 = sphere.intersection_sphere(1.0, np.array([1, 0, -2.1]))
sphere3 = sphere.intersection_sphere(0.5, np.array([-1, -0.25, -2]))



with open('camera_inclusion.ppm', 'a') as f:
    print("P3\n", image_width , ' ' , image_height , "\n255" ,file=f)
    #Now to calculate the distance from each pixel to the camera lense
    position_from_camera = np.array([])
    #iterate through pixels and normalize based on distance from camera to screen
    for j in range(0, image_height):
        
        height_tracker = j*2/image_height + bottom_left_screen[1] #coordinate of the bottom of the screen
        
        
        for i in range(0,image_width):
            width_trakcer = i*3/image_width + top_left_screen[0] # coordinate at the furthest left of the screen
            

            direction_vector = np.array([width_trakcer, height_tracker, -2])




            x, c = sphere.closest_point(sphere.intersection_sphere, camera_position, direction_vector)
            

                                
            
            if x !=0: #if theta is greater that zero the ray intersects with the object, thus we will give a colour of white or (255,255,255) in rgb to those locations
                
                intersection_point = camera_position + (sphere.normalize_vector(direction_vector-camera_position) *x) # Finding the point where the ray from the camera inter

                is_shaded =sphere.light_intersection(sphere.intersection_sphere, c, light_position, intersection_point)
                
                if (is_shaded):
                  ir = int(0)
                  ig = int(0)
                  ib = int(0)
                    
                if(not is_shaded):
                    
                    ir = int(x*25)
                    ig = int(x*25)
                    ib = int(x*25)
                    
                    
            else:
                ir = int(255)
                ig = int(0)
                ib = int(0)

            print(ir, ' ' , ig, ' ' , ib, file=f) 


    #position_from_camera = position_from_camera - min(position_from_camera) / max(position_from_camera) - min(position_from_camera)

    #print(position_from_camera)


