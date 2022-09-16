from locale import normalize
import numpy as np
import math
import rayClass as sphere

image_width = 300
image_height = 200

camera_position = np.array([0,0,2.5]) # X, Y, Z coordinates of the camera position 
light_position = { 'position': np.array([5, 5, 5]), 'ambient': np.array([1, 1, 1]), 'diffuse': np.array([1, 1, 1]), 'specular': np.array([1, 1, 1])}



top_left_screen = np.array([-1.5,1,-2]) # Orientation defined by looking at supposed screen
top_right_screen = np.array([1.5,1,-2]) # Negative z direction is into the screen, right is positive X and up is positive Y
bottom_left_screen = np.array([-1.5,-1,-2])
bottom_right_screen = np.array([1.5,-1,-2])


sphere1 = sphere.intersection_sphere(0.7, np.array([-0.2, 0, -2]), np.array([0.1, 0, 0]), np.array([0.7, 0, 0]), np.array([1, 1, 1]), 100)
sphere2 = sphere.intersection_sphere(0.2, np.array([0.1, -0.3, -1]), np.array([0.1, 0, 0]), np.array([0.7, 0, 0.7]), np.array([1, 1, 1]), 100)
# sphere3 = sphere.intersection_sphere(0.5, np.array([-1, -0.25, -2]))



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

                is_shaded =sphere.light_intersection(sphere.intersection_sphere, c.location, light_position, intersection_point)
                
                
                normal_to_surface = sphere.normalize_vector(intersection_point - c.location)
                shifted_point = intersection_point + (1e-5 * normal_to_surface)
                if (is_shaded):
                  ir = int(0)
                  ig = int(0)
                  ib = int(0)
                    
                if(not is_shaded):
                    
                    illumination = np.zeros((3))

                    # ambiant
                    illumination += c.ambient * light_position['ambient']

                    # diffuse
                    illumination += c.diffuse * light_position['diffuse'] * np.dot(sphere.normalize_vector(light_position['position'] - shifted_point), normal_to_surface)

                    # specular
                    intersection_to_camera = sphere.normalize_vector(camera_position - intersection_point)

                    H = sphere.normalize_vector(sphere.normalize_vector(light_position['position'] - shifted_point) + intersection_to_camera)
                    illumination += c.specular * light_position['specular'] * np.dot(normal_to_surface, H) ** (c.shiny / 4)
                    illumination = np.clip(illumination, 0, 1)
                
                    ir = illumination[0] *255.999
                    ig = illumination[1] *255.999
                    ib = illumination[2] *255.99
                    
            else:
                ir = int(0)
                ig = int(0)
                ib = int(0)

            print(ir, ' ' , ig, ' ' , ib, file=f) 


    #position_from_camera = position_from_camera - min(position_from_camera) / max(position_from_camera) - min(position_from_camera)

    #print(position_from_camera)


