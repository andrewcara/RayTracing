from msilib.schema import Class
import numpy as np
import weakref


class intersection_sphere:
    instances = []
    def __init__(self, radius, location, ambient, diffuse, specular, shiny):
        self.radius = radius
        self.location = location
        self.ambient = ambient
        self.diffuse= diffuse
        self.specular = specular
        self.shiny = shiny
        self.__class__.instances.append(weakref.proxy(self))

def unitVector(point_on_screen, centre_of_object, raidus_object, camera_origin):
        
        #a, b and c defined for the quadratic equation, where we are solving for t in the parametirc equation
        #Find where the ray from the camera intersects the object
        #where d is the unit vector from the camera along some ray
        #d_centre_of_object in this case will be centre of the sphere
    
    d = (point_on_screen - camera_origin) / np.linalg.norm(point_on_screen - camera_origin)

    a = np.dot(d, d) #should always be one, but a good check

    b = 2*np.dot(d, (camera_origin - centre_of_object))

    c = ((np.linalg.norm(camera_origin - centre_of_object))**2) - raidus_object**2

    theta = b**2 - 4*a*c

    #theta here is t from the parametric equation. In othere words it is the "time" that the ray will hit the object. Meaning a shorter time indicates a closer object
    t1 = (-b + np.sqrt(theta)) / 2
    t2 = (-b - np.sqrt(theta)) / 2
    if t1 > 0 and t2 > 0:
        return min(t1, t2)
    return None


def closest_point(sphere_object, camera_origin, distance_from_camera):
    minimum = 0
    center = 0
    obj = None

    # This function determines which point is closest to the camera 
    for i, j  in enumerate(sphere_object.instances):
        
        if unitVector(distance_from_camera, j.location, j.radius, camera_origin) != None and minimum == 0:
            minimum = unitVector(distance_from_camera, j.location, j.radius, camera_origin)
            center = j.location
            obj = j
        
        if unitVector(distance_from_camera, j.location, j.radius, camera_origin) != None and minimum != 0:
            if unitVector(distance_from_camera, j.location, j.radius, camera_origin) < minimum:
                center = j.location
                obj = j
            minimum = min(unitVector(distance_from_camera, j.location, j.radius, camera_origin),minimum)

    
    if minimum ==0:
        return minimum, obj
    
    return minimum, obj

def normalize_vector(v):
    v = v/np.linalg.norm(v)
    return v


def light_intersection(sphere_object, center_of_object, light_origin, intersection):
    
    normal_to_surface = normalize_vector(intersection - center_of_object)
    shifted_point = intersection + (1e-5 * normal_to_surface)

    x, _ = closest_point(sphere_object, light_origin['position'], shifted_point)
    
    if x < np.linalg.norm(intersection-light_origin['position']):
        return True
    else:
        return False




    




