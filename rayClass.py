from msilib.schema import Class
import numpy as np


class intersection_sphere:
    def __init__(self):
        self.radius = 0.7
        self.location = np.array([0, 0, -2.5])

def unitVector(d_camera, centre_of_object, raidus_object, camera_origin):
        
        #a, b and c defined for the quadratic equation, where we are solving for t in the parametirc equation
        #Find where the ray from the camera intersects the object
        #where d is the unit vector from the camera along some ray
        #d_centre_of_object in this case will be centre of the sphere
    
    d = (d_camera - camera_origin) / np.linalg.norm(d_camera - camera_origin)

    a = np.dot(d, d) #should always be one, but a good check

    b = 2*np.dot(d, (camera_origin - centre_of_object))

    c = ((np.linalg.norm(camera_origin - centre_of_object))**2) - raidus_object**2

    theta = b**2 - 4*a*c

    #theta here is t from the parametric equation. In othere words it is the "time" that the ray will hit the object. Meaning a shorter time indicates a closer object

    return theta





