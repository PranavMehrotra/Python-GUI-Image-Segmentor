#Imports
from random import randrange
import numpy as np
from PIL import Image

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        # Write your code here

        self.height , self.width = shape
        if(crop_type=='center'):
            self.crop_t = 'c'
        else:
            self.crop_t = 'r'


    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        img = Image.fromarray(image)
        width, height = img.size   # Get dimensions
        if(self.crop_t=='c'):
            left = (width - self.width)/2
            top = (height - self.height)/2
            right = (width + self.width)/2
            bottom = (height + self.height)/2

        else:
            left = int(randrange(0,width-self.width))
            top = int(randrange(0,height-self.height))
            right = left + self.width
            bottom = top + self.height
        img = img.crop((left,top,right,bottom))
        return np.array(img)