#Imports
import numpy as np
from PIL import Image

class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''

        # Write your code here
        if (flip_type=='vertical'):
            self.flip = 'v'
        else:
            self.flip = 'h'
        
    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        img = Image.fromarray(image)
        if(self.flip=='v'):
            img = img.transpose(Image.FLIP_TOP_BOTTOM)
        else:
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
        return np.array(img)
       