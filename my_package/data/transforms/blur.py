#Imports
import numpy as np
from PIL import Image
from PIL import ImageFilter

class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''

    def __init__(self, radius):
        '''
            Arguments:
            radius (int): radius to blur
        '''

        # Write your code here
        self.radii = radius

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        '''
        img = Image.fromarray(image)
        # Write your code here
        copied = img.filter(ImageFilter.GaussianBlur(self.radii))
        return np.array(copied)

